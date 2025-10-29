from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import *

# Create your views here.

    
def singin(request):
    
    if request.method == "POST":
       
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            
            messages.success(request, "user creat successfully")
            return redirect("singin")
        
       # messages.error(request, "error user creation")
        #return redirect("add-items")
    else:
        
        form = RegForm()
        
        return render(request, "regester.html",{'form':form})