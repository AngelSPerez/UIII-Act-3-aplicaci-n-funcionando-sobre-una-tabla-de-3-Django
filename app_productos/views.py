from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        precio_venta = request.POST.get('precio_venta')
        stock = request.POST.get('stock', 0)
        codigo_barras = request.POST.get('codigo_barras', '')
        categoria_id = request.POST.get('categoria')
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio_venta=precio_venta,
            stock=stock,
            codigo_barras=codigo_barras,
            categoria_id=categoria_id
        )
        return redirect('ver_productos')
    return render(request, 'producto/agregar_producto.html')

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre', producto.nombre)
        producto.descripcion = request.POST.get('descripcion', producto.descripcion)
        producto.precio_venta = request.POST.get('precio_venta', producto.precio_venta)
        producto.stock = request.POST.get('stock', producto.stock)
        producto.codigo_barras = request.POST.get('codigo_barras', producto.codigo_barras)
        producto.save()
        return redirect('ver_productos')
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})