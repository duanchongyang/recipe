from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import PrettyModelForm, PrettyEditModelForm

""" 靓号管理 """


def pretty_list(request):
    """ 靓号列表 """
    """ 搜索 """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')

    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset)

    context = {"search_data": search_data,
               "queryset": page_object.page_queryset,  # 分完页的数据
               "page_string": page_object.html()  # 生成的页码
               }
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    """ 新建靓号 """
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # models.UserInfo.objects.create()
        form.save()
        return redirect("/pretty/list")
    # 校验信息（在页面上显示错误信息）
    return render(request, 'pretty_add.html', {"form": form})


def pretty_edit(request, nid):
    """ 编辑靓号 """
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        # 根据ID去数据库获取要编辑的那一行数据(对象）
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list')
