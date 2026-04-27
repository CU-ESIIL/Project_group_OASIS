(function () {
  function isTypingTarget(target) {
    if (!target) return false;
    const tag = target.tagName ? target.tagName.toLowerCase() : "";
    return tag === "input" || tag === "textarea" || tag === "select" || target.isContentEditable;
  }

  function setPresentationMode(enabled) {
    document.body.classList.toggle("presentation-mode", enabled);
    document.documentElement.classList.toggle("presentation-mode", enabled);
    document.querySelectorAll("[data-oasis-present-toggle]").forEach((button) => {
      button.setAttribute("aria-pressed", enabled ? "true" : "false");
    });
  }

  function ensurePresentationControls() {
    const content = document.querySelector(".md-content__inner");
    if (!content || content.querySelector("[data-oasis-present-toggle]")) {
      return;
    }

    const toolbar = document.createElement("div");
    toolbar.className = "oasis-presentation-toolbar";

    const presentButton = document.createElement("button");
    presentButton.type = "button";
    presentButton.className = "oasis-present-button";
    presentButton.setAttribute("data-oasis-present-toggle", "");
    presentButton.setAttribute("aria-label", "Enter presentation mode");
    presentButton.setAttribute("aria-pressed", "false");
    presentButton.innerHTML = '<span aria-hidden="true">▶</span><span>Present</span>';
    presentButton.addEventListener("click", () => {
      setPresentationMode(!document.body.classList.contains("presentation-mode"));
    });

    const hint = document.createElement("span");
    hint.className = "oasis-present-hint";
    hint.textContent = "Press P to present";

    toolbar.append(presentButton, hint);
    content.prepend(toolbar);
  }

  function ensurePresentationChrome() {
    if (document.querySelector(".oasis-present-exit")) {
      return;
    }

    const exitButton = document.createElement("button");
    exitButton.type = "button";
    exitButton.className = "oasis-present-exit";
    exitButton.textContent = "Exit";
    exitButton.setAttribute("aria-label", "Exit presentation mode. Press Escape to exit.");
    exitButton.addEventListener("click", () => setPresentationMode(false));
    document.body.append(exitButton);

    const identity = document.createElement("div");
    identity.className = "oasis-present-identity";
    identity.textContent = "ESIIL · OASIS · 2026";
    identity.setAttribute("aria-hidden", "true");
    document.body.append(identity);
  }

  function bindShortcuts() {
    if (document.body.dataset.oasisPresentationBound === "true") {
      return;
    }
    document.body.dataset.oasisPresentationBound = "true";
    document.addEventListener("keydown", (event) => {
      if (isTypingTarget(event.target)) {
        return;
      }
      if (event.key === "Escape") {
        setPresentationMode(false);
        return;
      }
      if (event.key.toLowerCase() === "p" && !event.metaKey && !event.ctrlKey && !event.altKey) {
        event.preventDefault();
        setPresentationMode(!document.body.classList.contains("presentation-mode"));
      }
    });
  }

  function init() {
    ensurePresentationControls();
    ensurePresentationChrome();
    bindShortcuts();
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
