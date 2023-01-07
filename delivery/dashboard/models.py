from django.db import models

def upload_to(instance, filename):
    return 'images/items/{filename}'.format(filename=filename)

def upload_to_restaurant(instance, filename):
    return 'images/restaurants/{filename}'.format(filename=filename)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'Item', related_name='order', blank=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

class Address(models.Model):
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.street

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)
    rating  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

