from django.shortcuts import render,HttpResponse

# Create your views here.
def show(request):
    return render(request,'index.html')
    #return HttpResponse('Hello! , I am Amisha Agarwal')