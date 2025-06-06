from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Customer
from app.my_forms import CustomerForm, LoginForm
from app.my_serializers import CustomerSerializer


# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        names = request.POST.get("names")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        gender = request.POST.get("gender")
        Customer.objects.create(name=names, email=email, phone=phone, password=password ,weight=weight, height=height, gender=gender)
        count = Customer.objects.all().count()
        print(f"{count}Customers")
    return render(request,'home.html')
@login_required

def show(request):
    data = Customer.objects.all().order_by('-id')# select * from customers
    return render(request,'show.html',{'data':data})
@login_required

def delete(request,id):
    user = Customer.objects.get(id=id)
    user.delete()
    return redirect('show-page')
@login_required

def details(request,id):
    user = Customer.objects.get(id=id)

    return render(request,'details.html',{'user':user})
@login_required

def add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show-page')

    else:
         form = CustomerForm()
    return render(request,'forms.html',{'form':form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate( request,username=username, password=password)
            if user:
                login(request, user)#sessions and cookies
                return redirect('show-page')
    else:
        form = LoginForm()
    return render(request,'signin.html',{'form':form})

@api_view(['GET'])
def api_customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_save(request):
    person =request.data
    serializer = CustomerSerializer(data=person)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"})
    return Response(serializer.errors)

@api_view(['DELETE'])
def api_delete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return Response({"message":"delete"})
