from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from webshop.models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    # try:
    #     product = Product.objects.get(pk=product_id) 
    # except Product.DoesNotExist:    
    #     raise Http404("Product does not exist")
    return render(request, 'webshop/product_view.html', {'product': product})

def available_products(request):
    products = Product.objects.filter(quantity__gt=0) 
    return render(request, 'webshop/product_list.html', {'products': products})
