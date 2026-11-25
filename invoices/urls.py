from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('create/', views.invoice_create, name='invoice_create'),
    path('update/<int:pk/>', views.invoice_update, name='invoice_update'),
    # path('add/', views.add_invoice, name='add_invoice'),
]
