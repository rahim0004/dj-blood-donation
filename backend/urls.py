"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="index"),
    path('donors/', views.DonorsListView.as_view(), name="all_donors"),
    path('search/', views.SearchView.as_view(), name="search"),
    path('about/', views.AboutUsView.as_view(), name="about"),
    path('signup/', views.UserSignUpView.as_view(), name="signup"),
    path('signin/', views.UserSignInView.as_view(), name="signin"),
    path('profile/', views.ProfileUpdateView.as_view(), name="profile"),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('delete-account', views.DeleteAccountView.as_view(), name='delete_account'),
    path('logout/', views.user_logout, name="logout"),
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

