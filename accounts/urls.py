


from django.urls import path
from .views import RegisterView , VerifyCodeView , TeamProfileView , LoginView , LogoutView
app_name = 'account'
urlpatterns = [
    path('user_register/' , RegisterView.as_view(), name='user_register'   )  ,
    path('verify_code/'   , VerifyCodeView.as_view(), name='verify_code'   )  ,
    path('team_profile/<int:id>/' , TeamProfileView.as_view(), name='team_profile') ,
    path('login/' , LoginView.as_view(), name='login') ,
    path('logout/' , LogoutView.as_view(), name='logout') ,
]