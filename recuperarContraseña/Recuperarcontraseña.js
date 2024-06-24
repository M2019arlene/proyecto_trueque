function validarcorreo(){
    const correo = document.getElementById("correo").value.trim();
    const errorcorreo = document.getElementById("error-correo");

     let valid = true;

     errorcorreo.innerHTML = "";

     if (correo === "") {
        errorcorreo.innerHTML = "Ingrese su correo electrónico.";
        valid = false;
    } else {
        const correoPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoPattern.test(correo)) {
            errorcorreo.innerHTML = "Correo electrónico no válido.";
            valid = false;
        }
    }

    return valid;

}