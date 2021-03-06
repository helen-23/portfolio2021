from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('cs-projects', views.cs_projects, name='cs_projects'),
    path('art-projects', views.art_projects, name='art_projects'),
    path('FullMonteWeb', views.fullmonte_web, name='FullMonteWeb'),
    path('PocketTravel', views.pocket_travel, name='PocketTravel'),
    path('ReversiAI', views.reversi, name='ReversiAI'),
    path('GunmanJump', views.gunman_jump, name='GunmanJump'),
    path('BubbleMania', views.bubble_mania, name='BubbleMania'),
    path('Cycle63', views.cycle_63, name='Cycle63'),
    path('TunerPro', views.tuner_pro, name='TunerPro'),
    path('OregonWildlifeClassifier', views.ml_classifier, name='OregonWildlifeClassifier')
]