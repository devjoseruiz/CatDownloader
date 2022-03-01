from django.shortcuts import render
from . import tasks


def index(request):
    tasks.download_kitten_image.delay()
    return render(request, 'main/index.html')
