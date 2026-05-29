/* ── 思贤学习站 · 主题切换（蓝／粉／棉花糖） ── */
(function () {
  var theme = localStorage.getItem('sx_theme');
  if (theme === 'pink') {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-pink.css';
    link.id = 'theme-pink';
    document.head.appendChild(link);
  } else if (theme === 'marshmallow') {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-marshmallow.css';
    link.id = 'theme-marshmallow';
    document.head.appendChild(link);
  }
})();

function removeTheme(id) {
  var el = document.getElementById(id);
  if (el) el.remove();
}

function toggleTheme() {
  var current = localStorage.getItem('sx_theme') || 'blue';
  removeTheme('theme-pink');
  removeTheme('theme-marshmallow');

  if (current === 'blue') {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-pink.css';
    link.id = 'theme-pink';
    document.head.appendChild(link);
    localStorage.setItem('sx_theme', 'pink');
  } else if (current === 'pink') {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'css/theme-marshmallow.css';
    link.id = 'theme-marshmallow';
    document.head.appendChild(link);
    localStorage.setItem('sx_theme', 'marshmallow');
  } else {
    localStorage.setItem('sx_theme', 'blue');
  }
}
