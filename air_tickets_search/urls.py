from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.flight_list_p, name='flight_list_p'),
    path('d', views.flight_list_d, name='flight_list_d'),
    path('p', views.flight_list_p, name='flight_list_p'),
    path('b', views.flight_list_bought, name='flight_list_bought'),
    #path('init', views.flight_search, name='flight_search'),
    path('flight/new/', views.flight_new, name='flight_new'),
    path('flight/<int:fl>/', views.flight_detail, name='flight_detail'),
    #path('sign-in/', LoginPage.as_view(), name='sign-in'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    url('edit/', views.edit, name='edit'),
    #path('admin/', include(admin.site.urls)),
    #path('account/', include('account.urls')),
    #path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)