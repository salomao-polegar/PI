from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta, time
from django.utils import timezone
import pandas as pd

HORARIOFUNCIONAMENTO = [
    [time(9,0), time(19,0)]
]
DIASABERTOS = [
    [datetime.today(), datetime.today()+timedelta(days=7), ]
]



def definir_intervalos(minutos):
    horariosDisponiveis = []                
    horarioInicial = DIASABERTOS[0][0].replace(hour=HORARIOFUNCIONAMENTO[0][0].hour, minute=HORARIOFUNCIONAMENTO[0][0].minute)
    horarioFinal = DIASABERTOS[0][1].replace(hour=HORARIOFUNCIONAMENTO[0][1].hour, minute=HORARIOFUNCIONAMENTO[0][1].minute)
    # percorrendo dias
    while datetime(horarioInicial.year, horarioInicial.month, horarioInicial.day) <= datetime(horarioFinal.year, horarioFinal.month, horarioFinal.day):

        # percorrendo horário
        while time(horarioInicial.hour, horarioInicial.minute) <= time(horarioFinal.hour, horarioFinal.minute):
            
            # TODO filtrar horários já utilizados na agenda


            horariosDisponiveis.append([int(horarioInicial.timestamp()),
                str(horarioInicial.day).zfill(2)+ 
                "/"+
                str(horarioInicial.month).zfill(2)+ 
                "/"+
                str(horarioInicial.year).zfill(2)+ 
                " "+
                str(horarioInicial.hour).zfill(2)+ 
                ":"+
                str(horarioInicial.minute).zfill(2)
                ])
            horarioInicial += timedelta(minutes=minutos)
        horarioInicial+=timedelta(days=1)
        horarioInicial=horarioInicial.replace(hour=HORARIOFUNCIONAMENTO[0][0].hour, minute=HORARIOFUNCIONAMENTO[0][0].minute)

    #print(horariosDisponiveis)

    # agenda = Agenda.objects.filter(horario__gte=timezone.now())
    # print(pd.DataFrame(agenda.values()))
    # horariosDisponiveis2 = []
    # for i in agenda:
    #     print(i.horario)
    #     print(i.servico.duracao)

    #     for j in horariosDisponiveis:
    #         if j[0] >= i.horario.timestamp() and j[0] <= (i.horario+timedelta(hours=i.servico.duracao.hour,minutes=i.servico.duracao.minute)).timestamp():
    #             print(datetime.fromtimestamp(j[0]))
    #         else:
    #             horariosDisponiveis2.append(j)
    #     horariosDisponiveis = horariosDisponiveis2
    return horariosDisponiveis



# Create your views here.

def index(request):
    
    context = {
        'servicos' : Servico.objects.all(),
        'horarios' : definir_intervalos(15),
        'formaPagamento' : FormasDePagamento.objects.all()
    }

    # GET
    if request.method == 'GET':
        return render(request, "agenda/index.html", context=context)    
    
    # POST
    servicoAgenda = request.POST.get('servicoAgenda', None)
    horarioAgenda = request.POST.get('horarioAgenda', None)
    nomeAgenda  = request.POST.get('nomeAgenda', None)
    telefoneAgenda  = request.POST.get('telefoneAgenda', None)
    formaPagamento = request.POST.get('formaPagamento', None)
    cliente, _ = Cliente.objects.get_or_create(nome=nomeAgenda, celular=telefoneAgenda)

    agendaCriada = Agenda.objects.create(
        servico = Servico.objects.get(pk=servicoAgenda),
        cliente = cliente,
        horario = datetime.fromtimestamp(int(horarioAgenda)),
        formaPagamento = FormasDePagamento.objects.get(pk=formaPagamento)
        )
    agendaCriada.save()

    context['agendaCriada'] = agendaCriada

    return render(request, "agenda/index.html", context=context)    
    
    

def agendar(request):

    return render(request, "agenda/index.html")

def servico(request, id=None):

    if id==None:
        return redirect(index)
    servico = Servico.objects.get(id=id)
    fotosServico = FotosServico.objects.filter(servico=servico)
    context = {
        'servico' : servico,
        'fotosServico' : fotosServico
    }    
    
    return render (request, 'agenda/servico.html', context=context)