"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path       #新版普通路由用path ；要写正则用re_path
from t01.views import index,my_html,get_data        #导入的是viesw中的函数名字

urlpatterns = [
    #不写正则用path，简单一些，如果遇到复杂的路径要用正则的话，就用re_path

    # re_path写法【亲测成功】
    # re_path(r'^admin/$', admin.site.urls),
    # re_path(r'^hello/$',index)

    #path写法【亲测成功】
    path('admin/', admin.site.urls),
    path("hello/", index),  # hello是访问的时候网址上要输入的，根据输入的hello，找views中对应的index函数来响应这个网址
    path("index/",my_html),
    path("get_data/",get_data)





]
