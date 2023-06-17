from django.shortcuts import render , redirect
from . models import *
from django.http import JsonResponse
from . forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
import json
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


def product_detail(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)
    inputs = json.loads(product.inputs or '{}').items()
    context = {'product': product, 'inputs': inputs , 'products':products}
    if request.method == "POST":
        apikey = '6QW5RCW-HW7MBKQ-JFD823E-1527K1S'
        # Prepare the data to be sent as JSON response
        data = {
            'descrip': product.description,
            'price': product.pricebasic,
            'price2': product.pricepro,
            'price3': product.pricelifetime,
            'plan':request.POST.get('plan'),
            'api':apikey,

            # Add more data as needed
        }

        # Get the order ID from the request
        order_id = request.POST.get('order_id')

        # Create an Order object
        order = Order(
            user=request.user,
            order_id=order_id,
            status='Pending',
            email=request.user.email,
            product = product.name,
            plan = request.POST.get('plan'),
            nowpayments_response=None
        )
        order.save()

        return JsonResponse(data)  # Return JSON response

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
def MQL(request):
    products = Product.objects.all()
    return render(request, 'MQLfactory.html', {'products':products})
"""
from django.contrib.auth.decorators import login_required
import requests


@login_required
def initiate_payment(request):
    amount = 1000
    currency = 'usd'
    order_id = 'RGDBP-21314'
    order_description = 'Apple Macbook Pro 2019 x 1'
    callback_url = 'https://nowpayments.io'
    success_url = 'https://nowpayments.io'
    cancel_url = 'https://nowpayments.io'
    url = "https://api.nowpayments.io/v1/invoice"

    payload = {
        "price_amount": amount,
        "price_currency": currency,
        "order_id": order_id,
        "order_description": order_description,
        "ipn_callback_url": callback_url,
        "success_url": success_url,
        "cancel_url": cancel_url
    }
    headers = {
        'x-api-key': '6QW5RCW-HW7MBKQ-JFD823E-1527K1S',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        order = Order.objects.create(
            user=request.user,
            order_id=order_id,
            status='pending',
            email=request.user.email,
            nowpayments_response=response.json()
        )
        # Continue with the payment process
        payment_url = response.json().get('invoice_url')
        return redirect(payment_url)
    else:
        # Handle error case
        pass
def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        response = {
            'price': product.pricelifetime,
            'description': product.description,
        }
        return JsonResponse(response)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
        """