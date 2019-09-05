"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from strona.views import MenuView, KontaktView, OfertaView, RezerView, wydarzenieView, RenderLoginPageView, modyfikacja_wydarzeniaView, zarzadzanie_strnaView, modyfikacjaofertyView, modyfikacjarezerwView, konrtaktmodView

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', MenuView.as_view(), name="index"),

    url(r'kontakt/', KontaktView.as_view()),

    url(r'oferta/', OfertaView.as_view()),

    url(r'rezerwacje/', RezerView.as_view()),

    url(r'wydarzenia1/', wydarzenieView.as_view()),

    url(r'logowanie/', RenderLoginPageView.as_view()),

    url(r'zarzadzaniestrona/', zarzadzanie_strnaView.as_view()),

    url(r'wydarzeniamod/', modyfikacja_wydarzeniaView.as_view()),

    url(r'ofertamod/', modyfikacjaofertyView.as_view()),

    url(r'rezerwacjemod/', modyfikacjarezerwView.as_view()),

    url(r'modykontakt1/', konrtaktmodView.as_view())
    ]
