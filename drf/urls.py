from django.contrib import admin
from django.urls import path
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('error/', views.pagina_error, name='error'),
]


from django.contrib import admin
from django.urls import path
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('error/', views.pagina_error, name='error'),
]

# Le decimos a Django que use tu vista para los links rotos
handler404 = 'noticias.views.pagina_error'

