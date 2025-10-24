from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Persona
# Create your views here.
def index(request):
    personas_reniec = Persona.objects.all()
    #output = ", ".join([q.nombre for q in personas_reniec])
    #return HttpResponse(output) 
    #return HttpResponse("Hello, this is the Personas app index page.")
    #template = template.get_template('personas/index.html')
    context = {
        'personas_reniec': personas_reniec,
    }
    return render(request, 'personas/index.html', context)

def results(request, persona_id):
    try:
        persona = Persona.objects.get(pk=persona_id)
    except Persona.DoesNotExist:
        raise  Http404("Persona no encontrada")
    return HttpResponse(f"Resultados de la persona: {persona.nombre} {persona.apellido_paterno} {persona.apellido_materno}, DNI: {persona.dni}")

def get_for_dni(request, dni):
    try:
        persona = Persona.objects.get(dni=dni)
    except Persona.DoesNotExist:
        raise  Http404("Persona no encontrada")
    return render(request, 'personas/dni.html', {'persona': persona})