/* ---------------------------------------------------------------
   Horizontal scroll arrows on the top tab bar.
   Injects two arrow buttons over the tab list and toggles their
   visibility based on whether the list can scroll left / right.
   Companion stylesheet: docs/assets/stylesheets/extra.css
   --------------------------------------------------------------- */

(function () {
  function init() {
    var tabs = document.querySelector(".md-tabs");
    if (!tabs) return;
    var list = tabs.querySelector(".md-tabs__list");
    if (!list) return;

    // Avoid duplicate injection if init runs twice (e.g. instant nav).
    if (tabs.querySelector(".md-tabs__scroll-arrow")) return;

    var leftBtn = document.createElement("button");
    leftBtn.className = "md-tabs__scroll-arrow md-tabs__scroll-arrow--left";
    leftBtn.setAttribute("aria-label", "Scroll tabs left");
    leftBtn.setAttribute("type", "button");
    leftBtn.innerHTML = "‹"; // ‹

    var rightBtn = document.createElement("button");
    rightBtn.className = "md-tabs__scroll-arrow md-tabs__scroll-arrow--right";
    rightBtn.setAttribute("aria-label", "Scroll tabs right");
    rightBtn.setAttribute("type", "button");
    rightBtn.innerHTML = "›"; // ›

    tabs.appendChild(leftBtn);
    tabs.appendChild(rightBtn);

    function refresh() {
      var canLeft = list.scrollLeft > 4;
      var canRight = list.scrollLeft < list.scrollWidth - list.clientWidth - 4;
      leftBtn.style.display = canLeft ? "flex" : "none";
      rightBtn.style.display = canRight ? "flex" : "none";
    }

    leftBtn.addEventListener("click", function () {
      list.scrollBy({ left: -240, behavior: "smooth" });
    });
    rightBtn.addEventListener("click", function () {
      list.scrollBy({ left: 240, behavior: "smooth" });
    });

    list.addEventListener("scroll", refresh, { passive: true });
    window.addEventListener("resize", refresh);

    // Initial check after fonts/icons render.
    setTimeout(refresh, 150);
    setTimeout(refresh, 500);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
