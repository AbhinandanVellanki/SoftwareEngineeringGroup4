from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from util import db_helper

from check_out import check_out_helper
# Create your views here.


def index(request):
    items = ["308932602"]
    shopping_cart = check_out_helper.LinkedList()
    for i in items:
        info = db_helper.get_item_info(i)
        shopping_cart.insert(info[0], info[1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    return render(request, 'task_manager/index.html', context)
