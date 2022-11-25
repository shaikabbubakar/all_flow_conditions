from django.shortcuts import render

# Create your views here.
def a2_first(request):
    t={'a':22,'b':33,'c':34}
    return render(request,'a2_first.html',context=t)
def a2_second(request):
    s={'name':'AbbuBakar'}
    return render(request,'a2_second.html',s)