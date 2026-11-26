// Documentation pages: the shortcut filter and the "On this page" highlight.
(function () {
  var input = document.getElementById("filter");
  if (input) {
    var unbound = document.getElementById("show-unbound");
    var cards = Array.prototype.slice.call(document.querySelectorAll(".sc-card"));
    var empty = document.getElementById("filter-empty");
    var apply = function () {
      var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
      var showUnbound = unbound.checked || words.length > 0;
      var any = false;
      cards.forEach(function (card) {
        var shown = 0;
        card.querySelectorAll(".sc").forEach(function (item) {
          var text = (item.textContent + " " + (item.getAttribute("title") || "")).toLowerCase();
          var match = words.every(function (w) { return text.indexOf(w) !== -1; });
          var visible = match && (showUnbound || !item.classList.contains("unbound"));
          item.hidden = !visible;
          if (visible) shown++;
        });
        card.hidden = shown === 0;
        if (shown) any = true;
      });
      empty.hidden = any;
    };
    input.addEventListener("input", apply);
    unbound.addEventListener("change", apply);
    apply();
  }

  var links = document.querySelectorAll(".toc a");
  if (!links.length || !("IntersectionObserver" in window)) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      links.forEach(function (a) { a.classList.remove("active"); });
      var a = byId[e.target.id];
      if (a) a.classList.add("active");
    });
  }, { rootMargin: "-80px 0px -70% 0px" });
  document.querySelectorAll(".doc h2[id]").forEach(function (h) { observer.observe(h); });
})();
