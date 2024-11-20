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