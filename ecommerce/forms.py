from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"form-full-bane","placeholder":"Your Full Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","id":"form-full-bane","placeholder":"yourname@yourdomain.com"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"form-full-bane","placeholder":"Your content here"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be a gmail")
        return email