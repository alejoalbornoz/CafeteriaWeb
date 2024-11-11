from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            #Enviamos y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #Asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), #Cuerpo
                "no-contestar@inbox.mailtrap.io", #Email Origen
                ["alejoalbornoz912@gmail.com"], #Email Destino
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse("contact")+"?ok")
            except:
                return redirect(reverse("contact")+"?fail")

    return render(request,"contact/contact.html",{"form":contact_form})
