// Documentation pages: the shortcut filter and the "On this page" highlight.
(function () {
  var input = document.getElementById("filter");
  if (input) {
    var tables = Array.prototype.slice.call(document.querySelectorAll(".doc table"));
    var empty = document.getElementById("filter-empty");
    input.addEventListener("input", function () {
      var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
      var any = false;
      tables.forEach(function (table) {
        var shown = 0;
        table.querySelectorAll("tbody tr").forEach(function (row) {
          var text = row.textContent.toLowerCase();
          var match = words.every(function (w) { return text.indexOf(w) !== -1; });
          row.hidden = !match;
          if (match) shown++;
        });
        table.hidden = shown === 0;
        var heading = table.previousElementSibling;
        if (heading && heading.tagName === "H2") heading.hidden = shown === 0;
        if (shown) any = true;
      });
      empty.hidden = any;
    });
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
