from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
QuanTypes = [
    (0,"心情日记"),
    (1,"作文杂谈"),
    (2,"学习资料"),
    (3,"社团活动"),
    (4,"兴趣爱好"),
    (5,"吐槽"),
    (6,"学习互助社"),
    (7,"二手转让"),
]

class Quan(models.Model):
    quan_type = models.SmallIntegerField(blank=False, choices=QuanTypes, verbose_name="文章类型")
    quan_title = models.CharField(max_length=30, blank=False, verbose_name=("文章标题"))
    quan_content = models.TextField(max_length=800,null=False, blank=False, verbose_name=("文章内容或链接"))
    quan_tag = models.CharField(max_length=8, blank=True, verbose_name=("标签：建议#开头"))
    quan_pic  = models.CharField(max_length=80, blank=True, verbose_name=("引用图片链接"))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=('上传照片'))
    quan_star = models.IntegerField(null=True, default=0)
    quan_read = models.IntegerField(null=True, default=0)
    #pickup = models.BooleanField(null=True, default=False, verbose_name=("首页精华"))
    quan_creator = models.ForeignKey(User, verbose_name=("作者"), null=True, on_delete=models.SET_NULL)
    quan_created_date = models.DateTimeField(verbose_name=("创建日期"), auto_now_add=True)

"""
#user类能否直接改扩数据库中，系统user的表？
class User(models.Model):
   class_choices = (
        (0, "大关董家706"),
        (1, "北大地球物理（球系）"),
    )
    name = models.CharField(max_length=32, verbose_name=("用户名"))
    niname = models.CharField(max_length=32, blank=True, verbose_name=("用户昵称笔名"))
    class = models.SmallIntegerField(choices=class_choices, verbose_name=("学校班级代码"))
    user_detail = models.OneToOneField("UserDetail", on_delete=models.CASCADE)
"""
class UserDetail(models.Model):
    gender_choices = (
        (0, "女生"),
        (1, "男生"),
    )
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name=("性别"))
    birthday = models.DateField(verbose_name=("生日"))
    xuehao = models.SmallIntegerField(verbose_name=("学号"))
    tel = models.CharField(max_length=32, verbose_name=("手机号"))
    addr = models.CharField(max_length=64, verbose_name=("家庭住址"))
    weichat = models.CharField(max_length=64, verbose_name=("微信号"))
    email = models.EmailField()
    aboutme = models.CharField(max_length=64, verbose_name=("个人介绍"))
    avatar = models.CharField(max_length=64, verbose_name=("头像图片代码"))
    remarks = models.CharField(max_length=64, verbose_name=("备注"))
    ideal = models.CharField(max_length=64, verbose_name=("理想"))
    mood = models.CharField(max_length=64, verbose_name=("心情签名"))

"""
class upgrade(models.Model):
     profession_choices = (
        (0, "学习"),
        (1, "才艺"),
        (2, "交际魅力"),
        (3, "信誉声望"),
    )
    profession = models.SmallIntegerField(choices= profession_choices, verbose_name=("职业"))
    level = models.SmallIntegerField(verbose_name=("级别"))
    experience = models.SmallIntegerField(verbose_name=("经验值"))
    contribution = models.SmallIntegerField(verbose_name=("贡献值"))
    coin = models.SmallIntegerField(verbose_name=("金币"))
    class_leader = models.CharField(max_length=32, verbose_name=("班干部"))
    award1  = models.CharField(max_length=32, verbose_name=("省市区奖称号1"))
    award2  = models.CharField(max_length=32, verbose_name=("省市区奖称号2"))
    tasks = models.CharField(max_length=64, verbose_name=("任务"))
 
"""