htmx.on("porduct_add", function (e){
    Swal.fire({
        icon: 'success',
        text: 'Produit ajouté dans le panier.',
        timer: 3000
    })

    span_total_product = document.querySelectorAll("#total_product")
    for (item of span_total_product) {
        item.innerHTML = e.detail.total_product
    }
});