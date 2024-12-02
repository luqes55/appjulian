function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    var apellidos = document.getElementById("apellidos").value;
    var nit = document.getElementById("nit").value;
    var correo = document.getElementById("correo").value;
    var telefono = document.getElementById("telefono").value;
    var Imei = document.getElementById("Imei").value;
    var abono = document.getElementById("abono").value;

    // Validación del nombre
    if (nombre.trim() == "") {
        alert("El campo Nombre no puede estar vacío.");
        return false;
    }

    // Validación de apellidos
    if (apellidos.trim() == "") {
        alert("El campo Apellidos no puede estar vacío.");
        return false;
    }

    // Validación de NIT (debe ser un número positivo)
    if (nit.trim() == "" || isNaN(nit) || nit <= 0) {
        alert("El campo NIT debe ser un número válido.");
        return false;
    }

    // Validación del correo (formato correcto)
    var correoRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!correoRegex.test(correo)) {
        alert("Por favor ingrese un correo electrónico válido.");
        return false;
    }

    // Validación del teléfono (debe ser un número positivo)
    if (telefono.trim() == "" || isNaN(telefono) || telefono <= 0) {
        alert("El campo Teléfono debe ser un número válido.");
        return false;
    }

    // Validación de IMEI (debe ser un número de 15 dígitos)
    if (Imei.trim() == "" || isNaN(Imei) || Imei.length != 15) {
        alert("El IMEI debe ser un número de 15 dígitos.");
        return false;
    }

    // Validación de abono (debe ser un número positivo)
    if (abono.trim() == "" || isNaN(abono) || abono <= 0) {
        alert("El campo Abono debe ser un número mayor a 0.");
        return false;
    }

    // Si pasa todas las validaciones, el formulario se enviará
    return true;
}
