from django.shortcuts import render, get_object_or_404, redirect
from siteapp.forms import AlunoForms
from siteapp.forms import EventoForms
from siteapp.models import Aluno

# Create your views here.
def lista(request):
    alunos = Aluno.objects.all()  # Recupera todos os objetos Aluno
    context = {'alunos': alunos}
    return render(request, 'pg/lista.html', context)


def new(request):
    alunos = Aluno.objects.all()
    form = AlunoForms(request.POST, request.FILES)
    if request.method == "POST":
        #form = AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            aluno = form.save()
            aluno.save()
            form = AlunoForms()
            return redirect('lista')
    context={'form':form, 'alunos':alunos}
    return render(request, 'pg/new.html', context)

# usar esse caso quando o template for único para exibir alunos
def mostrar(request):
    alunos = Aluno.objects.all() # todos os objetos que estiverem na classe aluno
    context={'alunos':alunos}
    return render(request, 'pg/lista.html', context)

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
            return render(request, 'pg/editar.html',{'form':form})
    else:
        return render(request,'pg/editar.html',{'form':form, 'alunos':alunos})

def excluir(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    alunos = Aluno.objects.all()
    if(request.method == "POST"):
        aluno.delete()
        return redirect('lista')
    return render(request, 'pg/excluir.html', {'aluno':aluno, 'alunos':alunos, 'form':form})