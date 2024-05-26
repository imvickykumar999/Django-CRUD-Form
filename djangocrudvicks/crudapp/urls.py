from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', list_view, name='list_view'),
    path('create/', create_view, name='create_view'),
    path('<int:id>/', detail_view, name='detail_view'),
    path('<int:id>/update/', update_view, name='update_view'),
    path('<int:id>/delete/', delete_view, name='delete_view'),
]

# Custom handler for 404 errors
handler404 = 'crudapp.views.custom_404_view'
