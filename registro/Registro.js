function validarRegistro() {
    const nombre = document.getElementById("nombre").value.trim();
    const errorNombre = document.getElementById("error-nombre");
    const apellido = document.getElementById("apellido").value.trim();
    const errorApellido = document.getElementById("error-apellido");
    const correo = document.getElementById("correo").value.trim();
    const errorCorreo = document.getElementById("error-correo");
    const password = document.getElementById("password").value.trim();
    const errorPassword = document.getElementById("error-password");
    const passwordConfirmation = document.getElementById("password-confirmation").value.trim();
    const errorPasswordConfirmation = document.getElementById("error-password-confirmation");

    let valid = true;

    // Limpiar mensajes de error
    errorNombre.innerHTML = "";
    errorApellido.innerHTML = "";
    errorCorreo.innerHTML = "";
    errorPassword.innerHTML = "";
    errorPasswordConfirmation.innerHTML = "";

    // Validación del nombre
    if (nombre === "") {
        errorNombre.innerHTML = "Ingrese su nombre.";
        valid = false;
    } else {
        const nombrePattern = /^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{2,20}$/;
        if (!nombrePattern.test(nombre)) {
            errorNombre.innerHTML = "Nombre no válido. Use solo letras, espacios, apóstrofes y guiones.";
            valid = false;
        }
    }

    // Validación del apellido
    if (apellido === "") {
        errorApellido.innerHTML = "Ingrese su apellido.";
        valid = false;
    } else {
        const apellidoPattern = /^[A-Za-zÀ-ÖØ-öø-ÿ\s'-]{2,30}$/;
        if (!apellidoPattern.test(apellido)) {
            errorApellido.innerHTML = "Apellido no válido. Use solo letras, espacios, apóstrofes y guiones.";
            valid = false;
        }
    }

    // Validación del correo
    if (correo === "") {
        errorCorreo.innerHTML = "Ingrese su correo electrónico.";
        valid = false;
    } else {
        const correoPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoPattern.test(correo)) {
            errorCorreo.innerHTML = "Correo electrónico no válido.";
            valid = false;
        }
    }

    // Validación de la contraseña
    if (password === "") {
        errorPassword.innerHTML = "Ingrese su contraseña.";
        valid = false;
    } else {
        let errorMessages = [];
        if (!/(?=.*[a-z])/.test(password)) {
            errorMessages.push("Debe contener al menos una letra minúscula.");
        }
        if (!/(?=.*[A-Z])/.test(password)) {
            errorMessages.push("Debe contener al menos una letra mayúscula.");
        }
        if (!/(?=.*\d)/.test(password)) {
            errorMessages.push("Debe contener al menos un dígito.");
        }
        if (!/.{8,}/.test(password)) {
            errorMessages.push("Debe tener al menos 8 caracteres.");
        }
        if (errorMessages.length > 0) {
            errorPassword.innerHTML = "La contraseña no cumple con los siguientes criterios:<br>" + errorMessages.join("<br>");
            valid = false;
        }
    }

    // Validación de la confirmación de la contraseña
    if (passwordConfirmation === "") {
        errorPasswordConfirmation.innerHTML = "Confirme su contraseña.";
        valid = false;
    } else if (password !== passwordConfirmation) {
        errorPasswordConfirmation.innerHTML = "Las contraseñas no coinciden.";
        valid = false;
    }

    if (valid === true) {
        Swal.fire({
            position: "top-center",
            icon: "success",
            title: "Te registraste con éxito",
            showConfirmButton: false,
            timer: 1500
        });
    }

  return valid;

}