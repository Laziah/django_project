from django.shortcuts import render, redirect
# Import necessary function for rendering templates and redirecting

from django.http import HttpResponse, HttpResponseRedirect
# Import classes for handling HTTP responses

# Importing our models
from .models import *
# Import the models defined in the same directory as the views

# Importing our form
from .forms import *
# Import the forms defined in the same directory as the views

# Importing our filters
from .filters import *
# Import the filters defined in the same directory as the views

# A decorator is an arrangement where you just reference a function but you don't call it.
from django.contrib.auth.decorators import login_required
# Import the decorator for requiring authentication for views

# Import the 'reverse' function for URL reversing
from django.urls import reverse

# Define your views here.

def index(request):
    return render(request, 'ziah/be_real.html')
# Render the 'be_real.html' template for the 'index' view

def home(request):
    # Querying our database and ordering items by id
    products = Product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset=products)
    products = product_filters.qs
    # Returning the filtered and ordered products
    return render(request, 'ziah/home.html', {'products': products, 'product_filters': product_filters})

@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'ziah/product_detail.html', {'product': product})
# Display the details of a specific product if the user is logged in

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'ziah/receipt.html', {'sales': sales})
# Display the receipts of sales transactions if the user is logged in

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id=pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            # Update stock quantity and save the sale
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            return redirect('receipt')
    return render(request, 'ziah/issue_item.html', {'sales_form': sales_form})

def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'ziah/receipt_details.html', {'receipt': receipt})
# Display the details of a specific receipt

def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'ziah/all_sales.html', {'sales': sales, 'total': total, 'change': change, 'net': net})
# Display all sales transactions and calculate total, change, and net amounts

@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
    return render(request, 'ziah/add_to_stock.html', {'form': form})
# Add items to stock and update stock quantity

def about(request):
    return render(request, 'ziah/about.html')
# Render the 'about.html' template for the 'about' view

def contact(request):
    return render(request, 'ziah/contact.html')
# Render the 'contact.html' template for the 'contact' view

def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'ziah/register.html', {'form': form})
# Render the 'register.html' template for the 'register' view if the request method is GET
