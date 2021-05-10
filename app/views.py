from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StartA, FigureModel
from .figures import Figure
from .forms import StartAForm
import urllib.request


def index(request):
    error = ''
    startanalysis = StartA.objects.last()
    form = StartAForm()


    if request.method == 'POST':
        form = StartAForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Form error'

    bs64, test, url = FigureModel.objects.getFigure()

    context = {
        'form': form,
        'url': url,
        'webdata': test,
        'chart': bs64
    }

    return render(request, 'app/index.html', context)

def addon(request):
    return HttpResponse("TEst")
