from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm


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
    context = {'form': form}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["username"])
    else:
        form = SignUpForm()
    return render(request, template_name='users/signup.html', context=context)

def test(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, template_name='users/test.html', context=context)









