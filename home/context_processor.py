from . models import *
from userprofile.models import *

def company(request):
    cprofile = CompanyProfile.objects.get(pk=1)

    context = {
      'cprofile': cprofile,
    }

    return context 

def dropdown(request):
    dropdown = Type.objects.all()

    context = {
      'dropdown': dropdown,
    }

    return context

def profileavat(request):
    userprof = Customer.objects.get(user__username = request.user.username)

    context = {
        'userprof':userprof
    }

    return context 