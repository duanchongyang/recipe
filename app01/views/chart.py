from django.shortcuts import render,redirect
from django.http import JsonResponse


def chart_list(request):
    """ 数据统计页面 """
    info = request.session.get("info")
    if not info:
        return redirect('/login/')
    return render(request, 'chart_list.html')


def chart_bar(request):
    """ 构造柱状图的数据 """
    # 这些数据可以从数据库中获取
    legend = ["段重阳", "荆雨萌"]
    series_list = [
        {
            "name": '段重阳',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": '荆雨萌',
            "type": 'bar',
            "data": [15, 20, 36, 12, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    result = {
        "status": True,
        "data": {
            'legend': legend,
            "series_list": series_list,
            "x_axis": x_axis,

        }
    }
    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼图的数据 """

    db_data_list = [
        {"value": 2048, "name": 'IT部门'},
        {"value": 335, "name": '运营'},
        {"value": 480, "name": '新媒体'},

    ]

    result = {
        "status": True,
        "data": db_data_list,
    }

    return JsonResponse(result)


def chart_line(request):
    """ 构造线图的数据 """
    # 这些数据可以从数据库中获取
    legends = ["上海", "沈阳"]
    series_list = [
        {
            "name": '段重阳',
            "type": 'line',
            "stack": "Total",
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": '荆雨萌',
            "type": 'line',
            "stack": "Total",
            "data": [15, 20, 36, 12, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
    result = {
        "status": True,
        "data": {
            "legend": legends,
            "series_list": series_list,
            "x_axis": x_axis,

        }
    }
    return JsonResponse(result)
