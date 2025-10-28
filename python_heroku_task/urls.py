"""python_heroku_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from my_app import urls as my_app_urls
    2. Add a URL to urlpatterns:  path('my_app/', include(my_app_urls))
Note that the order matters: broader patterns should come first, more specific later.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect  # New: For redirecting root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Your blog paths
    path('', lambda request: HttpResponseRedirect('/blog/')),  # New: Redirect root to blog
]