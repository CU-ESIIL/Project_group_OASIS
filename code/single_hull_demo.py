"""Single-event ruled time hull plotting helper.

This script provides a lightweight example that builds one ruled vertical
hull for a cleaned FIRED event GeoDataFrame. It mirrors the logic shared in the
project notebook but keeps only the essentials required to explore an
individual event.
"""

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from shapely.geometry import Polygon, MultiPolygon, LineString
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# ---------- helpers you already have (light versions) ----------
def _largest_polygon(geom):
    if geom is None or geom.is_empty:
        return None
    if isinstance(geom, Polygon):
        return geom
    if isinstance(geom, MultiPolygon):
        polys = [p for p in geom.geoms if isinstance(p, Polygon)]
        return max(polys, key=lambda p: p.area) if polys else None
    return None


def _sample_ring_equal_steps(poly: Polygon, n_samples: int = 160):
    """Equal-arclength samples on exterior; returns (N, 2)."""
    if poly is None or poly.is_empty:
        return None
    ring = LineString(poly.exterior.coords)
    if ring.coords and ring.coords[0] == ring.coords[-1]:
        ring = LineString(list(ring.coords)[:-1])
    L = ring.length
    if not np.isfinite(L) or L <= 0:
        return None
    s = np.linspace(0, L, n_samples, endpoint=False)
    pts = np.array([ring.interpolate(d).coords[0] for d in s], float)
    return pts


def _center_xy(xy):
    """Remove centroid drift if you want a vertical funnel."""
    return xy - xy.mean(axis=0)


# ---------- ruled envelope (vertical hull) ----------
def plot_ruled_time_hull(
    eg_clean: gpd.GeoDataFrame,
    *,
    date_col="date",
    z_col="event_day",
    n_ring_samples=200,
    n_theta=128,
    center_each_day=True,
    crs_epsg=5070,
    smooth_over_z=3,
    cmap="cividis",
    wall_alpha=0.35,
    edge_alpha=0.25,
    elev=26,
    azim=-58,
    figsize=(9, 8),
):
    """Build a vertical ruled surface for a single cleaned FIRED event."""
    eg = eg_clean.copy()
    eg[date_col] = pd.to_datetime(eg[date_col], errors="coerce")
    eg = eg.sort_values(date_col).reset_index(drop=True)

    # select Z (event_day if present, else 1..N)
    Z = eg[z_col].to_numpy(float) if z_col in eg.columns else np.arange(1, len(eg) + 1, float)

    # CRS
    if crs_epsg is not None:
        try:
            eg = eg.to_crs(epsg=crs_epsg)
        except Exception:
            pass

    # sample per-day largest ring → XY arrays (centered if requested)
    rings = []
    for g in eg.geometry:
        poly = _largest_polygon(g)
        xy = _sample_ring_equal_steps(poly, n_ring_samples) if poly is not None else None
        if xy is None:
            rings.append(None)
            continue
        if center_each_day:
            xy = _center_xy(xy)
        rings.append(xy)

    keep = [i for i, xy in enumerate(rings) if xy is not None]
    if len(keep) < 2:
        raise ValueError("Not enough valid days to build a hull.")
    rings = [rings[i] for i in keep]
    Z = Z[keep]
    dates = eg.iloc[keep][date_col]

    # support directions
    thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
    U = np.stack([np.cos(thetas), np.sin(thetas)], axis=1)

    # compute radius r(θ,z) = max_x in ring ( x·u(θ) )
    R = np.zeros((len(rings), n_theta), dtype=float)
    for iz, xy in enumerate(rings):
        dots = U @ xy.T
        R[iz, :] = dots.max(axis=1)

    # optional smoothing across Z (to avoid jagged walls)
    if smooth_over_z and smooth_over_z > 1 and smooth_over_z % 2 == 1:
        from scipy.ndimage import uniform_filter1d

        R = uniform_filter1d(R, size=smooth_over_z, axis=0, mode="nearest")

    # build mesh of points P(θ,z) = r * u
    M, T = R.shape
    points3d = np.zeros((M, T, 3), dtype=float)
    points3d[:, :, 0] = R * U[None, :, 0]
    points3d[:, :, 1] = R * U[None, :, 1]
    points3d[:, :, 2] = Z[:, None]

    # triangulate as quads between (z_i, theta_j) and (z_{i+1}, theta_{j+1})
    quads = []
    for i in range(M - 1):
        for j in range(T):
            jn = (j + 1) % T
            v1 = points3d[i, j]
            v2 = points3d[i, jn]
            v3 = points3d[i + 1, jn]
            v4 = points3d[i + 1, j]
            if not np.all(np.isfinite([v1, v2, v3, v4])):
                continue
            quads.append([v1, v2, v3, v4])

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")

    hull_color = plt.get_cmap(cmap)(0.6)
    wall = Poly3DCollection(
        quads,
        facecolors=(hull_color[0], hull_color[1], hull_color[2], wall_alpha),
        edgecolors=(0, 0, 0, edge_alpha),
        linewidths=0.25,
    )
    if hasattr(wall, "set_zsort"):
        wall.set_zsort("min")
    ax.add_collection3d(wall)

    xmin = np.nanmin(points3d[:, :, 0])
    xmax = np.nanmax(points3d[:, :, 0])
    ymin = np.nanmin(points3d[:, :, 1])
    ymax = np.nanmax(points3d[:, :, 1])
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(Z.min(), Z.max())

    km_fmt = FuncFormatter(lambda v, pos: f"{v / 1000:.1f}")
    ax.xaxis.set_major_formatter(km_fmt)
    ax.yaxis.set_major_formatter(km_fmt)
    ax.set_xlabel("X (km)")
    ax.set_ylabel("Y (km)")
    ax.set_zlabel("Event day")

    ax.view_init(elev=elev, azim=azim)
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.06, top=0.92)

    t0 = dates.iloc[0].date() if dates.notna().any() else "?"
    t1 = dates.iloc[-1].date() if dates.notna().any() else "?"
    ax.set_title(f"Vertical ruled hull — {t0} → {t1}  (θ={n_theta}, days={M})")
    plt.show()
    return fig, ax


if __name__ == "__main__":
    raise SystemExit(
        "Import this module and call plot_ruled_time_hull(eg_clean) after cleaning "
        "your FIRED daily GeoDataFrame."
    )
