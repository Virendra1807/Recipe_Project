from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Storing Data to back-end 
# decorator LoginRequired is used for confedentiality of main page, no one can access it directly 
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_nm')
        receipe_desc = data.get('receipe_desc')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_desc = receipe_desc,
            receipe_img = receipe_img
        )

        return redirect('/receipes/')

    queryset = Receipe.objects.all()

    # Search Bar logic for here
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))



    context = { 'Showreceipes' : queryset, 'page':'Receipe World'}

    return render(request, 'receipes.html', context)



# Delete Receipe Operation
@login_required(login_url="/login/")
def delete_receipe(request, id):
    
    queryset = Receipe.objects.get(id = id).delete()
    # queryset.delete()
    return redirect('/receipes/')


# Update Recipe Operation
@login_required(login_url="/login/")
def update_receipe(request, id):

    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_nm')
        receipe_desc = data.get('receipe_desc')

    
        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc
        if receipe_img:
            queryset.receipe_img = receipe_img

        queryset.save()

        return redirect('/receipes/')

    context = {'receipe':queryset}

    return render(request, 'update_receipe.html', context)


# Login page function
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")

        else:
            login(request, user)
            messages.error(request, "Login Successfully")
            return redirect('/receipes/')
    
    context = {'page':'Login Page'}
    return render(request, 'login.html', context)

# logout logic
def logout_page(request):
    logout(request)
    return redirect('/login/')


# Register page logic
def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        
        messages.info(request, "Account Created Successfully")

        return redirect('/login/')

    context = {'page':'Registration'}
    return render(request, 'register.html', context)