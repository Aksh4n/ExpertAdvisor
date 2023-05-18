from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogCategory)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Message)
from django import forms
class ProductForm(forms.ModelForm):
    inputs = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
admin.site.register(Product,ProductAdmin)