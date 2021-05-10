from django.db import models
from .figures import Figure
import urllib.request


class StartA(models.Model):
    start = models.CharField('URL', max_length=200) 

class FigureManager(models.Manager):
    def getFigure(self):
        startanalysis = StartA.objects.last()
        url = 'None'
        if hasattr(startanalysis, 'start'):
            url = urllib.request.urlopen("https://" + startanalysis.start)
            data = url.read()
            test = len(data)
            url = startanalysis.start
        else:
            test = 100
        fig = Figure(test)
        bs64 = fig.psd()

        return bs64, test, url

class FigureModel(models.Manager):
    objects = FigureManager()

