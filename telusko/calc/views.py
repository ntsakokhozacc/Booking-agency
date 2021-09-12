from django.http.response import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#LANDING PAGE WITH FORM
def home(request):
    return render(request, 'home.html', {'MyName':'Ntsako Benedict Khoza'})


#ADDITTION PAGE THAT SHOWS RESULTS
def add(request):
    val1 =int(request.POST['num1'])
    val2 =int(request.POST['num2'])
    res=val1+val2
    return render(request, 'result.html',{'result':res})