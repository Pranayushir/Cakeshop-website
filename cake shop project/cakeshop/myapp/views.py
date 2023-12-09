from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name = name,email = email,message = message)
        contact.save()
    return render(request,"contact.html")

@login_required(login_url='login')
def menu(request):
    list1 = []
    ck = cake.objects.all()
    
    for x in ck:
        x = model_to_dict(x)
        x["img"] = settings.MEDIA_URL + str(x["img"])
        list1.append({'pk':x['cakeid'],'img':x['img'], 'value':[x['name']],"price" : [x["price"]]})
        

    # for tmp in list1:
    #     print(tmp)
    
    return render(request ,"menu.html",{"hi":list1})

def about(request):
    return render(request,"about.html")



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
# def index(request):
#     return render (request,'home.html')

@login_required(login_url='login')
def paymentview(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        if len(request.FILES)!=0:
            screenshot=request.FILES['photo']
        en=payment(name=name,email=email,screenshot=screenshot)
        en.save()
    return render(request, 'payment.html')

@login_required(login_url='login')
def add_to_cart(request, item_id):
    user_id = request.user.id
    newusercake = usercake(c = item_id, u = user_id)
    newusercake.save()
    return redirect('menu')

@login_required(login_url='login')
def cart_view(request):
    tmp = usercake.objects.filter(u = request.user.id, status = False)
    tot = 0
    ref = 25467
    items = []
    final = 0
    for i in tmp:
        ck = cake.objects.get(cakeid = i.c) 
        tot += ck.price
        ref += ck.cakeid
        ck_img = "/media/"+str(ck.img)
       
        items.append({'name':ck.name, 'price':ck.price,'image':ck_img,'ref':ref})
    
    tax = tot*7/100
    final = tax +tot
    
    tmp.update(status = True)

    return render(request, 'cart.html', {'tot':tot, 'items': items,'tax':tax,'final':final})

