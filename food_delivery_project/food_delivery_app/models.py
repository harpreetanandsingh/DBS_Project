from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# class CustomUser(AbstractUser):
#     CUSTOMER = '1'
#     RESTAURANT = '2'
#     DELIVERY = '3'
     
#     EMAIL_TO_USER_TYPE_MAP = {
#         'customer': CUSTOMER,
#         'restaurant': RESTAURANT,
#         'delivery person': DELIVERY
#     }
 
#     user_type_data = ((CUSTOMER, "CUSTOMER"), (RESTAURANT, "Restaurant"), (DELIVERY, "Delivery"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
class Authenticate(models.Model):
    p_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #p_id = models.ForeignKey(Authenticate, on_delete=models.CASCADE)

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=255)
    

class Products(models.Model):
    itemId = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    ordered_on = models.DateTimeField(auto_now=True)

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_val = models.CharField(max_length=255)

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255)

class deliveryPersonnel(models.Model):
    personnel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class orderItems(models.Model):
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Address(models.Model):
    add_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

class CustAddress(models.Model):
    add_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class CustNos(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ph_no = models.IntegerField()

class RestAddress(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    add_id = models.ForeignKey(Address,on_delete=models.CASCADE)

class restPhNos(models.Model):
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    ph_no = models.IntegerField()

class personnelAddr(models.Model):
    personnel_id = models.ForeignKey(deliveryPersonnel, on_delete=models.CASCADE)
    add_id = models.ForeignKey(Address,on_delete=models.CASCADE)


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    statusId = models.ForeignKey(Status, on_delete=models.CASCADE)
    orderId = models.ForeignKey(orders, on_delete=models.CASCADE)
    personnelId = models.ForeignKey(deliveryPersonnel, on_delete=models.CASCADE)
    timeDispatch = models.DateTimeField()
    timeArrival = models.DateTimeField()

class Reviews(models.Model):
    #delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    del_rev = models.CharField(max_length=255)
    food_rev = models.CharField(max_length=255)
    stars = models.IntegerField()



class payInfo(models.Model):
    custId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    infoId = models.AutoField(primary_key=True)
    payMode = models.CharField(max_length=100)
    payDescr = models.CharField(max_length = 100)


class Payment(models.Model):
    payId = models.AutoField(primary_key=True)
    payDate = models.DateTimeField()
    infoId = models.ForeignKey(payInfo, on_delete=models.CASCADE)

# class cancelledOrder(model.Model):
#     orderId = models.ForeignKey(orders, on_delete=models.CASCADE)
#     reason = models.CharField(max_length=100)
#     refundId = models.


