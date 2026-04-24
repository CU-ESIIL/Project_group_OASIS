from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "stickers"
SIZE = 256

PRIMARY_BLUE = (0x23, 0x4A, 0x65)
ACCENT_BLUE = (0x42, 0xBC, 0xDC)
ACCENT_GREEN = (0x00, 0x71, 0x35)
LIGHT_GREEN = (0x4F, 0xB7, 0x7F)
BODY_TEXT = (0x16, 0x1A, 0x19)
GRAY = (0xE3, 0xE3, 0xE3)
WHITE = (0xFF, 0xFF, 0xFF)


def write_png(path: Path, pixels: list[list[tuple[int, int, int]]]) -> None:
    raw = b"".join(b"\x00" + b"".join(bytes(px) for px in row) for row in pixels)

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def new_canvas() -> list[list[tuple[int, int, int]]]:
    return [[WHITE for _ in range(SIZE)] for _ in range(SIZE)]


def rect(img, x0, y0, x1, y1, color):
    for y in range(max(0, y0), min(SIZE, y1)):
        for x in range(max(0, x0), min(SIZE, x1)):
            img[y][x] = color


def circle(img, cx, cy, r, color):
    r2 = r * r
    for y in range(max(0, cy - r), min(SIZE, cy + r + 1)):
        for x in range(max(0, cx - r), min(SIZE, cx + r + 1)):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r2:
                img[y][x] = color


def line(img, x0, y0, x1, y1, color, width=8):
    steps = max(abs(x1 - x0), abs(y1 - y0), 1)
    for i in range(steps + 1):
        t = i / steps
        x = round(x0 + (x1 - x0) * t)
        y = round(y0 + (y1 - y0) * t)
        circle(img, x, y, width // 2, color)


def polygon(img, points, color):
    min_y = max(0, min(y for _, y in points))
    max_y = min(SIZE - 1, max(y for _, y in points))
    for y in range(min_y, max_y + 1):
        nodes = []
        j = len(points) - 1
        for i, (xi, yi) in enumerate(points):
            xj, yj = points[j]
            if (yi < y <= yj) or (yj < y <= yi):
                nodes.append(round(xi + (y - yi) / (yj - yi) * (xj - xi)))
            j = i
        nodes.sort()
        for a, b in zip(nodes[0::2], nodes[1::2]):
            rect(img, a, y, b + 1, y + 1, color)


def texture(img):
    for y in range(18, SIZE, 17):
        for x in range(11, SIZE, 29):
            if (x * 13 + y * 7) % 5 == 0:
                img[y][x] = GRAY


def frame(img, color=PRIMARY_BLUE):
    rect(img, 0, 0, SIZE, 12, color)
    rect(img, 0, SIZE - 12, SIZE, SIZE, color)
    rect(img, 0, 0, 12, SIZE, color)
    rect(img, SIZE - 12, 0, SIZE, SIZE, color)


def people():
    img = new_canvas()
    frame(img)
    pts = [(78, 86), (152, 70), (178, 142), (96, 166), (142, 204)]
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)]:
        line(img, *pts[a], *pts[b], ACCENT_GREEN, 9)
    for i, pt in enumerate(pts):
        circle(img, *pt, 21 if i != 1 else 25, ACCENT_BLUE if i != 4 else LIGHT_GREEN)
        circle(img, *pt, 9, BODY_TEXT)
    texture(img)
    return img


def question():
    img = new_canvas()
    frame(img)
    cx, cy = 128, 126
    for deg in range(30, 325):
        if 210 < deg < 255:
            continue
        rad = math.radians(deg)
        x = round(cx + 72 * math.cos(rad))
        y = round(cy + 72 * math.sin(rad))
        circle(img, x, y, 9, ACCENT_BLUE)
    circle(img, 156, 198, 12, ACCENT_GREEN)
    polygon(img, [(122, 92), (158, 112), (130, 144), (102, 126)], PRIMARY_BLUE)
    texture(img)
    return img


def tracks():
    img = new_canvas()
    frame(img)
    line(img, 54, 196, 106, 152, PRIMARY_BLUE, 18)
    line(img, 106, 152, 154, 108, PRIMARY_BLUE, 18)
    line(img, 154, 108, 206, 72, ACCENT_GREEN, 18)
    line(img, 154, 108, 202, 156, ACCENT_BLUE, 18)
    line(img, 106, 152, 160, 204, LIGHT_GREEN, 18)
    for pt in [(206, 72), (202, 156), (160, 204)]:
        circle(img, *pt, 15, BODY_TEXT)
    texture(img)
    return img


def data():
    img = new_canvas()
    frame(img)
    for y in range(58, 202, 32):
        line(img, 52, y, 204, y + ((y // 32) % 3 - 1) * 5, GRAY, 5)
    for x in range(58, 202, 32):
        line(img, x, 52, x + ((x // 32) % 3 - 1) * 5, 204, GRAY, 5)
    for x, y, color in [(70, 76, ACCENT_BLUE), (126, 98, PRIMARY_BLUE), (180, 84, ACCENT_GREEN), (94, 150, ACCENT_GREEN), (154, 172, ACCENT_BLUE), (198, 188, PRIMARY_BLUE)]:
        rect(img, x - 10, y - 10, x + 16, y + 16, color)
    texture(img)
    return img


def methods():
    img = new_canvas()
    frame(img)
    polygon(img, [(64, 82), (178, 58), (212, 88), (96, 114)], ACCENT_BLUE)
    polygon(img, [(52, 126), (168, 98), (208, 132), (90, 164)], PRIMARY_BLUE)
    polygon(img, [(72, 174), (184, 146), (218, 178), (104, 210)], ACCENT_GREEN)
    line(img, 92, 120, 182, 98, WHITE, 7)
    line(img, 106, 166, 184, 146, WHITE, 7)
    texture(img)
    return img


def results():
    img = new_canvas()
    frame(img)
    for x, h, color in [(62, 42, GRAY), (94, 68, ACCENT_BLUE), (126, 96, PRIMARY_BLUE), (158, 118, ACCENT_GREEN), (190, 138, LIGHT_GREEN)]:
        rect(img, x, 206 - h, x + 24, 206, color)
    line(img, 56, 176, 94, 154, BODY_TEXT, 7)
    line(img, 94, 154, 126, 126, BODY_TEXT, 7)
    line(img, 126, 126, 158, 96, BODY_TEXT, 7)
    line(img, 158, 96, 204, 72, BODY_TEXT, 7)
    texture(img)
    return img


def outputs():
    img = new_canvas()
    frame(img)
    rect(img, 58, 58, 198, 198, ACCENT_GREEN)
    rect(img, 76, 76, 180, 180, WHITE)
    rect(img, 92, 96, 164, 112, PRIMARY_BLUE)
    rect(img, 92, 128, 164, 142, ACCENT_BLUE)
    rect(img, 92, 158, 138, 172, LIGHT_GREEN)
    polygon(img, [(166, 170), (204, 198), (182, 214), (148, 184)], BODY_TEXT)
    texture(img)
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    makers = {
        "people": people,
        "question": question,
        "tracks": tracks,
        "data": data,
        "methods": methods,
        "results": results,
        "outputs": outputs,
    }
    for name, maker in makers.items():
        write_png(OUT / f"{name}.png", maker())


if __name__ == "__main__":
    main()
