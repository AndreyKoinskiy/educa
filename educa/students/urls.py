from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentRegistartionView.as_view(), name='student_registration')

    ]