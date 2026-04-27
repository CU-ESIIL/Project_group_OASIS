(function () {
  const STORAGE_KEY = "oasis-template-guidance";
  const scaffoldTitlePattern = /(?:show template guidance|template guidance|how to edit|replace this|d[1-3]-[a-g]|image swap|whiteboard|first data plot|how to replace)/i;

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
    document.querySelectorAll(".template-guidance-toggle__text").forEach((label) => {
      label.textContent = showGuidance ? "Guidance on" : "Guidance off";
    });
    if (showGuidance) {
      expandTemplateGuidanceBlocks();
    }
  }

  function updateHeaderTitle() {
    const titleTarget = document.querySelector(".md-header__topic:first-child .md-ellipsis");
    const pageHeading = document.querySelector(".md-typeset h1");
    if (!titleTarget || !pageHeading) {
      return;
    }
    titleTarget.textContent = pageHeading.textContent.trim();
  }

  function markScaffoldBlocks() {
    document.querySelectorAll(".md-typeset details, .md-typeset .admonition").forEach((block) => {
      const titleNode = block.querySelector("summary, .admonition-title");
      const title = titleNode ? titleNode.textContent.trim() : "";
      const text = block.textContent.trim();
      if (scaffoldTitlePattern.test(title) || scaffoldTitlePattern.test(text)) {
        block.classList.add("template-guidance-block", "oasis-scaffold");
      }
    });
  }

  function expandTemplateGuidanceBlocks() {
    document.querySelectorAll("details.template-guidance-block").forEach((block) => {
      block.setAttribute("open", "");
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
    updateHeaderTitle();

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
