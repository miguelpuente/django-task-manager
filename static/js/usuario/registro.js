// Script de validación del formulario si se necesita
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.register-form');
    
    form.addEventListener('submit', function (event) {
        const formElements = form.elements;
        let valid = true;

        // Validación de los campos de entrada
        for (let i = 0; i < formElements.length; i++) {
            if (formElements[i].type !== 'submit' && formElements[i].value.trim() === '') {
                valid = false;
                formElements[i].style.borderColor = 'red';
            } else {
                formElements[i].style.borderColor = '#ccc';
            }
        }

        if (!valid) {
            event.preventDefault();
            alert("Por favor, completa todos los campos.");
        }
    });
});
