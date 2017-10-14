from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

#from .models import pos #db모델 정보 import


class IndexView(generic.ListView):
    template_name = 'canvas/index.html'
    context_object_name = 'pos_list'

    def get_queryset(self):
#       return pos.objects.all().order_by('-timestamp')
'''
    class CanvasView(generic.DetailView):
    template_name = 'canvas/map.html'
    context_object_name = 'pos_list'

    def get_object(self):
        return pos.objects.all().order_by('-timestamp')
'''

