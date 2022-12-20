from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Servers
from django.views.generic import DetailView

@login_required
def index(request):
    laserv = Servers.objects.order_by('-id')
    return render(request, 'laservers/laservers.html', {'laserv': laserv})


class onebyone(DetailView):
    model = Servers
    template_name = 'laservers/onebyone.html'
    context_object_name = 'server'


