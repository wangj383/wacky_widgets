from django.shortcuts import render
from django.views import generic
from .models import Widget
from django.forms import ModelForm


class IndexView(generic.ListView):
    model = Widget
    template_name = 'index.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['widget_list'] = Widget.objects.all()
    #     return context

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']

def index(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            new_widget = form.save()
            new_widget.save()
            context = {'form': WidgetForm(), 'description':new_widget.description, 'quantity':new_widget.quantity}
            return render(request,"index.html", context)
    form = WidgetForm()
    IndexView()
    return render(request,"index.html",{'form':form})


class CreateView(generic.CreateView):
    model = Widget
    fields = ['description', 'quantity']


# def delete(request):


