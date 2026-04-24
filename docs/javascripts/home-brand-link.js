(() => {
  const homeLink = Array.from(document.querySelectorAll(".md-nav__link, .md-tabs__link"))
    .find((link) => link.textContent.trim() === "Home");

  const homeHref = homeLink?.getAttribute("href") || ".";

  const linkHomeBrand = () => {
    document.querySelectorAll("a.md-logo").forEach((logo) => {
      if (logo.closest(".md-header")) return;
      logo.setAttribute("href", homeHref);
      logo.setAttribute("title", "Home");
      logo.setAttribute("aria-label", "Home");
    });

    document.querySelectorAll(".md-sidebar--primary .md-nav__title").forEach((title) => {
      if (title.dataset.homeBrandLinked === "true") return;
      title.dataset.homeBrandLinked = "true";
      title.addEventListener("click", (event) => {
        const target = event.target instanceof Element ? event.target : event.target.parentElement;
        if (target?.closest("a")) return;
        window.location.href = homeHref;
      });
      title.setAttribute("role", "link");
      title.setAttribute("tabindex", "0");
      title.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          window.location.href = homeHref;
        }
      });
    });
  };

  linkHomeBrand();
  if (typeof document$ !== "undefined") {
    document$.subscribe(linkHomeBrand);
  }
})();
