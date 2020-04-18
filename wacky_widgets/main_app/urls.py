from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_widget, name='create_widget'),
    path('<int:widget_id>delete/',views.delete_widget,name='delete_widget')
]
