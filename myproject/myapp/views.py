# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from .forms import MyModelForm

def index(request):
    items = MyModel.objects.all()
    return render(request, 'index.html', {'items': items})

def create(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    return render(request, 'create.html', {'form': form})

def delete(request, pk):
    item = get_object_or_404(MyModel, pk=pk)
    item.delete()
    return redirect('index')
