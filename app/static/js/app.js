function cancelarRegistro() {
    if (confirm("¿Estás seguro de que deseas cancelar el registro? Todos los datos se perderán.")) {
        // Limpiar los campos del formulario
        document.querySelector('form').reset();
        // Redirigir a la página principal
        window.location.href = "/inicio";
    }
}


    // Función para abrir el modal
    function openPinModal() {
        document.getElementById('pinModal').style.display = 'block';
    }

    // Función para cerrar el modal
    function closePinModal() {
        document.getElementById('pinModal').style.display = 'none';
    }

    // Agregar un evento para el botón de cancelar
    document.getElementById('closeModal').onclick = function() {
        closePinModal();
    }

    // abrir el modal cuando se hace clic en un botón
    document.getElementById('openPinButton').onclick = function() {
        openPinModal();
    }

     // Limpiar los campos del formulario  si hay un mensaje de éxito de session iniciada}
     window.onload = function() {
        // Obtenemos los mensajes flash del backend
        const messages = JSON.parse(document.getElementById('messages-data').textContent);
        const successMessage = messages.some(msg => msg[0] === 'success');
    
        if (successMessage) {
            document.getElementById('usuario').value = '';
            document.getElementById('password').value = '';
        }
    };



    //aqui el js para el dropdown de el perfil

    document.getElementById('profileImg').addEventListener('click', ()=>{
        const dropdownMenu=document.getElementById('dropdownMenu');
        if (dropdownMenu.style.left=== 'opx'){
            dropdownMenu.style.left= '-250px';
            }else{
                dropdownMenu.style.left='0px';
            }
    })


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
        alert('Ocurrió un error inesperado.');
    }
});
