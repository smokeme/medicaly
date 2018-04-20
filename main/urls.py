from django.urls import path
from . import views

urlpatterns = [
    path('', views.visit_list, name="visit_list"),
    path('add/patient/', views.add_patient, name="add_patient"),
    path('add/visit/', views.add_visit, name="add_visit"),


#    path('detail/<int:rest_id>/', views.rest_detail, name="rest_detail"),
#
#    path('create/', views.restaurant_create, name='restaurant_create'),
#	path('update/<int:restaurant_id>)/', views.restaurant_update, name="restaurant_update"),
#	path('delete/<int:restaurant_id>)/', views.restaurant_delete, name="restaurant_delete"),
#
#	path('create/item/<int:restaurant_id>)/', views.item_create, name="item_create"),
#	path('update/item/<int:item_id>)/', views.item_update, name="item_update"),
#	path('delete/item/<int:item_id>)/', views.item_delete, name="item_delete"),
]