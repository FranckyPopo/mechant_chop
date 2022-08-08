span_total_product = document.querySelectorAll("#total_product");
span_tota_price_cart = document.querySelector("#tota_price_cart");

htmx.on("product_add", function (e){
    Swal.fire({
        icon: 'success',
        text: 'Produit ajouté dans le panier.',
        timer: 2000
    });

    for (item of span_total_product) {
        item.innerHTML = e.detail.total_product;
    };

    span_tota_price_cart.innerHTML = e.detail.tota_price_cart.total_price_cart  + " XOF"
});

htmx.on("product_delete", function (e){
    for (item of span_total_product) {
        item.innerHTML = e.detail.total_product;
    };

    span_tota_price_cart.innerHTML = e.detail.tota_price_cart.total_price_cart  + " XOF"
});

