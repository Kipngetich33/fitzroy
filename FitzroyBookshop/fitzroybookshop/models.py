from django.db import models

# Create your models here.

class Product(models.Model):
    '''
    class that defines the structure of product object found in 
    Fitzroy Bookshop
    '''
    title = models.CharField(max_length=50)
    isbn =  models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    price = models.IntegerField( null = True)
    quantity = models.IntegerField(null = True)
    image = models.ImageField(upload_to = 'images/' ,null = True)

    def __str__(self):
        return self.title 

    def save_prod(self):
        self.save()

    def delete_prod(self):
        self.delete()

    @classmethod
    def find_prod(cls,name):
        found_prods = cls.objects.filter(username__icontains = name).all()
        return found_prods

    @classmethod
    def search_prod(cls,min_price,max_price,category,publisher):
        '''
        Method that filter the object in the database based on the specifications
        of the users and returns a list of objects which satisfy these filters
        '''
        list_1 =[]
        requested_products = cls.objects.filter(category = category,publisher = publisher).all()
        for item in requested_products:
            if item.price>= min_price and item.price <= max_price:
                list_1.append(item)
        return list_1


class Image(models.Model):
    '''
    Class that defines the structure of the image objects
    '''
    name = models.CharField(max_length= 30)
    image = models.ImageField(upload_to = 'images/' ,null = True)