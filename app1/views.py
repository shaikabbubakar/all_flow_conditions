from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':100,'b':200,'c':150}
    return render(request,'a1_first.html',d)
def a1_second(request):
    e={'a':20,'b':30,'c':25}
    return render(request,'a1_second.html',e)