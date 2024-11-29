from django.shortcuts import render, redirect
from django.contrib import messages



def ana_sayfa(request):
    return render(request, "core/ana_sayfa.html")


# Gruba üye mi kontrol eden fonksiyon
def is_in_panik_atak_group(user):
    return 


def set_programi(request):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name="Panik Atak").exists():            
            # user panik atak grubunda mı kontrol et öyleyse render yap
            return render(request, "core/panik-atak-set-programi.html")
        else:
            messages.error(
                request, "Set programına erişiminiz bulunmamaktır."
            )
            return redirect('ana-sayfa')
    else:
        # user girili değilse o zaman komple login sayfasına yönlendir
        messages.error(
                request, 'Hesabınıza giriş yapmanız gerekmektedir.'
            )
        return redirect('giris')


def panik_atak(request):
    return render(request, "core/panik-atak.html")


def anksiyete(request):
    return render(request, "core/anksiyete.html")


def depresyon(request):
    return render(request, "core/depresyon.html")


def iliski_cift_terapisi(request):
    return render(request, "core/iliski-cift-terapisi.html")


def takintili_dusunce(request):
    return render(request, "core/takintili-dusunce.html")


def ofke_kontrol_bozukluk(request):
    return render(request, "core/ofke-kontrol-bozukluk.html")


def sosyal_fobi(request):
    return render(request, "core/sosyal-fobi.html")


def dinletiler(request):
    return render(request, "core/dinletiler.html")


def hakkinda(request):
    return render(request, "core/hakkinda.html")


def iletisim(request):
    return render(request, "core/iletisim.html")
