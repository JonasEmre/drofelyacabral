from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name="ana-sayfa"),
    path('panik-atak-tedavisi/', views.panik_atak, name="panik-atak"),
    path('anksiyete/', views.anksiyete, name="anksiyete"),
    path('depresyon/', views.depresyon, name="depresyon"),
    path('iliski-cift-terapisi/', views.iliski_cift_terapisi, name="iliski-cift-terapisi"),
    path('takintili-dusunce/', views.takintili_dusunce, name="takintili-dusunce"),
    path('ofke-kontrol-bozukluk/', views.ofke_kontrol_bozukluk, name="ofke-kontrol-bozukluk"),
    path('sosyal-fobi/', views.sosyal_fobi, name="sosyal-fobi"),
    path('dinletiler/', views.dinletiler, name="dinletiler"),
    path('hakkinda/', views.hakkinda, name="hakkinda"),
    path('iletisim/', views.iletisim, name="iletisim"),
]