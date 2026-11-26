// Home page: screenshots open large on the page (never navigate away), and the theme switcher.
(function () {
  var box = document.getElementById("lightbox");
  var themeImg = document.getElementById("theme-img");
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".theme-tab"));

  // ---- theme switcher
  function showTheme(tab) {
    tabs.forEach(function (t) { t.setAttribute("aria-selected", t === tab ? "true" : "false"); });
    var src = tab.getAttribute("data-src");
    themeImg.src = src;
    themeImg.alt = "The editor in the " + tab.getAttribute("data-name") + " theme";
    themeImg.parentNode.setAttribute("href", src);
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { showTheme(tab); });
    tab.addEventListener("keydown", function (e) {
      var step = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
      if (!step) return;
      var next = tabs[(i + step + tabs.length) % tabs.length];
      next.focus();
      showTheme(next);
      e.preventDefault();
    });
  });
  // the other theme pictures load once the page is idle, so a switch is instant
  window.addEventListener("load", function () {
    tabs.forEach(function (t) { new Image().src = t.getAttribute("data-src"); });
  });

  // ---- lightbox
  if (!box || typeof box.showModal !== "function") return;  // old browser: links open the picture
  var img = box.querySelector("img");
  var cap = box.querySelector("figcaption");
  var list = [];
  var at = 0;

  function items(link) {
    if (link.closest(".theme-shot")) {
      return tabs.map(function (t) { return { src: t.getAttribute("data-src"), caption: t.getAttribute("data-name") }; });
    }
    return Array.prototype.slice.call(document.querySelectorAll(".shots .zoom")).map(function (a) {
      var fc = a.parentNode.querySelector("figcaption");
      return { src: a.getAttribute("href"), caption: fc ? fc.textContent : "" };
    });
  }
  function show(i) {
    at = (i + list.length) % list.length;
    img.src = list[at].src;
    img.alt = list[at].caption;
    cap.textContent = list[at].caption;
  }
  document.querySelectorAll(".zoom").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      list = items(a);
      var href = a.getAttribute("href");
      var i = list.findIndex(function (x) { return x.src === href; });
      show(i < 0 ? 0 : i);
      box.showModal();
      box.focus();  // arrows and Esc work at once; no button starts out focused
    });
  });
  box.querySelector(".lb-close").addEventListener("click", function () { box.close(); });
  box.querySelector(".lb-prev").addEventListener("click", function () { show(at - 1); });
  box.querySelector(".lb-next").addEventListener("click", function () { show(at + 1); });
  box.addEventListener("click", function (e) { if (e.target === box) box.close(); });  // the dark area around
  box.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") { show(at + 1); e.preventDefault(); }
    if (e.key === "ArrowLeft") { show(at - 1); e.preventDefault(); }
  });
})();
