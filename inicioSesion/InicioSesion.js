function validarFormulario() {
    const email = document.getElementById("email").value.trim();
    const errorEmail = document.getElementById("error-email");
    const password = document.getElementById("contraseña").value.trim();
    const errorContraseña = document.getElementById("error-contraseña");

    let valid = true;

    // Limpiar mensajes de error previos
    errorEmail.innerHTML = "";
    errorContraseña.innerHTML = "";

    // Verificar si el campo de correo electrónico está vacío
    if (email === "") {
        errorEmail.innerHTML = "ingrese su correo electrónico.";
        valid = false;
    } else {
        // Verificar el formato del correo electrónico utilizando una expresión regular
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            errorEmail.innerHTML = "Correo electrónico no válido.";
            valid = false;
        }
    }

    // Verificar si el campo de contraseña está vacío
    if (password === "") {
        errorContraseña.innerHTML = "ingrese su contraseña.";
        valid = false;
    } else {
        // Verificar si la contraseña cumple con los criterios requeridos
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
            errorContraseña.innerHTML = "La contraseña no cumple con los siguientes criterios:<br>" + errorMessages.join("<br>");
            valid = false;
        }
    }

    return valid;
}