from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import suscripcion, betatester, inscripcion
from AppCoder.forms import suscformulario, betaformulario, inscformulario

# Create your views here.

def inicio(request):

      return render(request, "AppCoder/inicio.html")


def Suscripcion(request):

      return render(request, "AppCoder/suscripcion.html")


def Betatester(request):

      return render(request, "AppCoder/betatester.html")

def Inscripcion(request):

      return render(request, "AppCoder/inscripcion.html")


def Suscripcion(request):

      if request.method == 'POST':

            miFormulario = suscformulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  susc = suscripcion (nombre=informacion['nombre'], email=informacion['email'],) 

                  susc.save()

                  return render(request, "AppCoder/suscripcion.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= suscformulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/suscripcion.html", {"miFormulario":miFormulario})




def Betatester(request):

      if request.method == 'POST':

            miFormulario = betaformulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  beta = betatester (nombre=informacion['nombre'], email=informacion['email'],) 

                  beta.save()

                  return render(request, "AppCoder/betatester.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= betaformulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/betatester.html", {"miFormulario":miFormulario})


def Inscripcion(request):

      if request.method == 'POST':

            miFormulario = inscformulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  insc = inscripcion (nombre=informacion['nombre'], email=informacion['email'],) 

                  insc.save()

                  return render(request, "AppCoder/inscripcion.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= inscformulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/inscripcion.html", {"miFormulario":miFormulario})