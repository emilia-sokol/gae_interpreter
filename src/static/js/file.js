$(document).ready(function () {
  var mapper_file_name = document.getElementById("mapper_file_name");
  var reducer_file_name = document.getElementById("reducer_file_name");

  var data_file_name = document.getElementById("data_file_name");

  var form = document.getElementById("data_form");

  $("input[id='mapper_file']").change(function (e) {
    var $this = $(this);
    mapper_file_name.innerHTML = $this.val().split("\\").pop();
  });

  $("input[id='reducer_file']").change(function (e) {
    var $this = $(this);
    reducer_file_name.innerHTML = $this.val().split("\\").pop();
  });

  $("input[id='data_file']").change(function (e) {
    var $this = $(this);
    data_file_name.innerHTML = $this.val().split("\\").pop();
    form.submit();
  });
});
