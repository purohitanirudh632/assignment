from django.urls import path, include
from .views import *
urlpatterns = [
    path("items/ ", get_items ), 
    path("item/<str:id>", get_item),
    path("items/filter_by/<str:lookup>", filter_items)
]