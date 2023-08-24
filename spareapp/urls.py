from django.urls import path
# Import the 'path' function from the 'django.urls' module for defining URL patterns

# Let us reuse the django login view
from django.contrib.auth import views as auth_views
# Import the default Django authentication views with an alias 'auth_views'

# Lets import views file from 'myapp' Application
from spareapp import views
# Import the 'views' module from the 'spareapp' application

# Define URL patterns for the application
urlpatterns = [
    path('home/', views.home, name='home'),
    # Define a URL pattern for the 'home' view with the name 'home'
    
    path('', views.index, name='index'),
    # Define a URL pattern for the 'index' view with the name 'index'
    
    path('about/', views.about, name='about'),
    # Define a URL pattern for the 'about' view with the name 'about'
    
    path('contact/', views.contact, name='contact'),
    # Define a URL pattern for the 'contact' view with the name 'contact'
    
    path('login/', auth_views.LoginView.as_view(template_name='ziah/login.html'), name='login'),
    # Define a URL pattern for the default Django login view with the name 'login'
    # Use the 'LoginView' from 'auth_views', customize the template using 'template_name'
    
    path('logout/', auth_views.LogoutView.as_view(template_name='ziah/be_real.html'), name='logout'),
    # Define a URL pattern for the default Django logout view with the name 'logout'
    # Use the 'LogoutView' from 'auth_views', customize the template using 'template_name'
    
    path('home/<int:product_id>', views.product_detail, name='product_detail'),
    # Define a URL pattern for the 'product_detail' view that takes an integer 'product_id' as a parameter
    
    # receipt: Here we are issuing out a receipt after the sale
    
    path('receipt/', views.receipt, name='receipt'),
    # Define a URL pattern for the 'receipt' view with the name 'receipt'
    
    path('receipt/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
    # Define a URL pattern for the 'receipt_detail' view that takes an integer 'receipt_id' as a parameter
    
    # sales
    
    path('issue_item/<str:pk>', views.issue_item, name='issue_item'),
    # Define a URL pattern for the 'issue_item' view that takes a string 'pk' as a parameter
    
    path('all_sales/', views.all_sales, name='all_sales'),
    # Define a URL pattern for the 'all_sales' view with the name 'all_sales'
    
    # add to stock
    
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    # Define a URL pattern for the 'add_to_stock' view that takes a string 'pk' as a parameter
]
