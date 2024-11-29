from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    subscription_email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "form-input", "placeholder": "E-Posta adresiniz"}))

    class Meta:
        model = Subscription
        fields = ['subscription_email', ]


class ContactForm(forms.Form):
    sender_email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "contact-form__input", "placeholder": "E-Posta adresiniz"}))
    context = forms.CharField(widget=forms.Textarea(
        attrs={"class": "contact-form__message", "placeholder": "Mesajınızı buraya yazabilirsiniz."}))


