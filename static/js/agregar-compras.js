///otros pora agregar productos 
import {Mantenimiento, AlertasBotones,crearBotonEliminar } from "./Crud.js";
const mantenimiento = new Mantenimiento()
const alertas = new AlertasBotones()
let totalPago = 0
let totalDescuento = 0
let totalSinDescuento = 0

const opcionesTabla = {
    "dom":' <"opciones_tabla" <"#meter.container botonFormulario" B><"filter" f > <"length" l > > <t> <p>',
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
    scrollCollapse:true,
    scrollY: '400px',
    pageLength: 3, //nombre por defecto (cantidad de filas en cada tabla)
    destroy: true, //indicando que sea una tabla destruible
    lengthMenu: [3, 5, 10, 15], //para el menuto de contenido de la tabla 
    columnDefs: [{
        className: 'text-white text-center',
        targets: [0, 1, 2, 3, 4,5,6,7]//columnas inicia del 0 a n de las que se aplican los cabios
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


window.addEventListener('load', () => {
     agregarFuncionBtnEliminar();
    $('#datosdetalle').DataTable(opcionesTabla);
});


const agregarFuncionBtnEliminar = () => {
    const botonesEliminar = document.querySelectorAll('.btn-eliminar-producto');
    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', function () {

            const identificador = this.getAttribute('data-id');
            alertas.eliminar(identificador,eliminarProducto)
            console.log(identificador);

        });
    });
};


//! funcion eliminar tipo collback
const eliminarProducto= async(id)=>{
    const respuesta = await mantenimiento.eliminarDato(`/admon/agregar-compras/${id}/`,id)
    console.log(respuesta);
    if (respuesta.ok){
        mantenimiento.eliminarFilaTabla(id,'datosdetalle')
        console.log('-------------------------');
        console.log(respuesta);
        console.log('-------------------------');
    }
    return respuesta
}

//Buena frank 
// lo siento george no estamos ayudando :( so😪oooooolo
//bueena goerge dame una terminal bb WILSON LO SIENTO 😫
//xd 🤣🤣🤣🤣🤣
//ahi esta frank
//perame estoy arreglando 
//TIENE ERROR VA 
btGuardarDato.addEventListener('click', async (e) => {
    //
    e.preventDefault()
    const id = btGuardarDato.getAttribute('data-id')
    console.log(id);
    let formAgregar = new FormData(form_compra_producto);
    const jSonObjetos = mantenimiento.formulariosAObjeto(formAgregar)
    
    //convertirStrNumeric(jSonObjetos)
    operacionesAgregar(jSonObjetos)
    console.log(jSonObjetos);
    console.log('--------------------------------');
    console.log('total compra sin descuento:', totalSinDescuento);
    console.log('total descuento:', totalDescuento);
    console.log('total a pagar:', totalPago);
    /* const fila = filaTabla(jSonObjetos)
        console.log(fila);
        $('#datosdetalle').DataTable().row.add($(fila)).draw(false); */
    const respuesta = await mantenimiento.agregarNuevoRegistro(`/admon/agregar-compras/${id}/`, jSonObjetos) 
    console.log('---------')
    console.log(respuesta)
    console.log(respuesta.condicion)
    console.log('---------') 
    if (respuesta.ok) {
        // mantenimiento.limpiarInputs('input_form') 
        const fila = filaTabla(respuesta.datos)
        $('#datosdetalle').DataTable().row.add($(fila)).draw(false);
        agregarFuncionBtnEliminar() 
        alertas.exelente(respuesta.mensaje)
    }
    else {
        alertas.error(respuesta.mensaje)
    } 


    




 }); 



 const convertirStrNumeric= (jSonObjetos)=>{
    jSonObjetos.fk_categoria=parseInt(jSonObjetos.fk_categoria)
    jSonObjetos.fk_marca=parseInt(jSonObjetos.fk_marca)
    jSonObjetos.fk_presentacion= parseInt(jSonObjetos.fk_presentacion)
    jSonObjetos.fk_unidad_medida=parseInt(jSonObjetos.fk_unidad_medida)
     jSonObjetos.tamanio = parseFloat(jSonObjetos.tamanio)
   jSonObjetos.estado=jSonObjetos.estado=='on'?true:false 
 }

 //ingreso dato 20
const operacionesAgregar=(datos)=>{
    totalDescuento += datos.descuentos
    totalSinDescuento += datos.cantidad_compra * datos.precio_unitario_compra
    totalPago = totalSinDescuento - totalDescuento
}

//
const operacionesQuitar=(datos)=>{
    totalDescuento -= datos.descuentos
    totalSinDescuento -= datos.cantidad_compra * datos.precio_unitario_compra
    totalPago = totalSinDescuento - totalDescuento
}

const filaTabla = (elementos) => {
    const estado = elementos.estado ? 'Activo' : 'Inactivo';   
    let datos = `
    <tr data-id="${elementos.id_detalle_compra}">
        <td>${elementos.no_lote}</td>
        <td>${elementos.no_lote}</td>
        <td>${elementos.fk_producto}</td>
        <td>Q${elementos.descuentos}</td>
        <td>${elementos.cantidad_compra}</td>
        <td>Q${elementos.precio_unitario_compra}</td>
        <td>Q${elementos.precio_sugerido_venta}</td>
        <td>Q${elementos.cantidad_compra * elementos.precio_unitario_compra - elementos.descuentos}</td>
        <td>
            ${crearBotonEliminar(elementos.id_detalle_compra,'btn-eliminar-producto')}
            <a class="btn btn-outline-info" href="/admon/detalles-usuario/${elementos.id_detalle_compra}">Detalles</a>
        </td> 
    </tr>
    `
    return datos
}
