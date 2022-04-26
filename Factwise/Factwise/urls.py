"""Factwise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apicall import views as apilcallviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userbaseapi/user' , apilcallviews.UserBaseapi.as_view()),
    path('userbaseapi/getuserteams' , apilcallviews.get_user_teams_api.as_view()),
    path('teambaseapi/team' , apilcallviews.TeamBaseapi.as_view()),
    path('teambaseapi/removeuser' , apilcallviews.remove_users_to_team_api.as_view()),
    path('teambaseapi/adduser' , apilcallviews.add_users_to_team_api.as_view()),
    path('teambaseapi/listteamusers' , apilcallviews.list_team_users_api.as_view()),
    path('boardbaseapi/borad' , apilcallviews.board_base_api.as_view()),
    path('boardbaseapi/addtask' , apilcallviews.add_task_api.as_view()),
    path('boardbaseapi/updatetaskstatus' , apilcallviews.update_task_status_api.as_view()),
    path('boardbaseapi/listboardsapi' , apilcallviews.list_boards_api.as_view()),
    path('boardbaseapi/closeboardapi' , apilcallviews.close_board_api.as_view()),
    path('boardbaseapi/exportboardapi' , apilcallviews.export_board_api.as_view()),


]
