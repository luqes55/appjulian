
/**********************modal de pin de acceso a registro de nuevos usuarios*******/
    function openPinModal() {
        document.getElementById('pinModal').style.display = 'block';
    }

    document.getElementById('openModalLink').addEventListener('click', openPinModal);

    // Función para cerrar el modal
    function closePinModal() {
        document.getElementById('pinModal').style.display = 'none';
    }

    document.getElementById('closeModal').onclick = function(){
        closePinModal();
        
    }

     /*****************limpiar los datos del form login *****************/
     window.onload = function() {
        
        const messages = JSON.parse(document.getElementById('messages-data').textContent);
        const successMessage = messages.some(msg => msg[0] === 'success');
    
        if (successMessage) {
            document.getElementById('usuario').value = '';
            document.getElementById('password').value = '';
        }
    };


    /************ js para el formulario de final de el estado del registro *******/
   
    function abrirformulario(clienteId, estadoActual,idDispositivo) {
        if (estadoActual === "entregado") {
            // Si el estado es "Entregado", no mostrar el modal y mostrar una alerta
            alert('El estado ya está marcado como "Entregado" y no puede ser modificado.');
            return; // Detener la ejecución de la función
        }

        // Establecer el cliente-id y el estado actual en el formulario
        document.getElementById('cliente-id').value = clienteId;
        document.getElementById('estado').value = estadoActual;
        document.getElementById('idDispositivo').value = idDispositivo;
    
        // Obtener el campo de selección del estado
        const estadoSelect = document.getElementById('estado');
    
        
    
        // Mostrar el modal
        document.getElementById('modal-overlay').style.display = 'block';
        document.getElementById('modal').style.display = 'block';
    }
    
    function cerrarModa() {
        document.getElementById('modal-overlay').style.display = 'none';
        document.getElementById('modal').style.display = 'none';
    }
    
    // Evento para enviar el formulario cuando se presiona el botón de "Guardar"
    document.getElementById('form-estado').addEventListener('submit', async function(event) {
        event.preventDefault();  
        
        // Verificar si el estado es "Entregado" antes de enviarlo
        const estado = document.getElementById('estado').value;

    
        // Si el estado no es "Entregado", enviar la solicitud al servidor
        const formData = new FormData(this); 
        try {
            const respuesta = await fetch(this.action, {
                method: 'POST',
                body: formData
            });
            
            const datos = await respuesta.json();
    
            if (respuesta.ok) {
                alert(datos.mensaje);
                cerrarModa();  
            } else {
                alert(datos.error || 'Hubo un problema al actualizar el estado.');
            }
        } catch (error) {
            console.error('Error al enviar la solicitud:', error);
        }
    });
    


/*********************************** js para el loader de la app */


function showLoader(){
    document.getElementById('loader').style.display = 'flex';
}

function ocultarLoader(){
    document.getElementById('loader').style.display = 'none';
}

document.querySelectorAll('a').forEach(function(link){
    link.addEventListener('click', function(event){
        event.preventDefault();
        const href=link.getAttribute('href');
        console.log('loader activado');
        showLoader();

        setTimeout(() =>{
            window.location.href=href;
            ocultarLoader();
        }, 1200);
    });
});

window.addEventListener('beforeunload', function(){
    showLoader();
});


document.querySelectorAll('form').forEach(function(form){
    form.addEventListener('submit', function(event){
        event.preventDefault();
        showLoader();
        setTimeout(() =>{
            form.submit();
        },1200);
    });
});

/*********************************js para el reloj *****************/

function actualizarReloj() {
    console.log("Actualizando el reloj...");
    const fecha = new Date();
    let horas = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();

    
    horas = horas < 10 ? '0' + horas : horas;
    minutos = minutos < 10 ? '0' + minutos : minutos;
    segundos = segundos < 10 ? '0' + segundos : segundos;

    
    document.getElementById('reloj').textContent = `${horas}:${minutos}:${segundos}`;
}

setInterval(actualizarReloj, 1000);

actualizarReloj();


 // Captura el evento de navegación hacia atrás
 window.onpopstate = function(event) {
    // Redirige a la página de inicio
    window.location.href = '/';  // Cambia '/' a la URL de tu página de inicio
};

// Agrega un nuevo estado al historial para evitar que el usuario vuelva atrás
history.pushState(null, null, location.href);


/********* js para mostrar las paginas en inicio********* */
function ocultarVistas() {
    // Ocultar todas las vistas
    document.querySelectorAll('.view').forEach(vista => vista.style.display = 'none');
    // Quitar la clase activa de todos los botones
    document.querySelectorAll('.btn-toggle').forEach(boton => boton.classList.remove('active'));
}

function mostrarClientes() {
    ocultarVistas();
    document.getElementById('clientes-view').style.display = 'block';
    document.getElementById('clientes-btn').classList.add('active');
}

function mostrarDispositivos() {
    ocultarVistas();
    document.getElementById('dispositivos-view').style.display = 'block';
    document.getElementById('dispositivos-btn').classList.add('active');
}

function mostrarReporte() {
    ocultarVistas();
    document.getElementById('reporte-view').style.display = 'block';
    document.getElementById('reportes-btn').classList.add('active');
}

// Mostrar la vista de clientes por defecto
mostrarClientes();


//******************************** */ modal de la tabla info *************/

function abreModal() {

    document.getElementById('modal-info').style.display = 'block';
}

document.getElementById('abre').addEventListener('click', abreModal);

function cerrarModal() {
    document.getElementById('modal-info').style.display = 'none';
}

