(function () {
  const ALLOWED_EXTENSIONS = /\.(png|jpe?g|webp|gif)$/i;
  const EMPTY_MESSAGE = "No report-out images yet. Add image paths to the matching gallery manifest in docs/assets/report-out/. You can point to any image under docs/assets/.";

  function parseGalleryYaml(text) {
    const trimmed = text.trim();
    if (!trimmed || trimmed === "[]") {
      return [];
    }

    const items = [];
    let current = null;
    trimmed.split(/\r?\n/).forEach((line) => {
      const clean = line.trim();
      if (!clean || clean.startsWith("#")) {
        return;
      }
      if (clean.startsWith("- ")) {
        current = {};
        items.push(current);
        const rest = clean.slice(2).trim();
        if (rest.includes(":")) {
          const [key, ...valueParts] = rest.split(":");
          current[key.trim()] = valueParts.join(":").trim().replace(/^["']|["']$/g, "");
        }
        return;
      }
      if (current && clean.includes(":")) {
        const [key, ...valueParts] = clean.split(":");
        current[key.trim()] = valueParts.join(":").trim().replace(/^["']|["']$/g, "");
      }
    });

    return items
      .map((item) => {
        const src = item.src || (item.file ? `assets/report-out/${item.file}` : "");
        return { ...item, src };
      })
      .filter((item) => item.src && ALLOWED_EXTENSIONS.test(item.src));
  }

  function showMessage(container, message) {
    container.innerHTML = "";
    const placeholder = document.createElement("p");
    placeholder.className = "oasis-report-out-gallery__empty";
    placeholder.textContent = message;
    container.append(placeholder);
  }

  function renderGallery(container, items) {
    if (!items.length) {
      showMessage(container, EMPTY_MESSAGE);
      return;
    }

    const grid = document.createElement("div");
    grid.className = "oasis-report-out-gallery__grid";

    items.forEach((item) => {
      const figure = document.createElement("figure");
      figure.className = "oasis-report-out-gallery__item";

      const image = document.createElement("img");
      image.src = item.src;
      image.alt = item.alt || item.caption || item.src;
      image.loading = "lazy";
      figure.append(image);

      if (item.caption) {
        const caption = document.createElement("figcaption");
        caption.textContent = item.caption;
        figure.append(caption);
      }

      grid.append(figure);
    });

    container.innerHTML = "";
    container.append(grid);
  }

  function initGallery(container) {
    const manifest = container.getAttribute("data-manifest");
    if (!manifest) {
      showMessage(container, EMPTY_MESSAGE);
      return;
    }

    fetch(manifest, { cache: "no-cache" })
      .then((response) => (response.ok ? response.text() : ""))
      .then((text) => renderGallery(container, parseGalleryYaml(text)))
      .catch(() => showMessage(container, EMPTY_MESSAGE));
  }

  function init() {
    document.querySelectorAll("[data-report-out-gallery]").forEach(initGallery);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  }
})();
