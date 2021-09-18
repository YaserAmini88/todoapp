from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TodoList

def index(request):
    # Retrieve objects from db - By 'id' order
    todo_items = TodoList.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(request, 'base/index.html', context)
