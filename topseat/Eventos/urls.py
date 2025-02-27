from django.conf.urls import url
from .Vistas import views

'''
    URL's de la aplicacion de eventos con sus referencias a las vistas y sus respectivs nombres
'''
app_name='Eventos'

urlpatterns = [
    url(r'^$', views.Ahome.as_view(),name='Ahome'),
    url(r'^Quejas/$', views.SQuejas.as_view(),name='AQuejas'),
    url(r'^Sugerencias/$', views.SSugerencias.as_view(),name='ASugerencias'),
    url(r'^Fallas/$', views.SFallas.as_view(),name='AFallas'),
    url(r'^CrearQueja/$', views.crearQueja.as_view(),name='Crear_Queja'),
    url(r'^CrearSugerencia/$', views.crearSugerencia.as_view(),name='Crear_Sugerencia'),
    url(r'^CrearFalla/$', views.crearFalla.as_view(),name='Crear_Falla'),  
    url(r'^EventoMayor/$', views.reportarMayor.as_view(),name='RM'),  
]