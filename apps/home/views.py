from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'welcome': 'Portafolio de Rene Silva'}
    return render(request,'home/index.html', context)