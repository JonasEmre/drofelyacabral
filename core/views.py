from django.shortcuts import render


def ana_sayfa(request):
    return render(request, 'core/ana_sayfa.html')


def panik_atak(request):
    return render(request, 'core/panik-atak.html')


def anksiyete(request):
    return render(request, 'core/anksiyete.html')


def depresyon(request):
    return render(request, 'core/depresyon.html')

def iliski_cift_terapisi(request):
    return render(request, 'core/iliski-cift-terapisi.html')

def takintili_dusunce(request):
    return render(request, 'core/takintili-dusunce.html')

def ofke_kontrol_bozukluk(request):
    return render(request, 'core/ofke-kontrol-bozukluk.html')

def sosyal_fobi(request):
    return render(request, 'core/sosyal-fobi.html')

def dinletiler(request):
    return render(request, 'core/dinletiler.html')

def hakkinda(request):
    return render(request, 'core/hakkinda.html')

def iletisim(request):
    return render(request, 'core/iletisim.html')
