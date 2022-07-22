from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django.views.decorators.csrf import csrf_exempt
import json
import random
from datetime import datetime
from app01.utils.pagination import Pagination

datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


def order_list(request):
    """ 订单列表 """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    queryset = models.Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """ 创建订单 ajax """
    form = OrderModelForm(data=request.POST)
    # 成功
    if form.is_valid():
        # title=? price=? status=? admin_id=?
        # {'title': '23', 'price': 31212, 'status': 1, 'admin': <Admin: eric>}
        # no oid, 当用户输入的值不够我们填写数据库时，我们可以输入一些不是用户输入的值，可以写成 form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # print(form.cleaned_data)
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 设置管理员ID，去哪里获取呢?去Session中获取。
        form.instance.admin_id = request.session["info"]["id"]

        # 保存到数据库中
        form.save()
        return JsonResponse({"status": True})
        # return HttpResponse(json.dumps({"status": True}))

    # 失败
    return JsonResponse({"status": False, "error": form.errors})


# get 请求不需要crsf认证
def order_delete(request):
    """ 删除订单 """
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败,数据不存在"})

    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    """ 根据ID获取订单详细 """
    # 方式1
    """
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "error": "数据不存在"})
    # 从数据库获取到一个对象 row_object
    result = {
        "status": True,
        "data": {
            "title": row_object.title,
            "price": row_object.price,
            "status": row_object.status,

        }

    }
    return JsonResponse({"status": True, "data": result}) 
    """

    # 方式2
    uid = request.GET.get("uid")
    row_dict = models.Order.objects.filter(id=uid).values("title", "price", "status").first()

    # {'title': '饺子', 'price': 15, 'status': 1}
    # print(row_dict)
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
        # 从数据库获取到一个对象 row_object
    result = {
        "status": True,
        "data": row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """ 编辑订单 """
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在,请重试"})
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
