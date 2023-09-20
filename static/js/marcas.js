console.log('Buena Abi de Ines');


window.addEventListener('load', async () => {
    await cargaInicial();
})


const cargaInicial = async () => {
    await listarMarcas()
}

const listarMarcas = async () => {
    try {
        const repuesta = await fetch('/obtener_marcas')
        const datos = await repuesta.json()

        let contenido = ``
        console.log(datos);
        datos.marcas.forEach((element) => {
            contenido += `
        <tr>
            <td> ${element.id_marcas}</td>
            <td> ${element.nombre_marca}</td>
            <td> ${element.estado}</td>
            <td> ${element.descripcion}</td>
        </tr>
        `
        });
        tablaBody.innerHTML = contenido
        mensajemarca.innerHTML = datos.mensaje

    }
    catch (error) {
        console.log(error);
    }
}


$(document).ready( function () {
    $('#datosmarca').DataTable();
});
