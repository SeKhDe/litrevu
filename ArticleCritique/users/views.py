from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from .models import User

def login_page(request):
    form = LoginForm()
    context = {'form': form}
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'],)

            if user is not None:
                print("connexion reussie")
                login(request, user)
                message = f"Bonjour {user.username}"
                return redirect('test')

            else:
                message = "Identifiant ou mot de passe incorrect"
                print("connexion invalid")

    return render(request, template_name='users/login.html', context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    form = SignUpForm()
    message = ""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password1"] == form.cleaned_data["password2"]:
                User.objects.create_user(username=form.cleaned_data["username"],
                                         password=form.cleaned_data["password1"],)
                return redirect('test')

            else:
                message = 'Les mots de passe ne sont pas identiques.'
                form = SignUpForm(initial={'username': form.cleaned_data["username"],} )


    else:
        form = SignUpForm()
    return render(request, template_name='users/signup.html', context={'form': form, 'message': message})

def test(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, template_name='users/test.html', context=context)









