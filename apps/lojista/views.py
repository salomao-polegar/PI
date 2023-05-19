from django.shortcuts import render, redirect, HttpResponse
from agenda.models import Agenda
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required(login_url="/admin")
def index(request):
    # GET
   
    if request.method == 'GET':
        context = {
            'agendamentos' : Agenda.objects.filter(horario__gte=datetime.today()).order_by('horario')
        }
        return render(request, 'lojista/index.html', context=context)
    
    # POST
    id = request.POST.get('id')
    try:
        Agenda.objects.get(pk=id).delete()
    except ObjectDoesNotExist:
        pass

    context = {
            'agendamentos' : Agenda.objects.filter(horario__gte=datetime.today()).order_by('horario')
    }
    return render(request, 'lojista/index.html', context=context)

@login_required(login_url="/admin")
def sair(request):
    logout(request)
    return redirect('admin:index')
