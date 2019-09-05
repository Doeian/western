from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import MENU, kontakt, oferta, rezerwacja, wydarzenia1
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import loginForm





class MenuView(View):

    def get(self, request):
        return render(request, 'głowna.html', {'MENU': MENU})


    def post(self, request):
        pass

class KontaktView(View):

    def get(self, request):
        kontakt_firma = kontakt.objects.all()
        return render(request, "kontakt.html", {"kontakt":kontakt_firma})

class OfertaView(View):

    def get(self, request):
        oferta_firma = oferta.objects.all()
        return render(request, 'oferta1.html', {"oferta":oferta_firma})

class RezerView(View):
    def get(self, request):
        rezerwacja_hotel = rezerwacja.objects.all()
        return render(request, 'rezerwacje.html', {"rezerwacja":rezerwacja_hotel})


class wydarzenieView(View):
    def get(self, request):
        wydarzenie_hotel = wydarzenia1.objects.all()
        return render(request, 'wydarzenia.html', {"wydarzenia":wydarzenie_hotel} )

class RenderLoginPageView(View):

    def get(self, request):
        form = loginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                messages.success(request, 'Wrong login or password')
                return HttpResponseRedirect('/logowanie/')
            elif user is not None:
                loginForm(request, user)
                return HttpResponseRedirect('/zarzadzaniestrona/')


class modyfikacja_wydarzeniaView(View):

    def get(self, request):
        return render(request, "modyfikacjawyd.html")


class zarzadzanie_strnaView(View):

    def get(self, request):
        return render(request, 'zarzadzanie strona.html')

class modyfikacjaofertyView(View):

    def get(self, request):
        return render(request, 'ofertamod.html')

class modyfikacjarezerwView(View):

    def get(self, request):
        return render(request, 'rezerwacjemod.html')

class konrtaktmodView(View):

    def get(self, request):
        return render(request, 'modykontakt.html')
