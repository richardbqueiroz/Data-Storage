from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from app import views

urlpatterns = [
    # Admin com Django Admin
    path('admin/', admin.site.urls),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # API
    path('api/v1/', include('authentication.urls')),

    # Aplicações do sistema
    path('users/', include('users.urls')),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('inflows/', include('inflows.urls')),
    path('outflows/', include('outflows.urls')),
    path('products/', include('products.urls')),
    path('reports/', include('reports.urls')),

    # Página inicial e Termos de Uso
    path('', views.home, name='home'),
    path('terms_use/', views.terms_use, name='terms_use'),
]
