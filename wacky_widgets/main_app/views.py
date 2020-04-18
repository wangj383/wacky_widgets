from django.shortcuts import render,redirect
from django.views import generic
from .models import Widget
from django.forms import ModelForm

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
    
def index(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    return render(request,"index.html",{'form':form, 'widgets': widgets})

def create_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("index")

def delete_widget(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')



