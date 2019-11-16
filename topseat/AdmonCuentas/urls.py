from django.conf.urls import url
from AdmonCuentas import views


app_name='AdmonCuentas'

urlpatterns = [
    url(r'^$', views.home_AdmonCuentas,name='AdmonCuentas_home'),
    url(r'^login/', views.login_v,name='login'),
    url(r'^signup/', views.signup_v,name='signup'),
    url(r'^logout/', views.logout_v,name='logout'),
	url(r'^cambiar/', views.cambiarRol,name='cambiar'),
    url(r'^editarPerfil/', views.actualizarPerfil,name='editar_perfil'),
    url(r'^actualizarContrasena/', views.actualizarContrasena,name='actualizarContrasena'),
    url(r'^eliminarPerfil/', views.eliminarPerfil,name='eliminarPerfil'),
    url(r'^ReporteViajes/', views.ReporteViajes,name='ReporteViajes'),

]