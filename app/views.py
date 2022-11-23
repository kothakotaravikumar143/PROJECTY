from django.shortcuts import render

# Create your views here.
def jasiya(request):
    return render(request,'jasiya.html',context={'name':'Jasiya','age':'Ravi'})