from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
    if form.is_valid():
        your_email = form.cleaned_data.get('your_email')
        form.save()
        messages.success(request, f'Создан аккаунт {your_email}!')

        return redirect('index')
    else:
        form = register_form()

    return render(request, 'register.html', {'form': form})


def login(request):
    your_email = request.POST["email"]
    your_password = request.POST["password"]
    user = authenticate(request, username=your_email, password=your_password)

    login(request, user)

    return redirect("index")
