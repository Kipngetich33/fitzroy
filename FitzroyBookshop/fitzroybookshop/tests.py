from django.test import TestCase
from . models import Product

class ProductTestClass(TestCase):
    '''
    A class that test the Product class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.prod = Product(title = 'test title1',isbn = 'ISBN 0000',category ='Book',author = 'test author1',publisher = 'test publisher1',price = 90,quantity = 10,image ='images/img.png')

    def test_instance(self):
        '''
        method that test is Product objects are instanciated correctly
        '''
        self.assertTrue(isinstance(self.prod,Product)) 

    def test_save_prod(self):
        '''
        method that test the save method of model image
        '''
        self.prod.save_prod()
        all_prods= Product.objects.all()
        self.assertTrue(len(all_prods)>0)

    def test_delete_prod(self):
        '''
        method that tests the delete_prod method
        '''
        self.prod.save_prod()
        new_prod = Product(title = 'test title2',isbn = 'ISBN 1111',category ='Video',author = 'test artist',publisher = 'test publisher2',price = 10,quantity = 10,image ='images/vid.mpeg')
        new_prod.save_prod()
        self.prod.delete_prod()
        all_prods = Product.objects.all()
        self.assertTrue(len(all_prods)==1)

    def test_search_prod(self):
        '''
        Method that test the search_prod method
        '''
        self.prod.save_prod()
        new_prod = Product(title = 'test title2',isbn = 'ISBN 1111',category ='Book',author = 'test artist',publisher = 'test publisher1',price = 90,quantity = 10,image ='images/vid.mpeg')
        new_prod.save_prod()
        all_prods = Product.search_prod(80,100,'Book','test publisher1')  
        self.assertTrue(len(all_prods) ==2)        
