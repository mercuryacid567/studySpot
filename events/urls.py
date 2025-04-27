from django.urls import path
from . import views


urlpatterns = [
    path('', views.study_spots_home, name='events.home'),
    path('create/', views.create_study_event, name='create_study_event'),
    path('join/<int:event_id>/', views.join_study_event, name='join_study_event'),
]
