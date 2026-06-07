from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Libro, Cliente, Venta, DetalleVenta, Usuario
from .singleton import ConfiguracionSistema 
from django.contrib.auth.hashers import make_password

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

@login_required
def venta(request):

    busqueda = request.GET.get('buscar','')

    ventas = Venta.objects.filter(cliente__nombre__icontains=busqueda).order_by('-fecha')

    contexto = {'ventas': ventas,'clientes': Cliente.objects.all(),'libros': Libro.objects.filter(stock__gt=0)}

    return render(request,'venta.html', contexto)

@login_required
def agregar_venta(request):

    if request.method == 'POST':

        cliente = Cliente.objects.get(id=request.POST['cliente']
        )

        libro = Libro.objects.get(id=request.POST['libro'])

        cantidad = int(request.POST['cantidad'])

        metodo_pago = request.POST['metodo_pago']

        if cantidad <= 0:
            return redirect('venta')

        if libro.stock < cantidad:
            return redirect('venta')

        subtotal = libro.precio * cantidad

        venta = Venta.objects.create(cliente=cliente, empleado=request.user, metodo_pago=metodo_pago, total=subtotal)

        DetalleVenta.objects.create(venta=venta, libro=libro, cantidad=cantidad, subtotal=subtotal)

        libro.stock -= cantidad

        libro.save()

    return redirect('venta')

@login_required
def cliente(request):

    config = ConfiguracionSistema()

    nombre = Cliente.nombre

    apellido = Cliente.apellido

    email = Cliente.email

    telefono = Cliente.telefono

    nombre_sistema = config.NOMBRE_SISTEMA

    contexto = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono,
        'nombre_sistema': nombre_sistema
    }

    return render(request, 'cliente.html', contexto)

@login_required
def registrar_cliente(request):

    if request.method == "POST":

        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            telefono=request.POST['telefono']
        )

        return redirect('cliente')

@login_required
def usuarios(request):

    busqueda = request.GET.get('buscar', '')

    usuarios = Usuario.objects.filter(username__icontains=busqueda)

    contexto = {

        'usuarios': usuarios,

        'total_usuarios': Usuario.objects.count(),

        'admins': Usuario.objects.filter(rol='ADMIN').count(),

        'empleados': Usuario.objects.filter(rol='EMPLEADO').count(),

        'busqueda': busqueda

    }

    return render(request, 'usuario.html',contexto)

    
@login_required
def agregar_usuario(request):

    if request.method == 'POST':

        Usuario.objects.create(

            username=request.POST['username'],

            email=request.POST['email'],

            rol=request.POST['rol'],

            password=make_password(request.POST['password'])

        )

    return redirect('usuario')

@login_required
def editar_usuario(request, usuario_id):

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':

        usuario.email = request.POST['email']

        usuario.rol = request.POST['rol']

        usuario.save()

    return redirect('usuario')

@login_required
def eliminar_usuario(request, usuario_id):

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if usuario != request.user:

        usuario.delete()

    return redirect('usuario')
    


