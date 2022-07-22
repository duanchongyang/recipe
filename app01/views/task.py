from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from django import forms
from django.forms.utils import ErrorDict
from app01.utils.pagination import Pagination


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea,
            "detail": forms.TextInput,
        }


def task_list(request):
    """ 任务列表 """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    # 去数据库获取所有的任务
    queryset = models.Task.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = TaskModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

    return render(request, 'take_list.html', context)


# 免除csrf认证
@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    return HttpResponse(json.dumps(data_dict))
    # return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    # < QueryDict: {'level': ['1'], 'title': ['222'], 'detail': ['1212'], 'user': ['11']} >
    # print(request.POST)
    # 1. 用户发送过来的数据进行校验（ModelForm进行验证）
    form = TaskModelForm(data=request.POST)
    # AJAX
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    # 验证失败,ErrorDict
    # print(type(form.errors))
    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
