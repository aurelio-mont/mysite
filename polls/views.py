from django.http import HttpResponse


# Create your views here.
def index(request):
    a = 2 + 3
    return HttpResponse('Hola, la pagina esta funcionando {}'.format(a))
