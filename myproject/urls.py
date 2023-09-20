"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path


from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    re_path(r'^hello/', views.welcome),
    re_path(r'^hello1/', views.welcome1),
    re_path(r'^data_analysis/', views.data_analysis_view, name="data_analysis"),
    re_path(r'^FeedAndFetch/', views.feed_in_and_fetch, name="FeedAndFetch"),
    path('process_form/', views.process_form, name='process_form'),
    path('get_data_from_db/', views.get_data_from_db, name='get_data_from_db'),
    path('store_data/', views.store_data, name='store_data'),


]
