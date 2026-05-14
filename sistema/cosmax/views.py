from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario:
            login(request, usuario)
            return redirect('vista_index')

    return render(request, 'login.html')


@login_required
def vista_index(request):
    return render(request, 'index.html')
