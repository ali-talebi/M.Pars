from django.urls import path
from .views import Course_Detail_View
app_name = 'course'
urlpatterns = [
    path('course/<int:id>/', Course_Detail_View.as_view() , name='course_detail') ,
]