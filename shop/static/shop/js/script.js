span_total_product = document.querySelectorAll("#total_product");
span_tota_price_cart = document.querySelector("#tota_price_cart");

htmx.on("product_add", function (e){
    for (item of span_total_product) {
        item.innerHTML = e.detail.total_product;
    };

    span_tota_price_cart.innerHTML = e.detail.tota_price_cart.total_price_cart  + " XOF"

    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 1500,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
      })
      
      Toast.fire({
        icon: 'success',
        title: 'Produit ajouté dans le panier.'
      })
});

htmx.on("product_delete", function (e){
    console.log("suppresion");
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 1500,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    })
      
    Toast.fire({
    icon: 'success',
    title: 'Produit supprimer du panier.'
    })
    
    
    for (item of span_total_product) {
        item.innerHTML = e.detail.total_product;
    };

    span_tota_price_cart.innerHTML = e.detail.tota_price_cart.total_price_cart  + " XOF"
});

