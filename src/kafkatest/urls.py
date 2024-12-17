from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index),
    path('test-order-sending', views.test_send_order),
    path('test-order-processing', views.test_process_orders)
]
