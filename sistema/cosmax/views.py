from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Libro, Cliente, Venta, DetalleVenta, Usuario
from .singleton import ConfiguracionSistema 
from django.contrib.auth.hashers import make_password
from decimal import Decimal, InvalidOperation

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

    config = ConfiguracionSistema()

    modal_abierto = request.session.pop("modal_abierto", None)

    busqueda = request.GET.get('buscar', '')

    libros = Libro.objects.filter(
        titulo__icontains=busqueda
    )
    nombre_sistema = config.NOMBRE_SISTEMA
    return render(request, 'catalogo.html',
        {
            'libros': libros,
            'busqueda': busqueda,
            'nombre_sistema': nombre_sistema,
            "modal_abierto": modal_abierto
        }
    )


@login_required
def agregar_libro(request):

    if request.method == 'POST':

        titulo = request.POST['titulo'].strip()
        autor = request.POST['autor'].strip()

        try:
            precio = Decimal(request.POST['precio'])
        except (InvalidOperation, ValueError):
            messages.error(request, "El precio debe ser un número válido.")
            request.session["modal_abierto"] = "Agregar"
            return redirect('catalogo')

        stock = int(request.POST['stock'])

        if len(titulo) < 5:
            messages.error(request, "El título debe tener al menos 5 caracteres.")
            request.session["modal_abierto"] = "Agregar"
            return redirect('catalogo')

        if len(autor) < 3:
            messages.error(request, "El nombre del autor debe tener al menos 3 caracteres.")
            request.session["modal_abierto"] = "Agregar"
            return redirect('catalogo')

        if precio <= 0:
            messages.error(request, "El precio debe ser mayor que 0.")
            request.session["modal_abierto"] = "Agregar"
            return redirect('catalogo')

        if stock < 0:
            messages.error(request, "El stock no puede ser negativo.")
            request.session["modal_abierto"] = "Agregar"
            return redirect('catalogo')

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            precio=precio,
            stock=stock
        )

        messages.success(request, "Libro agregado correctamente.")

        return redirect('catalogo')

    return redirect('catalogo')


@login_required
def editar_libro(request, libro_id):

    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':

        titulo = request.POST['titulo'].strip()
        autor = request.POST['autor'].strip()

        try:
            precio = Decimal(request.POST['precio'])
        except (InvalidOperation, ValueError):
            messages.error(request, "El precio debe ser un número válido.")
            request.session["modal_abierto"] = f"Editar{libro.id}"
            return redirect('catalogo')

        if len(titulo) < 5:
            messages.error(request, "El título debe tener al menos 5 caracteres.")
            request.session["modal_abierto"] = f"Editar{libro.id}"
            return redirect('catalogo')

        if len(autor) < 3:
            messages.error(request, "El autor debe tener al menos 3 caracteres.")
            request.session["modal_abierto"] = f"Editar{libro.id}"
            return redirect('catalogo')

        if precio <= 0:
            messages.error(request, "El precio debe ser mayor que 0.")
            request.session["modal_abierto"] = f"Editar{libro.id}"
            return redirect('catalogo')

        libro.titulo = titulo
        libro.autor = autor
        libro.precio = precio
        libro.save()

        messages.success(request, "Libro editado correctamente.")

        return redirect('catalogo')

    return redirect('catalogo')


@login_required
def eliminar_libro(request, libro_id):

    libro = get_object_or_404(Libro, id=libro_id)

    libro.delete()

    return redirect('catalogo')


@login_required
def stock(request):

    config = ConfiguracionSistema()

    modal_abierto = request.session.pop("modal_abierto", None)

    nombre_sistema = config.NOMBRE_SISTEMA

    busqueda = request.GET.get('buscar', '')

    libros = Libro.objects.filter(titulo__icontains=busqueda)

    total_unidades = sum(libro.stock for libro in Libro.objects.all())

    stock_bajo = Libro.objects.filter(stock__lte=config.STOCK_BAJO).count()

    sin_stock = Libro.objects.filter(stock=config.SIN_STOCK).count()

    contexto = {
        'libros': libros,
        'busqueda': busqueda,
        'total_unidades': total_unidades,
        'stock_bajo': stock_bajo,
        'sin_stock': sin_stock,
        'nombre_sistema': nombre_sistema,
        'modal_abierto': modal_abierto
    }

    return render(request, 'stock.html', contexto)


@login_required
def ajustar_stock(request, libro_id):

    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':

        libro.stock = int(request.POST['stock'])
        if libro.stock < 0:
            messages.error(request, "El stock no puede ser negativo.")
            request.session["modal_abierto"] = f"stock{{ libro.id }}"
            return redirect('stock')
        
        libro.save()

    return redirect('stock')

@login_required
def venta(request):
    config = ConfiguracionSistema()

    nombre_sistema = config.NOMBRE_SISTEMA

    modal_abierto = request.session.pop("modal_abierto", None)

    busqueda = request.GET.get('buscar','')

    ventas = Venta.objects.filter(cliente__nombre__icontains=busqueda).order_by('-fecha')

    contexto = {
        'ventas': ventas,
        'clientes': Cliente.objects.all(),
        'libros': Libro.objects.filter(stock__gt=config.SIN_STOCK),
        'nombre_sistema': nombre_sistema,
        'modal_abierto': modal_abierto
        }

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
            messages.error(request, "La cantidad debe ser mayor que 0.")
            request.session["modal_abierto"] = "nuevaVenta"
            return redirect('venta')

        if libro.stock < cantidad:
            messages.error(request, "No hay suficiente stock disponible.")
            request.session["modal_abierto"] = "nuevaVenta"
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

    modal_abierto = request.session.pop("modal_abierto", None)

    busqueda = request.GET.get('buscar','')

    clientes = Cliente.objects.all()

    nombre = Cliente.nombre

    apellido = Cliente.apellido

    email = Cliente.email

    telefono = Cliente.telefono

    nombre_sistema = config.NOMBRE_SISTEMA

    contexto = {
        'clientes': clientes,
        'nombre': nombre,
        'busqueda': busqueda,
        'apellido': apellido,
        'email': email,
        'telefono': telefono,
        'nombre_sistema': nombre_sistema,
        'modal_abierto': modal_abierto
    }

    return render(request, 'cliente.html', contexto)

@login_required
def registrar_cliente(request):

    if request.method == "POST":

        nombre=request.POST['nombre'].strip()
        apellido=request.POST['apellido'].strip()
        email=request.POST['email'].strip()
        telefono=request.POST['telefono'].strip()

        if len(nombre) == 0:
            messages.error(request, "El nombre no puede estar vacío.")
            request.session["modal_abierto"] = "nuevoCliente"
            return redirect('cliente')
        
        if len(apellido) == 0:
            messages.error(request, "El apellido no puede estar vacío.")
            request.session["modal_abierto"] = "nuevoCliente"
            return redirect('cliente')
        
        if len(telefono) == 0:
            messages.error(request, "El teléfono no puede estar vacío.")
            request.session["modal_abierto"] = "nuevoCliente"
            return redirect('cliente')
        
        if len(telefono) != 10:
            messages.error(request, "El teléfono debe tener 10 dígitos.")
            request.session["modal_abierto"] = "nuevoCliente"
            return redirect('cliente') 

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )

        return redirect('cliente')

@login_required
def usuarios(request):

    config = ConfiguracionSistema()

    nombre_sistema = config.NOMBRE_SISTEMA

    busqueda = request.GET.get('buscar', '')

    usuarios = Usuario.objects.filter(username__icontains=busqueda)

    contexto = {
        'usuarios': usuarios,
        'total_usuarios': Usuario.objects.count(),
        'admins': Usuario.objects.filter(rol='ADMIN').count(),
        'empleados': Usuario.objects.filter(rol='EMPLEADO').count(),
        'busqueda': busqueda,
        'nombre_sistema': nombre_sistema

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
    


