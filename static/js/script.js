// Obtener referencias a los elementos del DOM
const unlockLink = document.getElementById('unlock-link');
const gifContainer = document.getElementById('gif-container');
const secondGifContainer = document.getElementById('second-gif-container');
const unlockedCouponContainer = document.getElementById('unlocked-coupon-container');
const couponCode = document.getElementById('coupon-code');
const couponDescription = document.getElementById('coupon-description');


unlockLink.addEventListener('click', async (event) => {
    event.preventDefault(); // Evitar que el enlace recargue la página

    // Ocultar el GIF inicial y mostrar el segundo GIF
    gifContainer.classList.add('hidden');
    secondGifContainer.classList.remove('hidden');

    // Esperar 2 segundos
    await new Promise(resolve => setTimeout(resolve, 1700));

    // Obtener el cupón del día
    const today = new Date().toISOString().split('T')[0]; // Formato YYYY-MM-DD
    const response = await fetch(`/unlock/${today}`);
    if (response.ok) {
        const coupon = await response.json();

        // Mostrar el cupón desbloqueado
        couponCode.textContent = coupon.code;
        couponDescription.textContent = coupon.description;
        secondGifContainer.classList.add('hidden');
        unlockedCouponContainer.classList.remove('hidden');
    } else {
        alert("Error al desbloquear el cupón.");
    }

    
});

// function shareOnWhatsApp() {
//     const couponCode = document.getElementById('coupon-code').textContent;
//     const couponDescription = document.getElementById('coupon-description').textContent;
//     const phoneNumber = "123456789";  // Reemplaza con el número de teléfono deseado
//     const message = `¡He canjeado mi cupón! Código: ${couponCode}, Descripción: ${couponDescription}`;
//     const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
//     window.open(url, '_blank');
// }

// function shareOnWhatsApp() {
//     const couponCode = document.getElementById('coupon-code').textContent;
//     const couponDescription = document.getElementById('coupon-description').textContent;
//     const phoneNumber = "609512301";  // Reemplaza con el número de teléfono deseado
//     const message = `¡He canjeado mi cupón! Código: ${couponCode}, Descripción: ${couponDescription}`;
//     const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
    
//     // Marcar el cupón como canjeado
//     fetch(`/redeem/${couponCode}`)
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === "success") {
//                 // Desactivar el botón
//                 const whatsappButton = document.getElementById('whatsapp-button');
//                 whatsappButton.disabled = true;
//                 // Actualizar el estado del cupón
//                 document.getElementById('coupon-status').textContent = "Canjeado";
//                 // Abrir WhatsApp
//                 window.open(url, '_blank');
//             } else {
//                 alert("Error al canjear el cupón.");
//             }
//         });
// }