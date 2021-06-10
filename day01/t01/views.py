from django.http import HttpResponse
from django.shortcuts import render  #导入渲染
from .models import Engineer  #从model.py中导入Engineer类
# Create your views here.

def index(req):  #req是request的缩写，是形参，代表请求
    #返回给前端的数据
    return HttpResponse('<h1>django 呵呵哒<h1/>')



#前端页面对应的逻辑处理——干活的函数
def my_html(req):
    #将页面渲染给前端，谁请求我，我就返回给谁
    return render(req,"my_index.html")


#去model.py中拿数据的函数
def get_data(req): #req是请求对象的形参
    #获取数据--相当于select * from 表名
    data= Engineer.objects.all()   # 类名.objects.all() —— 获取这个类中的所有对象
    print("***",data)

    #返回给前端一个页面"my_index.html"和model中的所有数据
    #数据用字典返回，然后赋值给参数context；前端通过key就能获取到data数据
    #return将渲染的整个内容返回给前端；render是渲染，将页面和数据在前端渲染出来
    return render(req,"my_index.html",context={"mydata":data})



