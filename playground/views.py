from django.shortcuts import render , redirect
from .models import Student
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("student")   # redirect anywhere you want
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student")
    return render(request, "signup.html", {"form": form})



def index(request):
    return render(request, 'child.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def student(request):
    students = Student.objects.all()
    return render(request, 'student.html' , { 'students': students})

