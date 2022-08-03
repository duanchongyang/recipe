from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

from django.shortcuts import render, redirect, HttpResponse
from app01 import models


class MenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.home
        fields = "__all__"
        # exclude = ["id"]




def meun_list(request, nid):
    queryset = models.home.objects.filter(id=nid)
    tools = int(request.POST.get("tools"))
    print(tools)
    return render(request, 'sec_menu.html', {"queryset": queryset, "tools": tools})


def meun_list1(request, nid):
    queryset = models.cust_recipe.objects.filter(id=nid)
    tools = int(request.POST.get("toolss"))
    print(tools)
    return render(request, 'sec_menu1.html', {"queryset": queryset, "tools": tools})
