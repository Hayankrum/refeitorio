from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# View para o registro do usuário
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Cria o usuário
            login(request, user)  # Realiza o login automaticamente
            return redirect('home')  # Redireciona para a página inicial ou outra página desejada
    else:
        form = UserCreationForm()  # Exibe o formulário de criação de usuário
    return render(request, 'registro.html', {'form': form})
