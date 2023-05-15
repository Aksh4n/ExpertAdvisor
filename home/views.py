from django.shortcuts import render
from . models import *
from django.http import JsonResponse
from . forms import *
from django.shortcuts import render, get_object_or_404
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
    context = {'product': product , 'products':products}
    return render(request, 'product_detail.html', context)


def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })
