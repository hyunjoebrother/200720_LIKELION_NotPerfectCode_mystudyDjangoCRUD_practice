"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import myapp.views #myapp 폴더 안에 views.py 불러오라고 선언

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', myapp.views.blog, name='blog'), #함수 안에 path함수로 연결해준다. url과 views 1ㄷ1 연결! 

    path('new/',myapp.views.new, name='new'),
    path('create/',myapp.views.create, name='create'),

    path('detail/<int:blog_id>', myapp.views.detail, name='detail'),
]
