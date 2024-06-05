from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import CustomUser as User 
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(username= username).exists():
                messages.error(request, "Usuário já existente")
                return render(request, 'registration/register.html')

            if User.objects.filter(email=email).exists():
                    messages.error(request, "Email já está cadastrado")
                    return render(request, 'registration/register.html')
            else:
                user = User.objects.create_user(
                        username=username, 
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                user.save()
                messages.success(request, "Cadastro realizado com sucesso")
                auth.login(request, user)
                return render(request, "registration/dashboard.html")
                
           
        else:
            messages.error(request, 'Senhas não conferem')
            return render(request, 'registration/register.html')
    else:
        return render(request, 'registration/register.html')


    

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você logou')
            return render(request, "registration/dashboard.html")
        else:
            messages.error(request, "Usuário e/ou senha inválidos")
            return render(request, "registration/login.html")
    else:
        return render(request, "registration/login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Você deslogou")
    return render(request, 'static_content/index.html')

def dashboard(request):
    return render(request, 'registration/dashboard.html')