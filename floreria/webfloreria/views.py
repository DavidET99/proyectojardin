from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import ProductoForm
from .models import Productos
from .forms import ProductoUpdateForm
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ControlUsuarios
from .forms import PhoneLoginForm
from django.contrib.auth.decorators import login_required






def index(request):
    mensaje_bienvenida = f'Hola, {request.user.username}'
    return render(request, 'index.html', {'mensaje_bienvenida': mensaje_bienvenida})

def presentacion(request):
    
    return render(request, 'presentacion.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def ayuda(request):
    
    return render(request, 'ayuda.html')

def subir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subir_producto') 
    else:
        form = ProductoForm()
    return render(request, 'formulario.html', {'form': form})

def modificar_producto(request, pk):
    producto = get_object_or_404(Productos, pk=pk)

    if request.method == 'POST':
        form = ProductoUpdateForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('subir_producto')  
    else:
        form = ProductoUpdateForm(instance=producto)

    return render(request, 'modificar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('subir_producto')  

    return render(request, 'eliminar_producto.html', {'producto': producto})

def productos_caseros(request):
    
    productos_caseros = Productos.objects.filter(categoria='Casero')

    
    return render(request, 'productos_caseros.html', {'productos': productos_caseros})

def productos_maceteros(request):
    productos_maceteros = Productos.objects.filter(categoria='Macetero')
    return render(request, 'productos_maceteros.html', {'productos': productos_maceteros})

def productos_thojas(request):
    productos_thojas = Productos.objects.filter(categoria='thojas')
    return render(request, 'productos_thojas.html', {'productos': productos_thojas})

def productos_totales(request):
    productos = Productos.objects.all()
    return render(request, 'todo_prod.html', {'productos': productos})

def registro_user(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

def phone_login_view(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            telefono = form.cleaned_data['telefono']
            try:
                user = ControlUsuarios.objects.get(telefono=telefono)
                login(request, user)
                mensaje_bienvenida = f'Hola, {user.username}!👋'
                return render(request, 'index.html', {'mensaje_bienvenida': mensaje_bienvenida})
            except ControlUsuarios.DoesNotExist:
                error_message = "Número de teléfono incorrecto."
                return render(request, 'phone_login.html', {'form': form, 'error_message': error_message})
    else:
        form = PhoneLoginForm()
    return render(request, 'login.html', {'form': form})

def compra(request):
    products = request.GET.get('products', '').split(',')
    quantities = list(map(int, request.GET.get('quantities', '').split(',')))

    products_in_cart = []

    total = 0

    for product_name, quantity in zip(products, quantities):
        product = Productos.objects.get(nombre=product_name)
        products_in_cart.append((product, quantity))
        total += product.precio * quantity

    return render(request, 'compra.html', {'cart': products_in_cart, 'total': total})

