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

    // Si necesitas abrir el modal en una acción específica, puedes llamar a openPinModal() desde ahí
    // Ejemplo de uso: abrir el modal cuando se hace clic en un botón
    document.getElementById('openPinButton').onclick = function() {
        openPinModal();
    }