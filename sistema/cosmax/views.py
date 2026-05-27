from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Libro, Cliente
from .singleton import ConfiguracionSistema 

def login_view(request):

    config = ConfiguracionSistema()

    nombre_sistema = config.NOMBRE_SISTEMA

    contexto = {
        'nombre_sistema': nombre_sistema
    }

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

    return render(request, 'login.html', contexto)


@login_required
def vista_index(request):
    config = ConfiguracionSistema()

    total_libros = Libro.objects.count()

    total_clientes = Cliente.objects.count()

    unidades_stock = sum(
        libro.stock for libro in Libro.objects.all()
    )

    nombre_sistema = config.NOMBRE_SISTEMA

    stock_bajo = Libro.objects.filter(
        stock__lte=config.STOCK_BAJO
    ).count()

    contexto = {
        'total_libros': total_libros,
        'total_clientes': total_clientes,
        'unidades_stock': unidades_stock,
        'stock_bajo': stock_bajo,
        'nombre_sistema': nombre_sistema
    }

    return render(request, 'index.html', contexto)

@login_required
def catalogo(request):

    busqueda = request.GET.get('buscar', '')

    libros = Libro.objects.filter(
        titulo__icontains=busqueda
    )

    return render(
        request,
        'catalogo.html',
        {
            'libros': libros,
            'busqueda': busqueda
        }
    )


@login_required
def agregar_libro(request):

    if request.method == 'POST':

        Libro.objects.create(
            titulo=request.POST['titulo'],
            autor=request.POST['autor'],
            precio=request.POST['precio'],
            stock=request.POST['stock']
        )

        return redirect('catalogo')

    return render(request, 'agregar_libro.html')


@login_required
def editar_libro(request, libro_id):

    libro = get_object_or_404(
        Libro,
        id=libro_id
    )

    if request.method == 'POST':

        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.precio = request.POST['precio']

        libro.save()

        return redirect('catalogo')

    return render(request, 'editar_libro.html', {'libro': libro})


@login_required
def eliminar_libro(request, libro_id):

    libro = get_object_or_404(Libro, id=libro_id)

    libro.delete()

    return redirect('catalogo')


@login_required
def stock(request):

    config = ConfiguracionSistema()

    nombre_sistema = config.NOMBRE_SISTEMA

    busqueda = request.GET.get('buscar', '')

    libros = Libro.objects.filter(titulo__icontains=busqueda)

    total_unidades = sum(libro.stock for libro in Libro.objects.all())

    stock_bajo = Libro.objects.filter(stock__lte=config.STOCK_BAJO).count()

    sin_stock = Libro.objects.filter(stock=0).count()

    contexto = {
        'libros': libros,
        'busqueda': busqueda,
        'total_unidades': total_unidades,
        'stock_bajo': stock_bajo,
        'sin_stock': sin_stock,
        'nombre_sistema': nombre_sistema
    }

    return render(request, 'stock.html', contexto)


@login_required
def ajustar_stock(request, libro_id):

    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':

        libro.stock = request.POST['stock']
        libro.save()

    return redirect('stock')


