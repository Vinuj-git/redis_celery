from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse
from sendmail.tasks import notification
# Create your vie:ws here..
def test(request):
    notification.delay()
    return HttpResponse("django home")