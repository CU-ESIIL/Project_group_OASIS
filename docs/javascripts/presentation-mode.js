(function () {
  function isTypingTarget(target) {
    if (!target) return false;
    const tag = target.tagName ? target.tagName.toLowerCase() : "";
    return tag === "input" || tag === "textarea" || tag === "select" || target.isContentEditable;
  }

  function isHomePage() {
    const path = window.location.pathname.replace(/\/+$/, "");
    return (
      path === "" ||
      path.endsWith("/index") ||
      path.endsWith("/index.html") ||
      Boolean(document.querySelector(".oasis-public-mode-marker"))
    );
  }

  function markReportOutBlocks() {
    document.querySelectorAll(".oasis-report-out-visible").forEach((element) => {
      element.classList.remove("oasis-report-out-visible");
    });

    ["report-out-day2", "report-out-day3"].forEach((id) => {
      const heading = document.getElementById(id);
      let element = heading;
      while (element) {
        element.classList.add("oasis-report-out-visible");
        element = element.nextElementSibling;
        if (element?.tagName?.toLowerCase() === "h2") {
          break;
        }
      }
    });
  }

  function setPresentationMode(enabled) {
    if (enabled && !isHomePage()) {
      return;
    }
    if (enabled) {
      markReportOutBlocks();
    }
    document.body.classList.toggle("presentation-mode", enabled);
    document.documentElement.classList.toggle("presentation-mode", enabled);
    document.querySelectorAll("[data-oasis-present-toggle]").forEach((button) => {
      button.setAttribute("aria-pressed", enabled ? "true" : "false");
    });
  }

  function getPresentationControlTarget() {
    const sidebar = document.querySelector(".md-sidebar--secondary .md-sidebar__inner");
    if (sidebar) {
      let utilities = sidebar.querySelector(".oasis-sidebar-utilities");
      if (!utilities) {
        utilities = document.createElement("div");
        utilities.className = "oasis-sidebar-utilities";
        sidebar.append(utilities);
      }
      return { element: utilities, inSidebar: true };
    }

    const content = document.querySelector(".md-content__inner");
    return content ? { element: content, inSidebar: false } : null;
  }

  function ensurePresentationControls() {
    if (!isHomePage()) {
      document.querySelector(".oasis-presentation-toolbar")?.remove();
      setPresentationMode(false);
      return;
    }

    const target = getPresentationControlTarget();
    if (!target) {
      return;
    }

    const existingToolbar = document.querySelector(".oasis-presentation-toolbar");
    if (existingToolbar) {
      if (existingToolbar.parentElement !== target.element) {
        target.element.append(existingToolbar);
      }
      existingToolbar.classList.toggle("oasis-presentation-toolbar--sidebar", target.inSidebar);
      existingToolbar.classList.toggle("oasis-presentation-toolbar--content", !target.inSidebar);
      return;
    }

    const toolbar = document.createElement("div");
    toolbar.className = "oasis-presentation-toolbar";
    toolbar.classList.toggle("oasis-presentation-toolbar--sidebar", target.inSidebar);
    toolbar.classList.toggle("oasis-presentation-toolbar--content", !target.inSidebar);

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
    target.element.append(toolbar);
  }

  function ensurePresentationChrome() {
    if (!isHomePage()) {
      document.querySelector(".oasis-present-exit")?.remove();
      document.querySelector(".oasis-present-identity")?.remove();
      return;
    }

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
      if (!isHomePage()) {
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
