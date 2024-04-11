from django.urls import path
from .views import Event_DetailView , EventListView




app_name = 'Event'
urlpatterns = [

    path('Events/<int:id>/', Event_DetailView.as_view() , name='Event_Detail' ) ,
    path('Events_list/', EventListView.as_view(), name='event_list'),
    path('Events_list/<int:page>/' , EventListView.as_view() , name='event_list' ) ,




]