from django.urls import path
from . import views

urlpatterns = [
    path('mine/',views.ManageCourseListView.as_view(),name = 'manage_course_list'),
    path('create/<pk>',views.CourseCreateView.as_view(),name='course_edit'),
    path('<pk>/delete/',views.CourseDeleteView.as_view(),name='course_delete'),
    #path('<pk>/module/',views.CourseModuleUpdateView.as_view(),name='course_module_update'),
]