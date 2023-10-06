import {Mantenimiento} from "./Crud.js";



let datosTabla;
let datosTablaInicializados = false
const mantenimiento = new Mantenimiento()

const opcionesTabla = {
    "dom":'   <"contenedor_tabla"  <"opciones_tabla" <"#meter.container botonFormulario" B> <"filter" f> <"length" l> ><t><"bottom"p> >',
    // Renderizar el lengthMenu personalizado
    buttons: [
        {
            text: 'Agregar',
            className:'btn btn-primary ',
            init: function (api,node,conf){
                // Agregar los atributos data-bs-toggle y data-bs-target
                $(node).attr('data-bs-toggle', 'modal');
                $(node).attr('data-bs-target', '#staticBackdrop');
                  // Agregar un ID al botón
                 $(node).attr('id', 'btnAgregdarMarca');
            }
        }
    ],
    scrollCollapsey:true,
    scrollY: '400px',
    pageLength: 3, //nombre por defecto (cantidad de filas en cada tabla)
    destroy: true, //indicando que sea una tabla destruible
    lengthMenu: [3, 5, 10, 15], //para el menuto de contenido de la tabla 
    columnDefs: [{
        className: 'text-white text-center',
        targets: [0, 1, 2, 3, 4]//columnas inicia del 0 a n de las que se aplican los cabios
    }, {
        orderable: false, //definimos que columnas no queremos que se ordenen  
        targets: [3, 4]
    }, {//buscando en columnas en espesifico
        searchable: false,
        targets: [3, 4]
    },// {width: '50%',targets:[0]} para el ancho entre columnas 

    ],
    language: {
        "sFilter": "<span class='mi-clase-filtro'>Filtro:</span>", // Nombre de clase personalizado para el filtro
        "sLengthMenu": "<span class='mi-clase-longitud'>Mostrar _MENU_ registros por página</span>" // Nombre de clase personalizado para la longitud
   
        ,"decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
        "infoPostFix": "",
        "thousands": ",",
        "lengthMenu": "Mostrar _MENU_ Entradas",
        "loadingRecords": "Cargando...",
        "processing": "Procesando...",
        "search": "Buscar:",
        "zeroRecords": "Sin resultados encontrados",
        "paginate": {
            "first": "Primero",
            "last": "Ultimo",
            "next": "Siguiente",
            "previous": "Anterior"
        }
    }
}
/*

---|----|---
---|----|---
---|----|---
*/



/////----------------------






/////----------------------


///------------------------
/*
$(document).ready(function () {
    // Obtén el elemento select y la tabla
    var selectElementos = $("#selectElementos");
    var miTabla = $("#datosmarca tbody");

    // Agrega un evento de cambio al elemento select
    selectElementos.on("change", function () {
        var cantidadMostrar = parseInt(selectElementos.val()); // Convierte el valor a un número entero
        var filas = miTabla.find('tr');
        console.log("pollo");
        // Oculta todas las filas de la tabla
        filas.hide();

        // Muestra la cantidad seleccionada de filas
        filas.slice(0, cantidadMostrar).show();
    });
});
///------------------------*/



const iniciarDatosTabla = async () => {
    if (datosTablaInicializados) [
        datosTabla.destroy()
    ]
    await listarMarcas()
    datosTabla = $('#datosmarca').DataTable(opcionesTabla)
    datosTablaInicializados = true
}


window.addEventListener('load', async () => {
    await cargaInicial();
});

const cargaInicial = async () => {
    await iniciarDatosTabla()
};


//cones esta funcion nosotros agregamos filas a la tabla. 
const filaTabla = (elementos) => {
    console.log(elementos.id_marcas)
    let datos = `
    <tr data-id="${elementos.id_marcas}">
        <td  >${elementos.id_marcas}</td>
        <td>${elementos.nombre_marca}</td>
        <td>${elementos.descripcion}</td>
        <td>${elementos.estado}</td>
        <td class = '' >${crearBotonEliminar(elementos.id_marcas)}</td> <!-- Agrega el botón de "Eliminar" -->
    </tr>
    `
    return datos
}

//con esta funicon nosotro agreagamos la funcionalidad a boton eliminar


const agregarBotonEliminar = () => {
    const botonesEliminar = document.querySelectorAll('.btn-eliminar-marca');

    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', function () {
            const idMarcaAEliminar = this.getAttribute('data-id');
            console.log(idMarcaAEliminar);
            eliminarMarca(idMarcaAEliminar);
        });
    });
};



//con esta funcion agregamos todo los datos a la tabla 
const agregarDatosTabla = (datos) => {
    let contenido = '';
    datos.respuesta.marcas.forEach((elementos) => {
        contenido += `
        ${filaTabla(elementos)}
        `;
    });
    tablaBody.innerHTML = contenido;
    mensajemarca.innerHTML = datos.respuesta.mensaje;
}

//listamos las informacion a traves de nuetro backend
const listarMarcas = async () => {
    const datos = await mantenimiento.obtenerDatos('/admon/obtener-marcas/')
    datos.respuesta.marcas = datos.respuesta.marcas.map(marc => {
             marc.estado = marc.estado ? 'Activo' : 'Inactivo';  
             return marc;
            });

    
    if (datos.estado) {
        agregarDatosTabla(datos)
        console.log(datos);
        // Agrega un evento de clic a los botones de "Eliminar" para llamar a la función de eliminación
        agregarBotonEliminar()
    }
    else {
        mensajemarca.innerHTML = 'Error al cargar las marcas';
    }
};


//funciones para guardar datos de coookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//evento para guardar los datos
btGuardarMarca.addEventListener('click', async () => {
    let formAgregar = new FormData(form_agregar_marca);
    const datos = await mantenimiento.agregarDatos('/admon/ingreso-marcas/', formAgregar)

    if (datos.estado) {
        in_nombre.value = ""
        in_descripcion.value = ""
        console.log('------------------');
        console.log(datos.respuesta);
        const fila = filaTabla(datos.respuesta)
        $('#datosmarca').DataTable().row.add($(fila)).draw(false);
        agregarBotonEliminar()
        Swal.fire(
            'Nueva Marca Ingresada!',
            'Preciona clic en el boton!',
            'success'
        )
    }
    else {
        console.log('Error al ingresar Datos');
    }

});





//eliminar datos de tabla 
const crearBotonEliminar = (idMarca) => {
    return `<button class="btn-eliminar-marca btn btn-outline-danger"  data-id="${idMarca}">Eliminar</button>`;
};



const eliminarDatoDeTabla = (idMarca) => {
    // Utiliza el ID de la marca para encontrar la fila correspondiente y eliminarla
    const filaAEliminar = $(`#datosmarca tr[data-id='${idMarca}']`);
    $('#datosmarca').DataTable().row(filaAEliminar).remove().draw(false);
};


//actualizar info 
const crearBotonActualizar = (idMarca) => {
    return `<button class="btn-actualizar-marca" data-id="${idMarca}">Editar</button>`;
};

// Llamada a la función para eliminar una marca cuando se hace clic en el botón "Eliminar"
const eliminarMarca = async (idMarca) => {
    try {
        const dato = { id_marca: idMarca }
        const eliminar = await fetch('/admon/modifica-marcas/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json', //espesifica que se envian datos al servido en formato JSon 
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(dato)//transfomrando nuestro objeto en string json

        });

        if (eliminar.ok) {
            const mensaje = await eliminar.json();
            console.log(mensaje);
            eliminarDatoDeTabla(idMarca);
        }
        else {
            console.error('Error al eliminar datos ')
        }

    } catch (error) {
        console.error(error);
    }
};




