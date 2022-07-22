from django.shortcuts import render, redirect
from app01 import models
from app01.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm
from app01.utils.pagination import Pagination


def user_list(request):
    """ User management """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    # 获取所有用户列表[obj,obj]
    queryset = models.UserInfo.objects.all()

    # 加分页
    page_object = Pagination(request, queryset, page_size=2)
    """
    # 用 Python的语法获取数据
    for obj in queryset:
        print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(),
              obj.depart_id, obj.depart.title)
    # obj.gender # 1 or 2
    # obj.get_gender_display() # 自动根据字段找到对应的文本内容 get_字段名称_display(),django自动提供的
    # print(obj.name, obj.depart_id)
    # obj.depart_id  # 获取 数据库中字段对应的值
    # xx = models.Department.objects.filter(id=obj.depart_id).first()
    # xx.title
    # obj.depart.title  # 根据id自动去关联的表中获取哪一行数据depart对象
    """
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    """ Add user """
    if request.method == 'GET':
        context = {
            'gender_choice': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all(),
        }

        return render(request, "user_add.html", context)
    # 获取用户提交的数据
    user = request.POST.get("name")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("ac")
    create_time = request.POST.get("ctime")
    gender_id = request.POST.get("ge")
    department_id = request.POST.get("dp")
    # 添加到数据库中
    models.UserInfo.objects.create(name=user, password=password,
                                   age=age, account=account, create_time=create_time,
                                   gender=gender_id, depart_id=department_id)
    # 返回到用户列表页面
    return redirect("/user/list/")


def user_model_form_add(request):
    """ Add user，based on ModelForm版本的 """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})
    # 用户POST提交数据，数据的校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # {'name': '123', 'password': '213', 'age': 123, 'account': Decimal('2'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'gender': 1, 'depart': <Department: 媒体企划>}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create()
        form.save()
        return redirect("/user/list/")
    # 校验信息（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


def user_edit(request, nid):
    """ Edit """
    if request.method == 'GET':
        # 根据ID去数据库获取要编辑的那一行数据(对象）
        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})

    row_object = models.UserInfo.objects.filter(id=nid).first()

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据， 如果想要再用户输入意外增加一点值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {"form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
