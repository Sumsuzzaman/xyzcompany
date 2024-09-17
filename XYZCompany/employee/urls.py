from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
