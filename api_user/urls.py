from django.urls import path
from . import views

app_name = 'api_user'

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<user_email>', views.UserView.as_view())
]