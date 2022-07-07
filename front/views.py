from django.shortcuts import render

def front_contact(request):
    return render(request, "shop/pages/contact.html")
