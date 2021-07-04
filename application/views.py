from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def fullmonte_web(request):
    return render(request, "FullMonteWeb.html")

def pocket_travel(request):
    return render(request, "PocketTravel.html")

def reversi(request):
    return render(request, "ReversiAI.html")

def gunman_jump(request):
    return render(request, "GunmanJump.html")

def bubble_mania(request):
    return render(request, "BubbleMania.html")

def cycle_63(request):
    return render(request, "Cycle63.html")

def tuner_pro(request):
    return render(request, "TunerPro.html")

def ml_classifier(request):
    return render(request, "OregonWildlifeClassifier.html")