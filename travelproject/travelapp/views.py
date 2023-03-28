from django.shortcuts import render
from .models import Place
from .models import Actor

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request, "index.html",{'result':obj})
def actor(request):
    obg=Actor.objects.all()
    return render(request, "index.html",{'key':obg})


#def addition(request):
#   x = int(request.GET['num1'])
#   y = int(request.GET['num2'])
#   res = x + y
#   return render(request, "result.html", {'result': res})
