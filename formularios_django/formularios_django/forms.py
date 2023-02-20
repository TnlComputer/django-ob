from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100,
                           help_text="100 caracteres maximo", required=True)
    url = forms.URLField(label="tu sitio web",
                         required=False, initial='http://')
    comment = forms.CharField(required=False)


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50, required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=50, required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2}))

    # añado las reglas mias propias con
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "Open":
            # error
            raise forms.ValidationError(
                "Tan solo el valor Open esta permitido para este campo")
        else:
            # exito
            return name
