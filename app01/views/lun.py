from django.shortcuts import render,redirect

def page1(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'det_lun1.html')
def page2(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'det_lun2.html')
def page3(request):
    # info = request.session.get("info")
    # if not info:
    #     return redirect('/login/')
    return render(request, 'det_lun3.html')
