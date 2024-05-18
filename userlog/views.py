from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from userlog.models import *
# Create your views here.
def login_page(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        if not User.objects.filter(username = email).exists():
            messages.info(request, "Wrong Username or Password")
            return redirect('/login')
        
        user =authenticate(username = email, password = password)
        if user is None:
            messages.info(request,  "Wrong Username or Password")
            return request('/login')
        else:
            login(request,user)
            return redirect('/')


    return render(request, "login.html")

def signup_page(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        print(email)
        print(password)
        
        user = User.objects.filter(username = email)
       
        if user.exists():
            messages.info(request ,"Username Already Exist")
            return redirect("/signup")

        user = User.objects.create(
            username = email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account Succesful Created")
        return redirect('/signup')
    return render(request, "signup.html")

@login_required(login_url= "/login")
def edit_page(requset,id):
    datas = user_details.objects.get(id = id)
    context = {'data' : datas }
    if requset.method == "POST":
        data = requset.POST
        name = data.get("name")
        ide = data.get("id")
        password = data.get("password")
        if len(name)  > 3 and len(ide) >3  and len(password) >3:
            datas.name = name 
            datas.ids = ide
            datas.password = password
            datas.save()

            return redirect("/")
        return redirect("/edit/id")
        



    return render(requset, "edit.html",context)

@login_required(login_url= "/login")
def addnew(request):

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        ides = data.get('id')
        password = data.get('password')

        if len(name)  > 3 and len(ides) >3  and len(password) >3:
            user_details.objects.create(
                name = name,
                ids = ides,
                password = password,
            )
            return redirect('/')
        else:
            print(len(name), len(id), len(password))
            return redirect('/addnew')
        
        

    return render(request,  "addnew.html")


@login_required(login_url= "/login")
def logout_page(request):
    logout(request)
    return redirect('/login')

@login_required(login_url= "/login")
def delete_id(request,id):
    data = user_details.objects.get( id = id)
    data.delete()
    return redirect('/')