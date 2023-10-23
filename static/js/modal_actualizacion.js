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
    const table = document.getElementById("datoscategoria");
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

