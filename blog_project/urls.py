"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  blog_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.http import HttpResponse

# Simple homepage view
def home_view(request):
    return HttpResponse("""
    <h1>Blog Backend API</h1>
    <p>Welcome to the Blog API. Available endpoints:</p>
    <ul>
        <li><a href="/api/">API Root</a></li>
        <li><a href="/admin/">Admin Panel</a></li>
    </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # Option 1: Redirect root to API
    # path('', RedirectView.as_view(url='/api/')),
    
    # Option 2: Simple homepage (uncomment this and comment the above line to use)
    path('', home_view, name='home'),
]