"""员工管理 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import depart, user, pretty, admin, account, task, order, chart, upload, city, main, subpage1, lun, \
    thirdpage, Ingre
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # Main page
    path('main/', main.home),

    path('meun/add/', main.add_meun),
    path('meun/<int:nid>/edit/', main.edit_meun),
    path('meun/<int:nid>/delete/', main.delete_meun),

    path('meun/list/', main.list_meun),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    # Subpage1
    path('subpage1/', subpage1.page),
    path('subpage2/', subpage1.page2),
    path('subpage3/', subpage1.page3),
    path('subpage4/', subpage1.page4),
    path('subpage5/', subpage1.page5),
    path('subpage6/', subpage1.page6),
    path('subpage7/', subpage1.page7),
    path('subpage8/', subpage1.page8),
    path('subpage9/', subpage1.page9),

    # Ingredient
    path('Ingredient/', Ingre.page1),

    # thirdpage
    path('thirdpage1/', thirdpage.page1),
    path('thirdpage2/', thirdpage.page2),
    path('thirdpage3/', thirdpage.page3),
    path('thirdpage4/', thirdpage.page4),
    path('thirdpage5/', thirdpage.page5),
    path('thirdpage6/', thirdpage.page6),
    path('thirdpage7/', thirdpage.page7),
    path('thirdpage8/', thirdpage.page8),
    path('thirdpage9/', thirdpage.page9),
    path('thirdpage10/', thirdpage.page10),
    path('thirdpage11/', thirdpage.page11),
    path('thirdpage12/', thirdpage.page12),
    path('thirdpage13/', thirdpage.page13),
    path('thirdpage14/', thirdpage.page14),
    path('thirdpage15/', thirdpage.page15),
    path('thirdpage16/', thirdpage.page16),
    path('thirdpage17/', thirdpage.page17),
    path('thirdpage18/', thirdpage.page18),
    path('thirdpage19/', thirdpage.page19),
    path('thirdpage20/', thirdpage.page20),
    path('thirdpage21/', thirdpage.page21),
    path('thirdpage22/', thirdpage.page22),
    path('thirdpage23/', thirdpage.page23),
    path('thirdpage24/', thirdpage.page24),

    # lun bo figure
    path('det_lun1/', lun.page1),
    path('det_lun2/', lun.page2),
    path('det_lun3/', lun.page3),

    # 部门管理

    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),

    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi/', depart.depart_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('pretty/list', pretty.pretty_list),
    path('pretty/add', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),


    # register
    path('register/', account.regist),


    # 任务管理
    path('task/list/', task.task_list),  # 学习AJAX
    path('task/ajax/', task.task_ajax),  # 学习AJAX
    path('task/add/', task.task_add),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modal/form/', upload.upload_modal_form),

    # 城市列表
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),

]
