from django.db import models

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
    price = models.CharField(null=True, blank=True,max_length=200)
    date = models.DateField(auto_now_add=True,null=True, blank=True)
    metaquotes = models.CharField(max_length=200,null=True, blank=True)

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
  
    """
class Order(models.Model):
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(max_length=1000)
    image = models.ImageField()



    def __str__(self):

        return self.name  
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url                    
        """