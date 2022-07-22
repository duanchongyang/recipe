from django.shortcuts import render,redirect


def page1(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'Ingre.html')
