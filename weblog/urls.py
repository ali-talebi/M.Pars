

from django.urls import path
from .views import TotalPostView , DetailPostView
app_name = 'weblog'
urlpatterns = [
    path('total_post/', TotalPostView.as_view() , name='Total_Post') ,
    path('total_post/<slug:slug_field>/', TotalPostView.as_view(), name='Total_Post'),
    path('detail_post/<int:id>/', DetailPostView.as_view() , name='Detail_Post') ,
]

