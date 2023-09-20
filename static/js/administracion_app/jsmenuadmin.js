

function mostrarContenido(idContenedor) {
    var contenedor = document.getElementById("contenedor-" + idContenedor);
    contenedor.style.display = "block";
}

// Para ocultar el contenido cuando se hace clic en el fondo gris
var contenedores = document.querySelectorAll(".contenedor");
contenedores.forEach(function (contenedor) {
    contenedor.addEventListener("click", function (e) {
        if (e.target === contenedor) {
            contenedor.style.display = "none";
        }
    });
});


function agregarFila() {
    // Obtener los valores de los campos de entrada
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var username = document.getElementById("username").value;
    var contrasena = document.getElementById("contrasena").value;
    var estado = document.getElementById("estado").value;

    // Obtener la tabla
    var table = document.getElementById("tablaBody");

    // Crear una nueva fila
    var newRow = table.insertRow();

    // Crear celdas para la nueva fila
    var cellNum = newRow.insertCell(0);
    var cellNombre = newRow.insertCell(1);
    var cellAcceso = newRow.insertCell(2);
    var cellEmail = newRow.insertCell(3);
    var cellUsername = newRow.insertCell(4);
    var cellContrasena = newRow.insertCell(5);
    var cellEstado = newRow.insertCell(6);

    // Asignar valores a las celdas
    cellNum.textContent = table.rows.length;
    cellNombre.textContent = nombre;
    cellAcceso.textContent = "Acceso"; // Puedes definir esta parte según tus necesidades
    cellEmail.textContent = email;
    cellUsername.textContent = username;
    cellContrasena.textContent = contrasena;
    cellEstado.textContent = estado;

    // Limpiar los campos de entrada
    document.getElementById("nombre").value = "";
    document.getElementById("email").value = "";
    document.getElementById("username").value = "";
    document.getElementById("contrasena").value = "";
    document.getElementById("estado").value = "activo";
}


