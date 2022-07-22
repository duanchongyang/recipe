from django.db import models


# Create your models here.


class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="Username", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    # 部门表
    # id 是自动生成的，也可以自己写
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="UserName", max_length=32)
    password = models.CharField(verbose_name="Passoword", max_length=64)
    age = models.IntegerField(verbose_name="Age")
    # 一共长为10， 小数占两位, 默认为2
    account = models.DecimalField(verbose_name="Account", max_digits=10, decimal_places=2, default=2)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="Date")
    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 1. 有约束
    # -to ,于那张表关联
    # -to_field 与表中的那一列关联
    # 2.django自动
    # -写的是depart
    # - 生成数据库的列 depart_id
    # 3. 部门表被删除
    # 3.1 级联删除

    depart = models.ForeignKey(verbose_name="Department", to="Department", to_field="id", on_delete=models.CASCADE)
    # 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # 在django中做的约束
    gender_choices = (
        (1, 'Male'),
        (2, 'Female'),
    )

    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_choices)


class PrettyNum(models.Model):
    """ 靓号表 """
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    # 若想要允许参数为空，null=true, blank=True

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.IntegerField(verbose_name="级别", choices=level_choices, default=1)
    # 像是之前class的性别字段。
    status_choices = (
        (1, "已占用"),
        (2, "未占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)


class Task(models.Model):
    """ 测试任务 """
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # on_delete=models.CASCADE 级联删除
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)


class Boss(models.Model):
    """ 老板 """
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="头像", max_length=128)


class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")
    # 本质上数据库是CharField字符串，自动保存数据,upload_to='city'以后这个图片会存在media下的city目录下
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='city')


class Menu(models.Model):
    """ all meun """
    name = models.CharField(verbose_name="Name", max_length=32)
    time = models.IntegerField(verbose_name="time need to be done")
    # 本质上数据库是CharField字符串，自动保存数据,upload_to='city'以后这个图片会存在media下的city目录下
    tem = models.IntegerField(verbose_name="temperature")
    inter = models.CharField(verbose_name="materials needed" , max_length=256)
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='Menu/')
