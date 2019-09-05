from django.db import models


MENU = (
    (1, "Kontakt"),
    (2, "Oferta"),
    (3, "Galeria"),
    (4, "Adres"),
    (5, "Imprezy"),
    (6, "Rezerwacje"),
)

# Create your models here.
class kontakt(models.Model):
     nazwa_firmy = models.CharField(max_length=64)
     numer_telefonu = models.IntegerField()


class oferta(models.Model):
    nazwa_oferty = models.CharField(max_length=64)
    koszt_oferty = models.IntegerField()
    czas_oferty = models.DateTimeField(auto_now_add=True)
    maksymalna_ilość_osob = models.IntegerField()


class rezerwacja(models.Model):
    ilosc_pokoi = models.IntegerField()
    nazwa_pokoju = models.CharField(max_length=64)
    ilosc_miejsc = models.IntegerField()

class goscie(models.Model):
    nazwa_pokoju = models.CharField(max_length=64)
    czas_pobytu_od = models.DateTimeField
    czas_do = models.DateTimeField
    ilosc_miejsc = models.IntegerField()

class wydarzenia1(models.Model):
    nazwa_wydarzenia = models.CharField(max_length=123)
    miejsce_wydarzenia = models.CharField(max_length=64)
    opis_wydarzenia = models.CharField(max_length=300)


