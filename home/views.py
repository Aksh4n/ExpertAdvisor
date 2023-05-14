from django.shortcuts import render
from . models import *
from django.http import JsonResponse

# Create your views here.def home(request):
def home(request):
    products = Product.objects.all()
    blog_category = BlogCategory.objects.all()
    post = Post.objects.all()
    return render(request, 'index.html' , {'products':products , 'cat':blog_category , 'posts': post})

