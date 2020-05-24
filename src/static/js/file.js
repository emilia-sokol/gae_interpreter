$(document).ready(function () {
  var mapper_file_name = document.getElementById("mapper_file_name");
  var reducer_file_name = document.getElementById("reducer_file_name");

  $("input[id='mapper_file']").change(function (e) {
    var $this = $(this);
    mapper_file_name.innerHTML = $this.val().split("\\").pop();
  });

  $("input[id='reducer_file']").change(function (e) {
    var $this = $(this);
    reducer_file_name.innerHTML = $this.val().split("\\").pop();
  });

  var btn = document.getElementById("startProcessing");
  var form = document.querySelector("form");
  btn.addEventListener("click", function () {
    form.reset();
    mapper_file_name.innerHTML = "Choose mapper";
    reducer_file_name.innerHTML = "Choose reducer";
  });
});
