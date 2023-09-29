/*
let editor = new DataTable.Editor({
    ajax: '/obtener_usuario/',
    fields: [
        {
            label: 'Password:',
            name: 'password'
        },
        {
            label: 'Last login:',
            name: 'last_log'
        },
        {
            label: 'Superuser:',
            name: 'is_superuser'
        },
        {
            label: 'Username:',
            name: 'username'
        },
        {
            label: 'First Name:',
            name: 'first_name'
        },
        {
            label: 'Last name:',
            name: 'last_name'
        },
        {
            label: 'Email:',
            name: 'email'
        },
        {
            label: 'Is Staff:',
            name: 'is_staff'
        },
        {
            label: 'Is Active:',
            name: 'is_active',
            type: 'options'
        },
        {
            label: 'Date joined:',
            name: 'date_joined',
            type: 'datetime'
        },

    ],
    table: '#example'
});
 
let table = $('#example').DataTable({
    ajax: '/obtener_usuario/',
    columns: [
        {
            usuario: null,
            render: function (usuario, type, row) {
                // Combine the first and last names into a single table field
                return  usuario.id +' '+ usuario.password +' '+ usuario.last_login +' '+ usuario.is_superuser +' '+ usuario.username+' '+  usuario.first_name + ' ' + usuario.last_name +' '+ usuario.email +' '+ usuario.is_staff +' '+ usuario.is_active +' '+ usuario.date_joined;
            }
        },
        { data: 'id' },
        { data: 'password' },
        { data: 'last_login' },
        { data: 'is_superuser' },
        { data: 'username' },
        { data: 'first_name' },
        { data: 'last_name' },
        { data: 'email' },
        { data: 'is_staff' },
        { data: 'is_active' },
        { data: 'date_joined' }
    ],
    lengthChange: false,
    select: true
});
 
// Display the buttons
new DataTable.Buttons(table, [
    { extend: 'create', editor: editor },
    { extend: 'edit', editor: editor },
    { extend: 'remove', editor: editor }
]);
 
table.buttons().container().appendTo($('.col-md-6:eq(0)', table.table().container()));

*/

/* ---------------------------------------------------------------------------------------------------- */


/* ejemplo geroge */

// ESTO NOS FUNCIONO
/*
let datosTabla;
let datosTablaInicializados = false

const opcionesTabla = {
    pageLength: 3, //nombre por defecto (cantidad de filas en cada tabla)
    destroy: true, //indicando que sea una tabla destruible
    lengthMenu:[3,5,10,15], //para el menuto de contenido de la tabla 
    columnDefs: [{
        className: 'text-white text-center',
        targets: [0, 1, 2, 3]//columnas inicia del 0 a n de las que se aplican los cabios
    },{
        orderable:false, 
        targets:[3]
    },{//buscando en columnas en espesifico
        searchable: false,
        targets:[1]
    },// {width: '50%',targets:[0]} para el ancho entre columnas 

    ],
    scrollX: '200px'


}




const iniciarDatosTabla = async () => {
    if (datosTablaInicializados) [
        datosTabla.destroy()
    ]
    await listarusuario()
    datosTabla = $('#datosusuario').DataTable(opcionesTabla)
    datosTablaInicializados = true

}
window.addEventListener('load', async () => {
    await cargaInicial();
});

const cargaInicial = async () => {
    await iniciarDatosTabla()
};
*/
/*

const listarusuario = async () => {
    try {
        const respuesta = await fetch('/obtener_usuario/');
        const datos = await respuesta.json();

        let contenido = '';
        console.log(datos);
        datos.usuarios.forEach((element) => {
            contenido += `
                <tr>
                    
                    <td >${element.id}</td>
                    <td >${element.password}</td>
                    <td >${element.last_login}</td>
                    <td >${element.is_superuser}</td>
                    <td >${element.username}</td>
                    <td >${element.first_name}</td>
                    <td >${element.last_name}</td>
                    <td >${element.email}</td>
                    <td >${element.is_staff}</td>
                    <td >${element.is_active}</td>
                    <td >${element.date_joined}</td> 
                    <td>
                        <button class="btn btn-primary" data-toggle="modal" data-target="#editarUsuarioModal" data-id="${element.id}">Editar</button>
                        <button class="btn btn-danger" data-toggle="modal" data-target="#eliminarUsuarioModal" data-id="${element.id}">Eliminar</button>
                    </td>
                </tr>
            `;
        });
        tablaBody.innerHTML = contenido;
        mensajemarca.innerHTML = datos.mensaje;
    } catch (error) {
        console.error(error);
        mensajemarca.innerHTML = 'Error al cargar los usuarios';
    }
};

*/



/* COMENTADO  */

/* 
//funciones para desplegar formulario
let formInicializado = false
btnAgregarMarca.addEventListener('click',()=>{
    if (formInicializado){
        div_form_marca.style.display = 'none'
        formInicializado = false
    }
    else{
        div_form_marca.style.display = 'block'
        formInicializado = true
    }
})


//funciones para guardar datos 
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
btGuardarMarca.addEventListener('click', async () => {
    let formAgregar = new FormData(form_agregar_marca);

    try {
        const response = await fetch('/ingresomarcas/', {
            method: 'POST',
            body: formAgregar,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        });

        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        

        // Maneja la respuesta de la vista aquí
        alert(data.message); // Muestra un mensaje de éxito
        await iniciarDatosTabla()
        // Puedes realizar otras acciones como limpiar el formulario o actualizar la interfaz de usuario
    } catch (error) {
        // Maneja errores si es necesario
        console.error('Error:', error);

    }
});

const agregarDatosATabla = (nuevoDato) => {
    const fila = `
        <tr>
            <td>${nuevoDato.id_marcas}</td>
            <td>${nuevoDato.nombre_marca}</td>
            <td>${nuevoDato.descripcion}</td>
            <td>${nuevoDato.estado}</td>
        </tr>
    `;
    // Agregar la fila a la tabla
    $('#datosmarca').DataTable().row.add($(fila)).draw(false);
};
 */

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


window.addEventListener('load', () => {
    $('#datosusuario').DataTable(opcionesTabla);
    agregarFuncionBtnEliminar();
    agregarFuncionBtnActualizar();
});

const agregarFuncionBtnEliminar = () => {
    const botonesEliminar = document.querySelectorAll('.btn-eliminar-usuario');

    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', function () {
            const idMarcaAEliminar = this.getAttribute('data-id');
            console.log(idMarcaAEliminar);
            eliminarUsuario(idMarcaAEliminar);
        });
    });
};

const agregarFuncionBtnActualizar = () => {
    const botonesEliminar = document.querySelectorAll('.btn-detalles-usuario');

    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', function () {
            const idMarcaAEliminar = this.getAttribute('data-id');
            console.log(idMarcaAEliminar);
            detallesUsuario(idMarcaAEliminar);
        });
    });
};

//funcion eliminar 
const eliminarUsuario= (id)=>{
    alert(`el id es ${id}`)
}

//funcion detalle de usuario 
const detallesUsuario= (id)=>{
    alert(`el id es de detalle es ${id}`)
}
