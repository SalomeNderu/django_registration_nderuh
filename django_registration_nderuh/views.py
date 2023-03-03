from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student

def index_page(request):
    data = Student.objects.all()
    context = {'data':data}
    return render(request, "index.html", context)
def login_page(request):
    return render(request, "login.html")
def edit_page(request):
    return render(request, "edit.html")
def signup_page(request):
    return render(request, "signup.html")
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')
        query = Student(name=name, email=email, age=age, gender=gender, phone=phone, city=city, country=country)
        query.save()
        return redirect("/")
    return render(request, "index.html")
def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")
def UpdateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')

        update = Student.objects.get(id=id)
        update.name = name
        update.email = email
        update.age = age
        update.gender = gender
        update.phone = phone
        update.city = city
        update.country = country

        update.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
