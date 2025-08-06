document.addEventListener("DOMContentLoaded", function() {
    const messageBox = document.getElementById("message-box");
    if (messageBox) {
        // Show the message
        messageBox.classList.add("show");

        // Scroll to top after 2 seconds
        setTimeout(() => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        }, 2000);

        // Hide after 4 seconds
        setTimeout(() => {
            messageBox.classList.remove("show");
        }, 4000);
    }
});