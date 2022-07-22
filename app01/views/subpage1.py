from app01.utils.pagination import Pagination
from openpyxl import load_workbook
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django.views.decorators.csrf import csrf_exempt


def page(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'subpage1.html')


def page2(request):
    return render(request, 'subpage2.html')


def page3(request):
    return render(request, 'subpage3.html')


def page4(request):
    return render(request, 'subpage4.html')


def page5(request):
    return render(request, 'subpage5.html')


def page6(request):
    return render(request, 'subpage6.html')


def page7(request):
    return render(request, 'subpage7.html')

def page8(request):
    return render(request, 'subpage8.html')


def page9(request):
    return render(request, 'subpage9.html')
