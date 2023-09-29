import Mantenimineto from "./Crud.js";


class Utilidad {
    constructor() {

    }

    funcionamientoEliminar(claseBoton) {
        const botonesEliminar = document.querySelectorAll(claseBoton);

        botonesEliminar.forEach((boton) => {
            boton.addEventListener('click', function () {
                const idBotonEliminar = this.getAttribute('data-id');
                console.log(idBotonEliminar);
                this._accionEliminar(idBotonEliminar);
            });
        });

    }

    _accionEliminar(id) {
        alert(`el id es ${id}`)
    }


}


export default Utilidad