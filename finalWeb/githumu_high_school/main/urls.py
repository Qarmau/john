from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('administration/', views.administration, name='administration'),
    path('teaching-staff/', views.teaching_staff, name='teaching_staff'),
    path('achievements/', views.achievements, name='achievements'),
    path('holiday-assignments/', views.holiday_assignments, name='holiday_assignments'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
] 