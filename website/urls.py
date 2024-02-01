from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('about/', views.about, name='about'),
    
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('leads/new/', views.lead_create, name='lead_create'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunities/<int:pk>/', views.opportunity_detail, name='opportunity_detail'),
    path('opportunities/new/', views.opportunity_create, name='opportunity_create'),
]
