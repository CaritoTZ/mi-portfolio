document.addEventListener("DOMContentLoaded", function () {
    function handleNavigation(event) {
        event.preventDefault();
        const url = this.getAttribute("href");

        fetch(url)
            .then(response => response.text())
            .then(html => {
                const newContent = new DOMParser().parseFromString(html, "text/html").querySelector(".container").innerHTML;
                document.querySelector(".container").innerHTML = newContent;
                history.pushState(null, "", url);
            })
            .catch(error => console.error("Error al cargar la página:", error));
    }

    // Manejar navegación de los enlaces del menú
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", handleNavigation);
    });

    // Manejar el botón "Saber más sobre mí"
    const btnLink = document.querySelector(".btn-link");
    if (btnLink) {
        btnLink.addEventListener("click", handleNavigation);
    }

    window.addEventListener("popstate", function () {
        location.reload(); // Maneja la navegación hacia atrás/adelante
    });
});
