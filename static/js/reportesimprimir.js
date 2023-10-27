

  //botn para imprimier 
  btn_imprimir.addEventListener("click", ()=>{
    //---codigo aqui 
    console.log("Este el boton imprimir");
   // let urlReporte = btn_imprimir.getAttribute("href");
    const url = btn_imprimir.getAttribute("data-url");
    // Abre una ventana emergente con la URL del reporte
    const popup = window.open(url, "_blank", "width=1000,height=600");

    let ventanaPrevia = window.open(url, "_blank");
    if (!popup) {
      alert("El navegador bloqueó la pestaña flotante.");
    }

    

    // Espera a que la ventana previa se cargue antes de imprimir o guardar como PDF
      ventanaPrevia.onload = function() {
  
    
    };    
    
  
    
  
  })


  // Obtener la fecha actual
let fechaActual = new Date();

// Obtener el elemento <span> por su ID
let fechaSpan = document.getElementById("fechaSpan");

// Establecer el contenido del <span> como la fecha actual
fechaSpan.textContent = fechaActual;
