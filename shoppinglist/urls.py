"""shoppinglist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from shop.views import home_page, add_item, add_list, ShopList, ListDetail
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('lists/add', add_item, name='add'),
    path('accounts/', include('allauth.urls')),
    path('lists/', ShopList.as_view(), name='lists'),
    path('lists/details/<int:pk>', ListDetail.as_view(), name='listdetails'),
    path('lists/addlist', add_list, name='addlists'),
]

urlpatterns += staticfiles_urlpatterns()
