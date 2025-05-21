from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import add_blogs, contacts, add_thought

# ================home and about=========================

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

# =====================Blog===============================

def add_blog(request):
    if request.method=="POST":
        # data fetching
        username=request.POST.get("username")
        textarea=request.POST.get("textarea")
        check=request.POST.get("check")

        # create model Objects and use data
        b=add_blogs()
        b.name=username
        b.add_blog=textarea
        b.checking=check
        if check is None:
            b.checking=False
        else:
            b.checking=True
        
        # save
        b.save()
        return redirect("view_blog")
   
    return render(request,"add_blog.html",{})


def view_blog(request):
   blog=add_blogs.objects.all()
   return render(request,"view_blog.html",{'blog': blog})

# ===================Thoughts===========================

def view_thoughts(request):
    thoughts=add_thought.objects.all()
    return render(request,"view_thoughts.html",{'thoughts': thoughts})

    return render(request,"view_thoughts.html")

def add_thoughts(request):
    if request.method=="POST":
        # data fetch from html
        name= request.POST.get("name")
        thought=request.POST.get("thought")
        check=request.POST.get("check")

        # create model objects and use data
        t=add_thought()       # class object
        t.name=name
        t.thought=thought
        t.checking=check
        if check is None:
            t.checking=False
        else:
            t.checking=True
            # save
            t.save()
            return redirect("view_thoughts")

    return render(request,"add_thoughts.html",{})

# =====================Contact=========================

def contact(request):
    if request.method=="POST":

        # data fetch from html
        name= request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        feedback=request.POST.get("feedback")

        # create model objects
        c=contacts()
        c.name=name
        c.email=email
        c.number=number
        c.feedback=feedback

        # save
        c.save()
        return redirect("home")

    return render(request,"contact.html",{})

# ===================Login and Register================

def register(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user= User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account Registerd Sucessfully!")
        return redirect("home")
    return render(request, "register.html")

def user_login(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          
          user = authenticate(request, username=username, password=password)
          
          if user is not None:
              login(request, user)
              return redirect('home')
          else:
              messages.error(request, "Invalid username or password.")
              return render(request, 'login.html')
      
      return render(request, 'login.html')
  

