
from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .views import custom_login_view
from .views import register

urlpatterns = [
    path('', list_view, name='list_view'),
    path('create/', create_view, name='create_view'),
    path('<int:id>/', detail_view, name='detail_view'),
    path('<int:id>/update/', update_view, name='update_view'),
    path('<int:id>/delete/', delete_view, name='delete_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='list_view'), name='logout'),
    path('register/', register, name='register'),
]

# Custom handler for 404 errors
handler404 = 'crudapp.views.custom_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
