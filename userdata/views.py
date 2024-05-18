from django.shortcuts import render
from userlog.models import *

# Create your views here.
def index(request):
    data = user_details.objects.all()
    context = {'data': data}
    return render(request, "index.html",context)