from .models import Subscription
from .forms import SubscriptionForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def abone_ol(request):
    if request.method == "POST":
        abone_form = SubscriptionForm(request.POST)
        if abone_form.is_valid():
            subscription_email = abone_form.cleaned_data.get("subscription_email")
            if not Subscription.objects.filter(subscription_email=subscription_email).exists():
                abone_form.save()
                messages.success(request, f"Abone listemize hoş geldin {subscription_email}")
            else:
                messages.error(request, f"Zaten abone listemizdesin sevgili {subscription_email}")

            # Formu temizleme
            abone_form = SubscriptionForm()
    else:
        abone_form = SubscriptionForm()
    return {"abone_form": abone_form}


def iletisim_formu(request):
    if request.method == "POST":
        iletisim_form = ContactForm(request.POST)
        if iletisim_form.is_valid():
            sender_email = iletisim_form.cleaned_data.get("sender_email")
            context = iletisim_form.cleaned_data.get("context")
            # Email gönderme mantığını buraya sonra yazacağım.
            # Send email logic
            subject = f"İletişim Postası: {sender_email}"
            message = f"Gönderici: {sender_email}\n\nContext: {context}"
            from_email = settings.DEFAULT_FROM_EMAIL
            # Use your actual recipient email address
            recipient_list = [settings.DEFAULT_FROM_EMAIL]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            messages.success(
                request,
                "Mesajınız bize gönderilmiştir. Müsait olduğumuzda size dönüş sağlayacağız.",
            )
    else:
        iletisim_form = ContactForm()
    iletisim_form = ContactForm()
    return {"iletisim_form": iletisim_form}
