from django.shortcuts import render
from django.views.generic import CreateView

from polls.forms import TelefonForm
from polls.models import Telefon


def index(request):
    telefonlar = Telefon.objects.all()
    return render(request, 'polls/index.html', {
        'telefonlar': telefonlar
    })

class TelefonCreateView(CreateView):
    model = Telefon
    form_class = TelefonForm
    success_url = '/polls/'