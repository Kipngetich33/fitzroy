from django import forms
from . models import Product

CATEGORY_CHOICES= [
    ('book', 'Book'),
    ('audio book', 'Audio Books'),
    ('video', 'Video'),
    ('music', 'Music'),
    ]

PUBLISHER_CHOICES= [
    ('harper collins', 'Harper Collins'),
    ('Penguins', 'Penguins'),
    ('st pauls publication', 'St Pauls Publication'),
    ('franciscan media', 'Franciscan Media'),
    ('orbis', 'Orbis'),
    ]


class ProductForm(forms.Form):
    '''
    class that generates the Product creation form
    ''' 
    title = forms.CharField(label='Title',max_length = 50)
    isbn = forms.CharField(label='ISBN',max_length = 50)
    category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORY_CHOICES))
    author = forms.CharField(label='Author',max_length = 50)
    publisher = forms.CharField(label='Publisher', widget=forms.Select(choices=PUBLISHER_CHOICES))
    price = forms.IntegerField(label='price')
    quantity = forms.CharField(label='Quantity',max_length = 50)
    image = forms.ImageField(label='Image',max_length = 50) 


class SearchForm(forms.Form):
    '''
    class that creates the search form
    ''' 
    min_price = forms.IntegerField(label='Min price')
    max_price = forms.IntegerField(label='Max price')
    category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORY_CHOICES))
    publisher = forms.CharField(label='Publisher', widget=forms.Select(choices=PUBLISHER_CHOICES))