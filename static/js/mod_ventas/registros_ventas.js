import {Mantenimiento, AlertasBotones,crearBotonEliminar } from "../Crud.js";
const mantenimiento = new Mantenimiento()
const alertas = new AlertasBotones()
const opcionesTabla = {
     buttons: [
        {
            text: 'Agregar',
            className:'btn btn-primary ',
            init: function (api,node,conf){
                // Agregar los atributos data-bs-toggle y data-bs-target
                $(node).attr('data-bs-toggle', 'modal');
                $(node).attr('data-bs-target', '#staticBackdrop');
                  // Agregar un ID al botón
                 $(node).attr('id', 'btnAgregarDatos');
            }
        }
    ],
    
    scrollCollapse:true,
    scrollY: '400px',
    pageLength: 7, //nombre por defecto (cantidad de filas en cada tabla)
    destroy: true, //indicando que sea una tabla destruible
    lengthMenu: [3,7, 5, 10, 15], //para el menuto de contenido de la tabla 
    columnDefs: [{
        className: 'text-white text-center ',
        targets: [0, 1, 2, 3, 4,5]//columnas inicia del 0 a n de las que se aplican los cabios
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

window.addEventListener('load',()=>{
    console.log('buena george')
    // agregarFuncionBtnEliminar()
    $('#registroventas').DataTable(opcionesTabla)
    
})


id_fk_id_producto1.addEventListener('change',async()=>{
    const id = id_fk_id_producto1.value;
    const datos = await mantenimiento.obtenerDatosUrl(`/usuario-ventas/obtener-datos-inventario/${id}/`)
    try {
        input_stock.value = datos.total_stock;
        input_precio.value = datos.precio_venta
    }
    catch (e) {
        input_stock.value = 0;
        input_precio.value = 0
    }

    
})


//! --------------------- fecha --------------------      
let fechaCompraInput = document.getElementById('fechacompra');

// Crea una nueva instancia de la fecha actual
let fechaActual = new Date();

// Formatea la fecha actual en el formato requerido para el campo 'date'
let dia = fechaActual.getDate().toString().padStart(2, '0');
let mes = (fechaActual.getMonth() + 1).toString().padStart(2, '0');
let año = fechaActual.getFullYear();

let fechaFormateada = `${año}-${mes}-${dia}`;

// Asigna la fecha formateada al campo de entrada de fecha
fechaCompraInput.value = fechaFormateada;