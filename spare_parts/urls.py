# spare_parts URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#    1. Add an import:  from my_app import views
#    2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#    1. Add an import:  from other_app.views import Home
#    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#    1. Import the include() function: from django.urls import include, path
#    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
# Import the 'admin' module for Django's admin site

from django.urls import path, include
# Import the 'path' function and 'include' function from 'django.urls'

from django.conf import settings
# Import the 'settings' module for accessing Django project settings

from django.conf.urls.static import static
# Import the 'static' function for serving static files during development

# Import URL patterns for the 'spareapp' application
urlpatterns = [
    path('admin/', admin.site.urls),
    # Define a URL pattern for the admin site
    
    path('', include('spareapp.urls')),
    # Define a URL pattern for including the URL patterns from the 'spareapp' application
]

# Serve static files (like images, CSS, JavaScript) during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
