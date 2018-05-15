from django.shortcuts import render
from django.shortcuts import render,redirect
from . models import Product
from . forms import ProductForm,SearchForm

# Create your views here.
def home(request):
    
    return render(request, 'home.html') 

def maintenance(request):
    form = ProductForm()
    if request.method == 'POST':
            form = ProductForm(request.POST,request.FILES)

            if form.is_valid():
                title = form.cleaned_data['title']
                isbn = form.cleaned_data['isbn']
                category = form.cleaned_data['category']
                author = form.cleaned_data['author']
                publisher = form.cleaned_data['publisher']
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']
                image = form.cleaned_data['image']

                prod = Product(title = title, isbn =isbn ,category =category,author =author ,publisher = publisher ,price = price,quantity = quantity ,image = image)
                prod.save()
                form = ProductForm()
            else:
                form = ProductForm()
    return render(request, 'maintenance.html',{"form":form}) 


def search(request):
    form = SearchForm()
    if request.method == 'POST':
            form = SearchForm(request.POST,request.FILES)

            if form.is_valid():
                min_price = form.cleaned_data['min_price']
                max_price = form.cleaned_data['max_price']
                category = form.cleaned_data['category']
                publisher = form.cleaned_data['publisher']
                
                requested_prods = Product.search_prod(min_price,max_price,category,publisher)
                return render(request, 'results.html',{"form":form,"requested_prods":requested_prods})
            else:
                form = ProductForm()
    return render(request, 'search.html',{"form":form}) 

def map(request):
    title = 'Site Map'
    return render(request, 'map.html',{"title":title}) 


