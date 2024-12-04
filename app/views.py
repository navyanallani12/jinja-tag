from django.shortcuts import render

# Create your views here.
dict={'a':'1o'}
def jinja(request):
    #dict={'a':'1o'}
    return render(request,'jinja.html',context=dict)