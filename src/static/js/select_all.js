function select_all(source, name) {
  var checkboxes = document.querySelectorAll('[aria-label="' + name + '"]');
  for (var i = 0, n = checkboxes.length; i < n; i++) {
    checkboxes[i].checked = source.checked;
  }
}
