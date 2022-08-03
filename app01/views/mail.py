from django.shortcuts import HttpResponse
from django.core.mail import send_mail


def sendmail(request):
    """ send email """
    send_mail(subject='This is for practice',
              message='Hi, I am testing if the codes work！',
              from_email='jingyumengdcy@126.com',  # The sender's email
              recipient_list=['Yu.Meng.Jing@ibm.com'],  # The receiver's email
              fail_silently=False)

    return HttpResponse("Send successfully!")
