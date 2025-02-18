function output(inp) {
  document.body.appendChild(document.createElement("pre")).innerHTML = inp;
}

function syntaxHighlight(json) {
  json = json
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  return json.replace(
    /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
    function (match) {
      var cls = "number";
      if (/^"/.test(match)) {
        if (/:$/.test(match)) {
          cls = "key";
        } else {
          cls = "string";
        }
      } else if (/true|false/.test(match)) {
        cls = "boolean";
      } else if (/null/.test(match)) {
        cls = "null";
      }
      return '<span class="' + cls + '">' + match + "</span>";
    }
  );
}

var obj = {
  0: { type: "temp", value: "45,5", id: "user_id" },
  1: { type: "text", value: "some important message" },
};
var str = JSON.stringify(obj, undefined, 4);

document.getElementById("json_example").innerHTML = syntaxHighlight(str);
// output(str);
// output(syntaxHighlight(str));
