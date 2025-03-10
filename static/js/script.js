document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const sidebar = document.querySelector(".sidebar");
    const userMenu = document.querySelector(".user-menu");

    // Botón de menú lateral (móviles)
    menuToggle.addEventListener("click", () => {
        sidebar.classList.toggle("active");
    });

    // Mostrar/Ocultar dropdown del usuario
    userMenu.addEventListener("click", () => {
        userMenu.classList.toggle("active");
    });

    // Cerrar menús al hacer clic fuera
    document.addEventListener("click", (event) => {
        if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
            sidebar.classList.remove("active");
        }

        if (!userMenu.contains(event.target)) {
            userMenu.classList.remove("active");
        }
    });
});