from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('create/', create_view, name='create_view'),
    path('', list_view, name='list_view'),
    path('<id>/', detail_view, name='detail_view'),
    path('<id>/update/', update_view, name='update_view'),
    path('<id>/delete/', delete_view, name='delete_view'),
]
