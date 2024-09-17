from .forms import UserForm
from django.shortcuts import render
from django.http import *

def index(request):
 userform = UserForm()
 if request.method == "POST":
  userform = UserForm(request.POST)
 if userform.is_valid():
  name = userform.cleaned_data["name"]
  return HttpResponse("<h2>Имя введено коррректно – {0}</h2>".format(name))
 return render(request, "app/index.html", {"form": userform})


def about(request):
 return HttpResponse("About")
def contact(request):
 return HttpResponseRedirect("/about")
def details(request):
 return HttpResponsePermanentRedirect("/")
def products(request, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request,id=1, name='Максим'):
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3> ".format(id,name)
    return HttpResponse(output)

