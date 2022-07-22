from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

from django.shortcuts import render, redirect
from app01 import models


def home(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'main.html')


class MenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"
        # exclude = ["id"]


def list_meun(request):
    """ Menu list """
    data_dict = {}
    # Search function
    search_data = request.GET.get('q', "")

    if search_data:
        data_dict["name__contains"] = search_data




    queryset = models.Menu.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset)

    context = {"search_data": search_data,
               "queryset": page_object.page_queryset,  # 分完页的数据
               "page_string": page_object.html()  # 生成的页码
               }
    return render(request, 'meun_list.html', context)
    # data_dict = {}
    # search_data = request.GET.get('q', "")
    # if search_data:
    #     data_dict["name__contains"] = search_data
    #
    # queryset = models.Menu.objects.filter(**data_dict).order_by("id")
    # # queryset = models.Menu.objects.all().order_by("-id")
    # page_object = Pagination(request, queryset)
    # form = MenuModelForm()
    #
    # context = {
    #     "form": form,
    #     "queryset": page_object.page_queryset,  # 分完页的数据
    #     "page_string": page_object.html()  # 生成的页码
    # }
    # return render(request, 'meun_list.html', context)


def add_meun(request):
    title = "Create menu"
    if request.method == 'GET':
        form = MenuModelForm()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MenuModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():

        form.save()
        return redirect('/meun/list/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


def edit_meun(request, nid):
    """ Edit """
    if request.method == 'GET':
        row_object = models.Menu.objects.filter(id=nid).first()
        form = MenuModelForm(instance=row_object)
        return render(request, 'meun_edit.html', {"form": form})

    row_object = models.Menu.objects.filter(id=nid).first()

    form = MenuModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/meun/list/')
    return render(request, 'meun_edit.html', {"form": form})


def delete_meun(request, nid):
    models.Menu.objects.filter(id=nid).delete()
    return redirect('/meun/list/')
