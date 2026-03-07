from django.urls import path
from pages import views  # Import the views from the pages app

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),
    
    path('contact/', views.contact_me_view, name='contact_me'),
]
