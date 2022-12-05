from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


# Create your views here.
from portfolio.forms import UserForm     #View or Logic for collecting the data from the form and saving it in the database
def index(request):
    if request.method == "POST":  #Collecting the data from the form if request is POST method
        form = UserForm(request.POST)
        if form.is_valid():    
          form.save()
        try:
             return redirect('Thank you')   
        except:
                pass
        else:
          template = loader.get_template("index.html",) #getting my template
    stu = UserForm()
    return render(request, "index.html", {"form":stu})