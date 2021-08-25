from django.urls import path
from .views import index,register,AdminDash,ProfileView,Catalogue
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('userdash/', AdminDash.as_view(), name='userdash'),
    path('catalogue/', Catalogue.as_view(), name='catalogue'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
