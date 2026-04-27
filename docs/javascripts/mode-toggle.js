(function () {
  const STORAGE_KEY = "oasis-template-guidance";
  const scaffoldTitlePattern = /^(show template guidance|how to edit|d[1-3]-[a-g])/i;

  function pageHasTemplateGuidance() {
    return Boolean(document.querySelector(".oasis-public-mode-marker, .oasis-scaffold"));
  }

  function readShowGuidance() {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    return stored === null ? true : stored === "show";
  }

  function applyGuidanceMode(showGuidance) {
    document.documentElement.classList.toggle("hide-template-guidance", !showGuidance);
    document.body.classList.toggle("hide-template-guidance", !showGuidance);
    document.body.classList.toggle("edit-mode", showGuidance);
    document.body.classList.toggle("public-mode", !showGuidance);
    document.querySelectorAll("[data-oasis-mode-toggle]").forEach((toggle) => {
      toggle.checked = showGuidance;
    });
  }

  function markScaffoldBlocks() {
    document.querySelectorAll(".md-typeset details").forEach((block) => {
      const summary = block.querySelector("summary");
      if (!summary) {
        return;
      }
      const title = summary.textContent.trim();
      if (scaffoldTitlePattern.test(title)) {
        block.classList.add("oasis-scaffold");
      }
    });
  }

  function bindToggles() {
    document.querySelectorAll("[data-oasis-mode-toggle]").forEach((toggle) => {
      if (toggle.dataset.oasisModeBound === "true") {
        return;
      }
      toggle.dataset.oasisModeBound = "true";
      toggle.addEventListener("change", () => {
        const showGuidance = toggle.checked;
        window.localStorage.setItem(STORAGE_KEY, showGuidance ? "show" : "hide");
        applyGuidanceMode(showGuidance);
      });
    });
  }

  function init() {
    markScaffoldBlocks();
    bindToggles();
    applyGuidanceMode(readShowGuidance());

    document.body.classList.toggle("has-template-guidance", pageHasTemplateGuidance());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  }
  document.addEventListener("md-content-replaced", init);
})();
