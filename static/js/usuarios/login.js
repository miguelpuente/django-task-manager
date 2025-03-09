document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.querySelector(".sign-in-htm");
    const formRegister = document.querySelector(".sign-up-htm");

    // Validación del formulario de registro
    formRegister.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío si hay errores

        const username = document.getElementById("signup-user").value.trim();
        const email = document.getElementById("signup-email").value.trim();
        const password1 = document.getElementById("signup-pass").value;
        const password2 = document.getElementById("signup-repeat-pass").value;

        if (!validarEmail(email)) {
            mostrarError("signup-email", "El correo electrónico no es válido.");
            return;
        }

        if (password1.length < 6) {
            mostrarError("signup-pass", "La contraseña debe tener al menos 6 caracteres.");
            return;
        }

        if (password1 !== password2) {
            mostrarError("signup-repeat-pass", "Las contraseñas no coinciden.");
            return;
        }

        formRegister.submit(); // Si todo está correcto, envía el formulario
    });

    // Validación del formulario de login
    formLogin.addEventListener("submit", function (event) {
        const username = document.getElementById("login-user").value.trim();
        const password = document.getElementById("login-pass").value.trim();

        if (username === "" || password === "") {
            event.preventDefault();
            alert("Por favor, completa todos los campos.");
        }
    });

    // Función para validar formato de email
    function validarEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Función para mostrar mensajes de error
    function mostrarError(inputId, mensaje) {
        const input = document.getElementById(inputId);
        const error = document.createElement("div");
        error.className = "error-message";
        error.textContent = mensaje;

        eliminarErrores(input); // Limpia errores previos
        input.classList.add("input-error");
        input.parentNode.appendChild(error);

        setTimeout(() => {
            eliminarErrores(input);
        }, 5000); // Borra el mensaje después de 5 segundos
    }

    // Función para eliminar mensajes de error previos
    function eliminarErrores(input) {
        input.classList.remove("input-error");
        const error = input.parentNode.querySelector(".error-message");
        if (error) error.remove();
    }
});
