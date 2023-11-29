# urls.py
from django.urls import path
from .views import create_employee, update_employee, get_all_employees, delete_employee

urlpatterns = [
    path('create_employee/', create_employee, name='create_employee'),
    path('update_employee/<int:emp_id>/', update_employee, name='update_employee'),
    path('get_all_employees/', get_all_employees, name='get_all_employees'),
    path('delete_employee/<int:emp_id>/', delete_employee, name='delete_employee'),
]
