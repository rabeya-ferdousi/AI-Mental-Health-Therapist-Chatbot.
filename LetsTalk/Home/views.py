from django.shortcuts import render, redirect
def loadpage(request):
    return render(request,'Home/loadpage.html',{})