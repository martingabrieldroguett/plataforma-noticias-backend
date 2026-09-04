from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bienvenida.html')

def pagina_error(request, exception=None):
    return render(request, 'error.html', status=404)

