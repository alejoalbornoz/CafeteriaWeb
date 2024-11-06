from django import template
from pages.models import Page


register = template.Library() #Registarmos esto en la libreria de tamplates

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages 