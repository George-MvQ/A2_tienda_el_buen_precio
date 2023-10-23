import {Mantenimiento, AlertasBotones,crearBotonEliminar } from "./Crud.js";


const mantenimiento = new Mantenimiento()
const alertas = new AlertasBotones() 


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
    pageLength: 7, //nombre por defecto (cantidad de filas en cada tabla)
    destroy: true, //indicando que sea una tabla destruible
    lengthMenu: [3, 5, 7,10, 15], //para el menuto de contenido de la tabla 
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


window.addEventListener('load', () => {
    agregarFuncionBtnEliminar()
    agregarFuncionBtnActualizar()
    $('#datosmarca').DataTable(opcionesTabla);
});

const agregarFuncionBtnEliminar = () => {
    const botonesEliminar = document.querySelectorAll('.btn-eliminar-marca');
    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', function () {
            const identificador = this.getAttribute('data-id');
            //print(form_agregar_marca)
            alertas.eliminar(identificador, eliminarMarcas)
            console.log(identificador);
            
        });
    });
};

//funcion eliminar 
const eliminarMarcas = async (id) => {
    const respuesta = await mantenimiento.eliminarDato('/admon/ingreso-marcas/', id)
    if (respuesta.condicion === 'ok') {
        mantenimiento.eliminarFilaTabla(id, 'datosmarca')
    }
    return respuesta
}

/*  AGREGAR DATOS  */
btGuardarMarca.addEventListener('click', async (e) => {
    e.preventDefault()
    let formAgregar = new FormData(form_agregar_marca);//pasamos como parametro el id del formulario que queremos 

    const jSonObjetos = mantenimiento.formulariosAObjeto(formAgregar)
    console.log(jSonObjetos);
    const respuesta = await mantenimiento.agregarNuevoRegistro('/admon/ingreso-marcas/', jSonObjetos)
    console.log('---------')
    console.log(respuesta)
    console.log(respuesta.condicion)
    console.log('---------')
    if (respuesta.condicion === 'ok') {
        // mantenimiento.limpiarInputs('input_form')

        const fila = filaTabla(respuesta.datos)
        console.log(fila)
        $('#datosmarca').DataTable().row.add($(fila)).draw(false);
        agregarFuncionBtnEliminar()

        alertas.exelente(respuesta.mensaje)
    }
    else {
        alertas.error(respuesta.mensaje)
    }

});

const filaTabla = (elementos) => {
    const estado = elementos.estado ? 'Activo' : 'Inactivo';
    let datos = `
    <tr data-id="${elementos.id_marcas}">
        <td>${elementos.id_marcas}</td>
        <td  >${elementos.nombre_marca}</td>
        <td>${elementos.descripcion}</td>
        <td>${estado}</td>
        <td>
            ${crearBotonEliminar(elementos.id_marcas, 'btn-eliminar-marca')}
            <a class="btn btn-outline-info" href="/admon/detalles-usuario/${elementos.id}/">Actualizar</a>
        </td> 
    </tr>
    `
    return datos
}

/*
    ----------------ACTUALIZAR----------------
*/

// -----------------FUNCIONES PARA ACTUALIZAR

//funcion que agregar el funcionamiento al boton actualizar 
const agregarFuncionBtnActualizar = () => {
    const btn_form_actualizar = document.querySelectorAll('.btn-formActualizar');
    btn_form_actualizar.forEach((boton) => {
        boton.addEventListener('click', function () {
            const identificador = this.getAttribute('data-id');
            agregarDatosForm(identificador)
            console.log(identificador);
        });
    });
};

//esta funcion se encarga de obtener y agregar los datos de la fila al formulario 
const agregarDatosForm = (id) => {
    const filas = obtenerFila(id)
    frm_nom_categoria.value =  filas[1].textContent
    frm_desc.value = filas[2].textContent
    frm_estado.value = filas[3].textContent
    btn_actualizar.setAttribute('data-id', parseInt(id))
}

//esta funcion s encarga de obtener una fila en espesifico 
const obtenerFila = (id) => {
    console.log(id);
    const table = document.getElementById("datosmarca");
    // Encuentra la fila por su data-id
    const fila = table.querySelector(`tr[data-id="${id}"]`);
    if (fila) {
        const celdas = fila.cells;
        return celdas
    } else {
        console.log("No se encontró una fila con data-id '" + dataId + "'.");
        return null
    }
}

// esta funcion es la que se encarga de actualizar datos 
btn_actualizar.addEventListener('click',async ()=>{
    const datos = obetenerDatosForm()
    alertas.actualizar(datos,actualizarRegistro)
});

const actualizarRegistro = async(datos)=>{
    const respuesta = await mantenimiento.actualizarRegistroCompleto('/admon/categorias/', datos)
    if (respuesta.condicion === 'ok'){
        console.log('----respuesat del servidor----');
        console.log(respuesta.datos);
        actualizarFila(respuesta.datos);
    }
    return respuesta
}

//esta funcion obtiene todo los datos de la fila a actualizar 
const obetenerDatosForm = ()=>{
    const id = btn_actualizar.getAttribute('data-id')
    let formActualizar = new FormData(form_actualizar);
    const jSonObjetos = mantenimiento.formulariosAObjeto(formActualizar)
    jSonObjetos.estado = jSonObjetos.estado ==='Activo'
    jSonObjetos.identificador = parseInt(id)
    return jSonObjetos
}

//este apartado actualiza las filas con los nuevos datos 
const actualizarFila = (nuevosDatos) => {
    const fila = obtenerFila(nuevosDatos.id_categoria);
    fila[1].textContent = nuevosDatos.nombre_categoria;
    fila[2].textContent = nuevosDatos.descripcion;
    fila[3].textContent = nuevosDatos.estado;
}





















/*
const iniciarDatosTabla = async () => {
    if (datosTablaInicializados) [
        datosTabla.destroy()
    ]
    await listarMarcas()
    datosTabla = $('#datosmarca').DataTable(opcionesTabla)
    datosTablaInicializados = true
}


//cones esta funcion nosotros agregamos filas a la tabla. 
const filaTabla = (elementos) => {
    const estado = elementos.estado ? 'Activo' : 'Inactivo';   
    let datos = `
    <tr data-id="${elementos.id_marcas}">
        <td  >${elementos.id_marcas}</td>
        <td>${elementos.nombre_marca}</td>
        <td>${elementos.descripcion}</td>
        <td>${estado}</td>
        <td class = '' >${crearBotonEliminar(elementos.id_marcas)}</td> 
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
     // Obtenemos una referencia al campo de nombre de marca
     const inNombre = document.getElementById('in_nombre');
    
     // Verificamos si el campo de nombre de marca está vacío
     if (inNombre.value.trim() === '') {
         Swal.fire('El campo Nombre de Marca es obligatorio. Por favor, ingresa un nombre de marca.');
         return; // No enviamos el formulario si hay errores
     }
    let formAgregar = new FormData(form_agregar_marca);
    const datos = await mantenimiento.agregarDatos('/admon/ingreso-marcas/', formAgregar)
    if (datos.respuesta.condicion==='ok') {
        in_nombre.value = ""
        in_descripcion.value = ""
        const fila = filaTabla(datos.respuesta)
        $('#datosmarca').DataTable().row.add($(fila)).draw(false);
        agregarBotonEliminar()
        Swal.fire(
            datos.respuesta.mensaje,
            'Preciona clic en el boton!',
            'success'       
        )
    }
    else {
        Swal.fire(
            datos.respuesta.mensaje,
            'Datos no guardados, Preciona clic en el boton!',
            'warning'
        )
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
        const eliminar = await fetch('', {
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


*/