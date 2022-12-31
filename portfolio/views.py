from django.shortcuts import render, redirect
from .models import User

# Create your views here.


# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get the form data from the request.POST dictionary
        Fullname = request.POST['Fullname']
        Email = request.POST['Email']         
        Phone = request.POST['Phone']
        Comment = request.POST['Comment']

        # Save the form data to the database
        User.objects.create(Fullname=Fullname, Email=Email, Phone=Phone, Comment=Comment)

        # Redirect to a success page
        return redirect('index')
    else:
        # Render the form template
        return render(request, 'index.html')    #Here is the  API for the contact form .