from django import forms 


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Nombre"}))                           
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"ejemplo@gmail.com"}))
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control',"placeholder":"Escribe tu mensaje"}))


