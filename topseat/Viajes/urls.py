from django.conf.urls import url
from Viajes.Vistas import views


app_name='Viajes'

urlpatterns = [
    url(r'^$', views.Viajes_homeView.as_view(),name='Viajes_home'),
    url(r'^crearViaje/$', views.crearViaje.as_view(),name='crearViaje'),
    url(r'^verMapa/$', views.verMapa.as_view(),name='verMapa'),
    url(r'^eliminarViaje/$', views.eliminarViaje.as_view(),name='eliminarViaje'),
    url(r'^editarViaje/$', views.editarViaje.as_view(),name='editarViaje'),
    url(r'^confirmarReserva/$', views.confirmarReserva.as_view(),name='confirmarReserva'),
    url(r'^eliminarReserva/$', views.eliminarReserva.as_view(),name='eliminarReserva'),
    url(r'^IniciarViaje/$', views.IniciarViaje.as_view(),name='IniciarViaje'),
    
]