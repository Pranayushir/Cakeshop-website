from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(default="No message provided")

    def __str__(self) -> str:
        return self.name

class cake(models.Model):
    cakeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="cakeimg")
    price = models.IntegerField(default=300)
    
    def __str__(self) -> str:
        return str(self.img)
    

class payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    screenshot = models.ImageField(upload_to="ss/",null=True,default=True)

# class cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     total_amt=models.FloatField()
#     order_dt=models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         verbose_name_plural='8. Orders'

# class cartorder(models.Model):
#     order=models.ForeignKey(cart,on_delete=models.CASCADE)
#     item=models.CharField(max_length=150)
#     image=models.CharField(max_length=200)
#     qty=models.IntegerField()
#     price=models.FloatField()
#     total=models.FloatField()
    
#     class Meta:
#         verbose_name_plural='9. Order iteams'


class usercake(models.Model):
    c = models.IntegerField()
    u = models.IntegerField()
    status = models.BooleanField(default=False)
    




# class ShoppingCart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(cake)


    


