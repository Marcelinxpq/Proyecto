function cerrarss() {
  var form = document.createElement("form");
  form.method = "POST";
  form.action = "/logout";
  document.body.appendChild(form);
  form.submit();
}

function borrar(entradaId) {
  if (confirm("¿Estás seguro de que quieres eliminar esta entrada?")) {
      var form = document.createElement("form");
      form.method = "POST";
      form.action = "/borrar/" + entradaId;

      var methodField = document.createElement("input");
      methodField.type = "hidden";
      methodField.name = "_method";
      methodField.value = "DELETE";
      form.appendChild(methodField);

      document.body.appendChild(form);
      form.submit();
  }
}

function comprobarClave() {
    let contraseña = document.getElementById("contraseña").value
    let cocontraseña = document.getElementById("cocontraseña").value

    if (contraseña == cocontraseña) {
      document.getElementById("registro").submit()
    }
    else {
      alert("Las contraseñas no coinciden")
    }
}