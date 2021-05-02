from django.shortcuts import render

from polls.models import Telefon


def index(request):
    telefonlar = Telefon.objects.all()
    return render(request, 'polls/index.html', {
        'telefonlar': telefonlar
    })