from django import forms


class PosteoFormulario(forms.Form):   
    titulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(widget=forms.Textarea)
    autor = forms.EmailField()
    fecha = forms.DateTimeField(widget=forms.SelectDateWidget)