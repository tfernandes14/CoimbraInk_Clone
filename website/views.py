from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import requests


from .models import *


def home(request):
    reprografias = Reprografia.objects.all()
    todas = get_lat_long()
    print(todas)
    return render(request, 'base.html', {'reprografias': reprografias, 'lista': todas})


def get_lat_long():
    res = []
    tam_reprografias = len(list(Reprografia.objects.all()))
    response = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCrc4kHDhi7GOYb5IBKUn1mrj6MsX85eNg')
    # print("$$$", response.json())
    # print("%%%%", response.json()['location']['lat'])
    # print("$$$$", response.json()['location']['lng'])
    res.append(["", response.json()['location']['lat'], response.json()['location']['lng']])
    for i in range(1, tam_reprografias + 2):
        try:
            rep = Reprografia.objects.get(id=i)
        except ObjectDoesNotExist:
            rep = None
        if rep is not None:
            aux = [rep.nome, rep.latitude, rep.longitude]
            res.append(aux)
    return res


def simulador(request):
    reprografias = Reprografia.objects.all()

    A5 = Acinco.objects.all()
    tese = Tese.objects.all()
    A4 = Aquatro.objects.all()
    A3 = Atres.objects.all()
    A2 = Adois.objects.all()
    A1 = Aum.objects.all()
    A0 = Azero.objects.all()

    return render(request, 'simulador.html', {'reprografias': reprografias,
                                              'A5': A5, 'A4': A4, 'A3': A3,
                                              'A2': A2,'A1': A1, 'A0': A0, 'tese' : tese})
