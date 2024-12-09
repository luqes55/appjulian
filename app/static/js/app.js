
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
        }, 2000);
    });
});

document.querySelectorAll('button').forEach(function(link){
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

window.addEventListener('beforeunload', function(){
    showLoader();
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

    setTimeout(()=>{
        document.getElementById('clientes-view').style.display='block';
    },50);
}

function mostrarPendientes() {
    document.getElementById('clientes-view').style.display = 'none';
    document.getElementById('pendientes-view').style.display = 'block';
}




// Mostrar la vista de clientes por defecto
mostrarClientes();


//******************************** */ modal de la tabla info *************/


  
  function cerrarmodal() {
    document.getElementById('info-all').style.display = 'none';
   
  }
  function abremodal(idCliente) {
    fetch(`/get_cliente_info/${idCliente}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                // Actualiza la sección del cliente
                if (data.cliente) {
                    let clienteHTML = `
                        <h4>Cliente</h4>
                        <table>
                            <thead>
                                <tr>
                                    <th>ID Cliente</th>
                                    <th>Nombre</th>
                                    <th>Apellidos</th>
                                    <th>NIT</th>
                                    <th>Correo</th>
                                    <th>Dirección</th>
                                    <th>Teléfono</th>
                                    <th>fecha de ingreso</th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>${data.cliente.idCliente}</td>
                                    <td>${data.cliente.nombre}</td>
                                    <td>${data.cliente.apellidos}</td>
                                    <td>${data.cliente.nit}</td>
                                    <td>${data.cliente.correo}</td>
                                    <td>${data.cliente.direccion}</td>
                                    <td>${data.cliente.telefono}</td>
                                    <td>${data.cliente.fechaIngreso}</td>
                                    
                                    
                                </tr>
                            </tbody>
                        </table>
                    `;
                    document.getElementById('cliente-info').innerHTML = clienteHTML;
            } else {
    document.getElementById('cliente-info').innerHTML = '<h4>Cliente</h4><p>No se encontró información del cliente.</p>';
}
                // Actualiza la sección de dispositivos
                if (data.dispositivos.length > 0) {
                    let dispositivosHTML = `
                        <h4>Dispositivos</h4>
                        <table>
                            <thead>
                                <tr>
                                    <th>ID Cliente</th>
                                    <th>ID Dispositivo</th>
                                    <th>Marca</th>
                                    <th>Modelo</th>
                                    <th>IMEI</th>
                                    <th>color</th>
                                    <th>abono</th>
                                    <th>detalles</th>
                                    
                                    
                                </tr>
                            </thead>
                            <tbody>
                    `;
                    data.dispositivos.forEach(dispositivo => {
                        dispositivosHTML += `
                            <tr>
                            <td> ${dispositivo.idCliente}</td>
                                <td>${dispositivo.idDispositivo}</td>
                                <td>${dispositivo.marca}</td>
                                <td>${dispositivo.modelo}</td>
                                <td>${dispositivo.Imei}</td>
                                <td>${dispositivo.color}</td>
                                <td>$ ${dispositivo.abono}</td>
                                <td>${dispositivo.detalles}</td>
                                
                                
                                
                            </tr>
                        `;
                    });
                    dispositivosHTML += '</tbody></table>';
                    document.getElementById('dispositivo-info').innerHTML = dispositivosHTML;
                } else {
                    document.getElementById('dispositivo-info').innerHTML = '<h4>Dispositivos</h4><p>No hay dispositivos registrados.</p>';
                }

                // Actualiza la sección de reportes
                if (data.reportes.length > 0) {
                    let reportesHTML = `
                        <h4>Reporte Final</h4>
                        <table>
                            <thead>
                                <tr>
                                    <th>ID Reporte</th>
                                    <th>ID Dispositivo</th>
                                    <th>Técnico Encargado</th>
                                    <th>Proveedor Repuesto</th>
                                    <th>Nombre Repuesto</th>
                                    <th>Fecha Entrega</th>
                                    <th>Valor Repuesto</th>
                                    <th>Total</th>
                                </tr>
                            </thead>
                            <tbody>
                    `;
                    data.reportes.forEach(reporte => {
                        reportesHTML += `
                            <tr>
                                <td>${reporte.idReporte}</td>
                                <td>${reporte.idDispositivo}</td>
                                <td>${reporte.tec_arregla}</td>
                                <td>${reporte.provedorRepuesto}</td>
                                <td>${reporte.nombreRepuesto}</td>
                                <td>${reporte.fechaEntrega}</td>
                                <td>${reporte.valorRepuesto}</td>
                                <td>${reporte.valorArreglo}</td>
                            </tr>
                        `;
                    });
                    reportesHTML += '</tbody></table>';
                    document.getElementById('reporte-info').innerHTML = reportesHTML;
                } else {
                    document.getElementById('reporte-info').innerHTML = '<h4>Reporte Final</h4>';
                }
            }

            // Muestra el modal
            document.getElementById('info-all').style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
}


function actualizarEstado(idCliente) {
    fetch(`/actualizar_estado/${idCliente}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            // Actualiza la interfaz para quitar el cliente de pendientes
            location.reload();  // Recarga la página para reflejar los cambios
        } else {
            alert('Error al actualizar el estado');
        }
    })
    .catch(error => console.error('Error:', error));
}
