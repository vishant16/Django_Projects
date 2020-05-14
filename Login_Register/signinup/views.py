from django.shortcuts import render
from .models import signin
from .forms import UserForm

def Login(request):
    return render(request,"login.html")

def Register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("form saved")
                return redirect('/login/')
            except:
                pass
    else:
        form = UserForm()
    return render(request,'register.html',{'form':form})
