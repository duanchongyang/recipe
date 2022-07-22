from django.shortcuts import HttpResponse, render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm, BootStrap


def city_list(request):
    """ 城市列表 """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    queryset = models.City.objects.all()

    return render(request, 'city_list.html', {"queryset": queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def city_add(request):
    title = "新建城市"
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 自动保存在media文件夹中，并且把上传的路径写入到数据库中
        form.save()
        return redirect('/city/list/')
    return render(request, 'upload_form.html', {"form": form, "title": title})
