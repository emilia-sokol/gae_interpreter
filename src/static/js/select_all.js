function select_all(source) {
  var checkboxes = document.querySelectorAll('[aria-label="to_delete"]');
  for(var i=0, n=checkboxes.length;i<n;i++) {
    checkboxes[i].checked = source.checked;
  }
}