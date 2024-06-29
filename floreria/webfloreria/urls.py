from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subir/', views.subir_producto, name='subir_producto'),
    path('modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/casero/', views.productos_caseros, name='productos_caseros'),
    path('productos/maceteros/', views.productos_maceteros, name='productos_maceteros'),
    path('productos/thojas/', views.productos_thojas, name='productos_thojas'),
    path('productos/todos/', views.productos_totales, name='todo_prod'),
    path('registro/', views.registro_user, name='registro'),
    path('phone_login/', views.phone_login_view, name='phone_login'),
    path('compra/', views.compra, name='compra'),
    path('presentacion/', views.presentacion, name='presentacion'),
    path('contacto/', views.contacto, name='contacto'),
    path('ayuda/', views.ayuda, name='ayuda'),
]
