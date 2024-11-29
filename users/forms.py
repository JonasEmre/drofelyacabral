from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()  # Doğru kullanıcı modelini al

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "contact-form__input",
                "placeholder": "Kullanıcı adınızı girin",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "contact-form__input",
                "placeholder": "Şifrenizi belirleyin",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "contact-form__input",
                "placeholder": "Şifrenizi tekrar girin",
            }
        )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "contact-form__input", "placeholder": "E-Posta adresiniz"}
        )
    )

    class Meta:
        model = User  # Burada varsayılan model yerine CustomUser kullanılacak
        fields = ["username", "email", "password1", "password2"]
