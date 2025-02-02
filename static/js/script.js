document.addEventListener("DOMContentLoaded", function () {
    // Verificar si localStorage ya tiene los cupones
    if (!localStorage.getItem("unlocked_coupons")) {
        // Leer cookies existentes
        const cookies = document.cookie.split("; ");
        let unlockedCoupons = {};

        cookies.forEach(cookie => {
            const [name, value] = cookie.split("=");
            if (name.startsWith("coupon_")) {
                try {
                    const couponData = JSON.parse(decodeURIComponent(value));
                    unlockedCoupons[name.replace("coupon_", "")] = couponData;
                } catch (e) {
                    console.error("Error al leer la cookie:", e);
                }
            }
        });

        // Guardar en localStorage
        if (Object.keys(unlockedCoupons).length > 0) {
            localStorage.setItem("unlocked_coupons", JSON.stringify(unlockedCoupons));

            // Eliminar cookies antiguas
            cookies.forEach(cookie => {
                const [name] = cookie.split("=");
                document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
            });
        }
    }
});
