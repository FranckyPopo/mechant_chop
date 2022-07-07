from django.shortcuts import render

def front_contact(request):
    return render(request, "front/pages/contact.html")
