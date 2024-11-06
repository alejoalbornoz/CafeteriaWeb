from .models import Link


#Este es un procesador de contexto
def context_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
        
    return ctx