from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app1/vista1.html")

def vista2(request):
    return render(request,"app1/vista2.html")