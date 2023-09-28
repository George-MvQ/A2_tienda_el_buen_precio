class Mantenimineto {
    constructor() {

    }

    async obtenerDatos(url_obtener) {
        const datos = {
            respuesta: '',
            estado:true
        };
        try {
            const respuesta = await fetch(url_obtener)
            datos.respuesta = await respuesta.json()
        } catch (error) {
            console.error(error)
            datos.estado = false
        }
        return datos
    }

    async agregarDatos(url_obtener, formulario) {
        const datos = {
            respuesta: {},
            estado:true
        };

        try {
            const respuesta = await fetch(url_obtener, {
                method: 'POST',
                body: formulario,
                headers: { 'X-CSRFToken': this.getCookie('csrftoken') }
            })

            if (respuesta.ok) {
                datos.respuesta = await respuesta.json()
            }

        } catch (error) {
            console.error(error);
            datos.estado =false
        }
        return datos
    };



    
    async eliminarDato(url_elimnar, objetoId) {
        let datos = {
            mensaje: '',
            estado: true,
        }
        try {
            const eliminar = await fetch(url_elimnar, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json', //espesifica que se envian datos al servido en formato JSon 
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify(objetoId)
            })
            const mensaje = await eliminar.json();
            datos.mensaje = mensaje
            datos.estado = true
        } catch (error) {
            console.error(error)
            datos.estado = false
        }
    }

    async actualizarDato() {

    }


    getCookie(name) {
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


}

//exportar clase

export default Mantenimineto