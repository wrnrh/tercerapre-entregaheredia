from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('suscripcion', views.Suscripcion, name="suscripcion"),
    path('betatester', views.Betatester, name="betatester"),
    path('inscripcion', views.Inscripcion, name="inscripcion"),
   
]

