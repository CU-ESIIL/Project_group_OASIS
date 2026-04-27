(function () {
  const STORAGE_KEY = "oasis-edit-mode";
  const scaffoldTitlePattern = /^(show template guidance|how to edit|d[1-3]-[a-g])/i;

  function isFrontPageWithToggle() {
    return Boolean(document.querySelector(".oasis-public-mode-marker"));
  }

  function readEditMode() {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    return stored === null ? true : stored === "true";
  }

  function applyMode(editMode) {
    document.body.classList.toggle("edit-mode", editMode);
    document.body.classList.toggle("public-mode", !editMode);
    document.querySelectorAll("[data-oasis-mode-toggle]").forEach((toggle) => {
      toggle.checked = editMode;
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

  function buildToggle() {
    const content = document.querySelector(".md-content__inner");
    const marker = document.querySelector(".oasis-public-mode-marker");
    if (!content || !marker || document.querySelector(".oasis-mode-toggle")) {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "oasis-mode-toggle";
    wrapper.innerHTML = `
      <label class="oasis-mode-toggle__label">
        <input type="checkbox" data-oasis-mode-toggle>
        <span class="oasis-mode-toggle__control" aria-hidden="true"></span>
        <span class="oasis-mode-toggle__text">Show template guidance</span>
      </label>
    `;

    const firstHeading = content.querySelector("h1");
    if (firstHeading) {
      firstHeading.insertAdjacentElement("afterend", wrapper);
    } else {
      marker.insertAdjacentElement("afterend", wrapper);
    }

    const checkbox = wrapper.querySelector("[data-oasis-mode-toggle]");
    checkbox.addEventListener("change", () => {
      const editMode = checkbox.checked;
      window.localStorage.setItem(STORAGE_KEY, String(editMode));
      applyMode(editMode);
    });
  }

  function init() {
    if (!isFrontPageWithToggle()) {
      return;
    }
    markScaffoldBlocks();
    buildToggle();
    applyMode(readEditMode());
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
