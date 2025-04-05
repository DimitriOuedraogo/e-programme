from django.urls import path

from . import views


urlpatterns =[
    path("",views.creer_tache, name="create-tache"),
    path('generer_programme/', views.generer_programme, name='generer_programme'),
]