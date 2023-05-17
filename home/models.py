from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200)
    TestVideo = models.CharField(max_length=200)
    Eduvideo = models.CharField(max_length=200)
    explain = models.TextField()
    pricebasic = models.CharField(null=True, blank=True,max_length=200)
    pricepro = models.CharField(null=True, blank=True,max_length=200)
    pricelifetime = models.CharField(null=True, blank=True,max_length=200)
    
    date = models.DateField(auto_now_add=True,null=True, blank=True)
    metaquotes = models.CharField(max_length=200,null=True, blank=True)
    backtest1 = models.ImageField(null=True,blank=True)
    backtest2 = models.ImageField(null=True,blank=True)
    backtest3 = models.ImageField(null=True,blank=True)
    backtest4 = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url          


    
class Post(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=400,null=True,blank=True)
    short_info = models.CharField(max_length=400,null=True,blank=True)
    heading = models.CharField(max_length=400,null=True,blank=True)
    text1 = models.TextField(null=True,blank=True)
    text2 = models.TextField(null=True,blank=True)
    video_link = models.CharField(max_length=400,null=True,blank=True)

    date = models.DateField(auto_now_add=True)
    img1 = models.ImageField(null=True,blank=True)
    img2 = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.img1.url
        except:
            url = ''
        return url   




class Contact(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)



    def __str__(self):

        return self.subject  


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    last = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200 , null=True)
    email = models.CharField(max_length=200 , null=True)
    def __str__(self):
        return str(self.user)
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        customer_email = instance.email  # Get the email from the User instance
        customer = Customer.objects.create(user=instance, email=customer_email)
        # Create welcome message
        subject = 'Welcome to Our Website'
        message_text = f'Dear {customer.user},\n\nThank you for registering with us. We are excited to have you as our customer!\n\nBest regards,\nThe Admin Team'
        sender = User.objects.get(username='sarsh')  # Assuming 'admin' is the username of the admin user
        recipient = instance

        welcome_message = Message.objects.create(sender=sender, recipient=recipient, subject=subject, message=message_text)
post_save.connect(create_customer, sender=User)
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject