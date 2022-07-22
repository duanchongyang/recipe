from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
import os
from app01 import models
from django.conf import settings
from app01.utils.bootstrap import BootStrapModelForm, BootStrap


@csrf_exempt
def upload_list(request):
    """ 文件的上传 """
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    if request.method == "GET":
        return render(request, 'upload_list.html')

    # print(request.POST)
    # # <QueryDict: {'username': ['123'], 'avatar': ['logo.jpeg'], '提交': ['Submit']}>
    # # < QueryDict: {'username': ['123'], '提交': ['Submit']} >
    # # < MultiValueDict: {'avatar': [ < InMemoryUploadedFile: logo.jpeg(image / jpeg) >]} >
    # print(request.FILES)
    file_object = request.FILES.get("avatar")
    # logo.jpeg，上传的文件名字
    # print(file_object.name)

    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("hhhhhhh")


from django import forms
from app01.utils.bootstrap import BootStrapForm


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})

    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # {'name': '李晗', 'age': 25, 'img': <InMemoryUploadedFile: logo.jpeg (image/jpeg)>}
        # print(form.cleaned_data)
        # 读取到内容自己处理每个字段的数据
        # 1. 读取图片内容，写入到文件夹中，写的过程中，获取文件的路径
        image_object = form.cleaned_data.get("img")
        # media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)
        media_path = os.path.join("media", image_object.name)
        f = open(media_path, mode='wb')
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 2. 把图片的路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data["name"],
            age=form.cleaned_data["age"],
            img=media_path,
        )
        return HttpResponse("...")

    return render(request, 'upload_form.html', {"form": form, "title": title})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def upload_modal_form(request):
    """ 上传文件数据基于ModalForm """
    title = "ModelForm上传文件"
    if request.method == 'GET':
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = UpModelForm(data=request.POST, files = request.FILES)
    if form.is_valid():
        # 自动保存在media文件夹中，并且把上传的路径写入到数据库中
        form.save()
        return HttpResponse("上传成功")
    return render(request, 'upload_form.html', {"form": form, "title": title})
