/* ── 思贤学习站 · 主题切换 ── */
(function () {
  var theme = localStorage.getItem('sx_theme');
  if (theme === 'pink') {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-pink.css';
    link.id = 'theme-pink';
    document.head.appendChild(link);
  }
})();

function toggleTheme() {
  var link = document.getElementById('theme-pink');
  if (link) {
    link.remove();
    localStorage.setItem('sx_theme', 'blue');
  } else {
    link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-pink.css';
    link.id = 'theme-pink';
    document.head.appendChild(link);
    localStorage.setItem('sx_theme', 'pink');
  }
}
