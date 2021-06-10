from django.db import models

# Create your models here.

#类名就相当于创建数据库的表名
#创建数据表
class Engineer(models.Model):

    #name字段
    name=models.CharField(    #字符串类型 CharField
        max_length=30,        #30位
        verbose_name="名字"  #提示该字段是什么意思
    )


    #age字段
    age=models.IntegerField(  #整数类型 IntegerField
        default=18   #默认值
    )

    #这里就有两个字段了

    #这里添加重写函数，打印的时候可以显示出名字，在Models.py中添加内置函数不用迁移
    def __str__(self):
        return self.name



#创建新的数据表Cart
#车的model
class Cart(models.Model):
    #字段name
    name = models.CharField(
        max_length=30
    )

    #字段color
    color=models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name




#司机的数据表
class Siji(models.Model):
    name=models.CharField(
        max_length=30
    )

    #添加外键，和谁有关系，就指定对应的类名
    #一个司机可以对应多个车
    cart=models.ForeignKey(
        Cart,                  #关联谁，就指定对应的类名
        on_delete="CASCADE",  #在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
        verbose_name="车"
    )


    def __str__(self):
        return self.name



