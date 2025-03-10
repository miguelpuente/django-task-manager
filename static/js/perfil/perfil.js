document.addEventListener("DOMContentLoaded", () => {
    const uploadImage = document.getElementById("uploadImage");
    const userImage = document.getElementById("userImage");

    uploadImage.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                userImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

});
