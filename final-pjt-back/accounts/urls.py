from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_pk>/', views.profile_detail),
    # path('check/<int:user_pk>', views.check)
]