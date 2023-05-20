from django.shortcuts import render , redirect
from . models import *
from django.http import JsonResponse
from . forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.def home(request):
def home(request):
    products = Product.objects.all()
    blog_category = BlogCategory.objects.all()
    post = Post.objects.all()
    return render(request, 'index.html' , {'products':products , 'cat':blog_category , 'posts': post})

def product(request):
    products = Product.objects.all()
    blog_category = BlogCategory.objects.all()
    post = Post.objects.all()
    return render(request, 'Ea.html' , {'products':products , 'cat':blog_category , 'posts': post})

import json

def product_detail(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)
    inputs = json.loads(product.inputs or '{}').items()
    context = {'product': product, 'inputs': inputs , 'products':products}
    return render(request, 'product_detail.html', context)
def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })
def logout_user(request):
    logout(request)
    return redirect('home')

from .forms import CustomUserCreationForm

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']  # Get the email value from the form
            user.email = email
            user.save()
            return JsonResponse({'msg': 'Success'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'msg': 'Err', 'errors': errors})
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'msg': 'Success'})
        else:
            return JsonResponse({'msg': 'Err', 'error': 'Invalid credentials'})


def profile(request):
    products = Product.objects.all()
    return render(request, 'profile.html', {'products':products})
def updateprofile(request):
	if request.method == "POST":
		customer = Customer.objects.get(id=request.user.customer.id)
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid:
			form.save()
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'err'})
def ideas(request):
    products = Product.objects.all()
    blog_category = BlogCategory.objects.all()
    posts = Post.objects.all()
    posts = sorted(posts, key=lambda x: x.date, reverse=True)
    comments = Comment.objects.all()
    return render(request, 'ideas.html', {'posts':posts,'comments':comments,'cat':blog_category,'products':products})
