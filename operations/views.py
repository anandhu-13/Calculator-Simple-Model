from django.shortcuts import render
from django.views.generic import View
from django import forms



# Create your views here.

class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print("result=",result)
        return render(request,"add.html",{"data":result})
    
     

class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'sub.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print("result=",result)
        return render(request,"sub.html",{"data":result})
    

class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'mul.html')
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print("result=",result)
        return render(request,"mul.html",{"data":result})
    

class LeapyearView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'year.html')
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        result=""
        if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
            result=f"{year} is a Leap year"
        else:
            result=f"{year} is not a Leap year"
        
        return render(request,"year.html",{"data":result})
    
    
class EmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'emi.html')
    
    def post(self,request,*args,**kwargs):
        loan_amount=int(request.POST.get("amount"))
        intrest_rate=int(request.POST.get("interest"))
        tenure=int(request.POST.get("tenure"))


        p=loan_amount

        r=intrest_rate/12

        i=r/100
        n=tenure*12
        one_plus_power=(1+i)**n

        EMI=round((p*i*one_plus_power)/(one_plus_power-1))

        print(f"emi amount={EMI}")
        total_intrest_payable=(EMI*n)-p
        total_payment=total_intrest_payable+p

        context={
            "emi":EMI,
            "tip":total_intrest_payable,
            "tp":total_payment
        }

        return render(request,"emi.html",context)



class IndexView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    

    


# localhost:8000/login/

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


     
class SigninView(View):

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    



#localhost:8000/register/ 

class RegistrationForm(forms.Form):
    firstname=forms.CharField(label="FirstName")
    lastname=forms.CharField(label="LastName")
    email=forms.CharField(label="Email")
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password")


class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        form=RegistrationForm()
        print(request.POST.get("firstname"))
        print(request.POST.get("lastname"))
        print(request.POST.get("email"))
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return render(request,"register.html",{"form":form})
    



    



    

    

    
    
    
    


    
    

