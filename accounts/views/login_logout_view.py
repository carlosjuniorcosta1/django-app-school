from django.shortcuts import render, redirect
from django.contrib import messages, auth
from ..models import CustomUser as User 
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from django.views.generic import DetailView, ListView


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user_picture = request.FILES.get('user_picture')
        has_accepted_terms = bool(request.POST.get('has_accepted_terms'))

        if not has_accepted_terms:
            messages.error(request, "Você deve aceitar os termos e condições.")
            return render(request, 'registration/register.html')

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
                        last_name=last_name,
                        has_accepted_terms = has_accepted_terms
                    )
                if user_picture:
                    user.user_picture = user_picture
                user.save()
                auth.login(request, user)
                return redirect("dashboard")
                
           
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
            return redirect('index') 
        else:
            messages.error(request, "Usuário e/ou senha inválidos")
            return render(request, "registration/login.html")
    else:
        return render(request, "registration/login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return render(request, 'static_content/index.html')


def terms_of_acceptance(request):
    return render(request, 'registration/term_of_acceptance.html')