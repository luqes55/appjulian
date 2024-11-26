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


    /*******************************js para el formulario de final de el estado del registro **************************/
    
    function abrirform(clienteId, estadoActual){
        document.getElementById('estado_id').value= clienteId;
        document.getElementById('estado').value= estadoActual;

        document.getElementById('modal').style.display='block';
        ducument.getElementById('modal-overlay').style.display='block';
        
    }

    function cerrarformulario(){
        ducument.getElementById('modal').style.display='none';
        document.getElementById('modal-overlay').style.display='none';
    }

    document.getElementById('form-estado').addEventListener('submit', async(event) =>{
        event.preventDefault();


        const formdata= new FormData(event.target);
        const respuesta= await fetch(event.target.action,{
            method: 'POST',
            body: formdata
        });

        if (respuesta.ok){
            const datos= await respuesta.json();
            alert('estado actualizado exitosamente');

            const estado = FormData.get('estado_id');
            const nuevoEstado = formdata.get('estado');
            const estadoSpan = document.querySelector(`span[onclick="abrirform(${estadoId},'${nuevoEstado}')"]`);
            if(estadoSpan){
                estadoSpan.textContent= nuevoEstado;
                estadoSpan.className= `estado ${nuevoEstado}`;
            }

            cerrarformulario();
        }else{
            alert('error al actualizar el estado')
        }
    });
