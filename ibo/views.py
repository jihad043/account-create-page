from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import *
from .forms import RegForm
# Create your views here.

    
def singin(request):
    
    if request.method == "POST":
       
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            
            messages.success(request, "user creat successfully")
            return redirect()
        
       # messages.error(request, "error user creation")
        #return redirect("add-items")
    else:
        
        form = RegForm()
        
        return render(request, "regester.html",{'form':form})