
//modal de pin de acceso a registro de nuevos usuarios
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

     /**limpiar los datos del form login */
     window.onload = function() {
        
        const messages = JSON.parse(document.getElementById('messages-data').textContent);
        const successMessage = messages.some(msg => msg[0] === 'success');
    
        if (successMessage) {
            document.getElementById('usuario').value = '';
            document.getElementById('password').value = '';
        }
    };


    /************ js para el formulario de final de el estado del registro *******/
   
    function abrirformulario(clienteId, estadoActual) {
       
        document.getElementById('cliente-id').value = clienteId;
        document.getElementById('estado').value = estadoActual;
    
        // Mostrar el modal
        document.getElementById('modal-overlay').style.display = 'block';
        document.getElementById('modal').style.display = 'block';
    }

    function cerrarModal() {
        document.getElementById('modal-overlay').style.display = 'none';  
        document.getElementById('modal').style.display = 'none';  
    }
    

    // Interceptar el envío del formulario con JavaScript (AJAX)
document.getElementById('form-estado').addEventListener('submit', async function(event) {
    event.preventDefault();  
    
    const formData = new FormData(this); 
    try {
        // Realizamos la solicitud AJAX usando fetch
        const respuesta = await fetch(this.action, {
            method: 'POST',
            body: formData
            
        });
        
        // Convertimos la respuesta en formato JSON
        const datos = await respuesta.json();

        if (respuesta.ok) {
            alert(datos.mensaje);
            cerrarModal();  
        } else {
           
            alert(datos.error || 'Hubo un problema al actualizar el estado.');
        }
    } catch (error) {
        console.error('Error al enviar la solicitud:', error);
        
    }
});





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
        }, 2000);
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
        },2000);
    });
});
