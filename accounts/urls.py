


from django.urls import path
from .views import RegisterView , VerifyCodeView , TeamProfileView
app_name = 'account'
urlpatterns = [
    path('user_register/' , RegisterView.as_view(), name='user_register'   )  ,
    path('verify_code/'   , VerifyCodeView.as_view(), name='verify_code'   )  ,
    path('team_profile/<int:id>/' , TeamProfileView.as_view(), name='team_profile')
]