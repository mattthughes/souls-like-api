from django.urls import path
from trending import views

urlpatterns = [
    path('trending/', views.TrendingList.as_view()),
    
]