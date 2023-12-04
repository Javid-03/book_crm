from django.shortcuts import render,redirect
from django.views import View
from first.forms import SignupForm,SigninForm,StudentForm,BookForm
from first.models import Student,Book

class Viewlogin(View):
    def get(self,request):
        form=SignupForm()
        return render(request,"signup.html",{"form":form})

    def post(self,request):
        form=SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            p=form.cleaned_data.get('email')
            print(p)
        else:
            print("gud by")
        return render(request,"signup.html",{"form":form})
    
class Viewsignin(View):
    def get(self,request):
        form=SigninForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request):
        form=SigninForm(request.POST)
        form.is_valid()
        p1=form.cleaned_data.get("password1")
        p2=form.cleaned_data.get("password2")
        if p1==p2:
            print("Login success!")
        else:
            print("Login Failed")
        return render(request,"signin.html",{"form":form})
    
class Viewstudent(View):
    def get(self,request):
        form=StudentForm()
        return render(request,"add.html",{"form":form})
    
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Student.objects.create(**form.cleaned_data)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})


class Viewbook(View):
    def get(self,request):
        form=BookForm()
        return render(request,"book.html",{"form":form})
    
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Book.objects.create(**form.cleaned_data)
            return render(request,"book.html",{"form":form})
        else:
            return render(request,"book.html",{"form":form})
        
class Booklist(View):
    def get(self,request):
        qs=Book.objects.all()
        return render(request,"booklist.html",{"qs":qs})
    
class Bookdetails(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get('pk')
        qs=Book.objects.get(id=id)
        return render(request,"bookdetails.html",{"data":qs})


class Book_delete(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs= Book.objects.get(id=id).delete()
        return redirect('book-al')