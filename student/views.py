from django.shortcuts import render,redirect
from .forms import StudentInfo
from .models import Student
# Create your views here.

def home(request):
    if request.method =='POST':
        fm=StudentInfo(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=Student(name=name,email=email,password=password)
            reg.save()
            return redirect('/')
    else:
        fm=StudentInfo()
    stud=Student.objects.all()    
    return render(request,'show_detail.html',{'form':fm,'stud':stud})


def update(request,id):
    if request.method=='POST':
        get_data=Student.objects.get(pk=id)
        fm=StudentInfo(request.POST,instance=get_data)
        if fm.is_valid():
            fm.save()
            return redirect('/')   
    else:
        get_data=Student.objects.get(pk=id)
        fm=StudentInfo(instance=get_data)

    return render(request,'update_detail.html',{'form':fm})

def delete(request,id):
    info=Student.objects.get(pk=id)
    info.delete()
    return redirect('/')    