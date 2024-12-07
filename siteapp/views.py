from django.shortcuts import render, get_object_or_404, redirect
from siteapp.forms import AlunoForms
from siteapp.forms import EventoForms
from siteapp.models import Aluno

def lista(request):
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'pg_al/lista.html', context)


def new(request):
    alunos = Aluno.objects.all()
    form = AlunoForms(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            aluno = form.save()
            aluno.save()
            form = AlunoForms()
            return redirect('lista')
    context={'form':form, 'alunos':alunos}
    return render(request, 'pg_al/new.html', context)

def mostrar(request):
    alunos = Aluno.objects.all()
    context={'alunos':alunos}
    return render(request, 'pg_al/lista.html', context)

def editar(request, id):
    alunos =Aluno.objects.all()
    aluno = get_object_or_404(Aluno, pk=id)
    form= AlunoForms(instance=aluno)
    if (request.method=='POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista')
        else:
            return render(request, 'pg_al/editar.html',{'form':form})
    else:
        return render(request,'pg_al/editar.html',{'form':form, 'alunos':alunos})

def excluir(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    alunos = Aluno.objects.all()
    if(request.method == "POST"):
        aluno.delete()
        return redirect('lista')
    return render(request, 'pg_al/excluir.html', {'aluno':aluno, 'alunos':alunos, 'form':form})



#------------------------------------------------------------------------------------------------------
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForms

def ev_lista(request):
    eventos = Evento.objects.filter(id_aluno=request.user.id)
    return render(request, 'pg_ev/ev_lista.html', {'eventos': eventos})

def ev_new(request):
    if request.method == 'POST':
        form = EventoForms(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            return redirect('ev_lista')
    else:
        form = EventoForms()
    return render(request, 'pg_ev/ev_new.html', {'form': form})

def ev_editar(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    if request.method == 'POST':
        form = EventoForms(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('ev_lista')
    else:
        form = EventoForms(instance=evento)
    return render(request, 'pg_ev/ev_editar.html', {'form': form})


def ev_excluir(request, id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)
    if request.method == 'POST':
        evento.delete()
        return redirect('ev_lista')
    return render(request, 'pg_ev/ev_excluir.html', {'evento': evento})
