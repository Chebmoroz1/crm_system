from django.urls import path
from .views import cash_expenses_list

urlpatterns = [
    path('cash-expenses/', cash_expenses_list, name='cash_expenses_list'),
]
