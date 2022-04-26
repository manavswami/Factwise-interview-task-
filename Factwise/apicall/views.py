from msilib.schema import Error
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import sys
import os
import json 
#to get the current working directory
directory = os.getcwd()
from apicall import create_csv
# from create_csv import *
create_csv.loadOrCreateCSV()
from apicall import user_base_extended,team_base_extended,project_board_base_extended

# user_base_extended.UserBase_extended()
    




class get_user_teams_api(APIView,user_base_extended.UserBase_extended):
    def get(self, request):
        try:
            return Response(user_base_extended.UserBase_extended.get_user_teams(self,request), status=status.HTTP_200_OK)
        except:
            return Response({'Error': "no data"}, status=status.HTTP_428_PRECONDITION_REQUIRED)

class UserBaseapi(APIView,user_base_extended.UserBase_extended):
    def get(self, request):
        
        if request.query_params.get("id") :
            return Response(user_base_extended.UserBase_extended.describe_user(self,request), status=status.HTTP_200_OK)
        else:
            return Response(user_base_extended.UserBase_extended.list_users(self), status=status.HTTP_200_OK)

    def post(self, request):
        try:
            output=user_base_extended.UserBase_extended.create_user(self,request)
            return Response(output, status=status.HTTP_201_CREATED)
        except:
            return Response({'Error': "user name must be unique m,name can be max 64 characters and display name can be max 64 characters"}, status=status.HTTP_428_PRECONDITION_REQUIRED)
    def put(self, request):
        try:
            return Response(user_base_extended.UserBase_extended.describe_user(self,request), status=status.HTTP_200_OK)
        except:
            return Response({'Error': "name can be max 64 characters and display name can be max 64 characters"}, status=status.HTTP_428_PRECONDITION_REQUIRED)

class TeamBaseapi(APIView,team_base_extended.TeamBase_extended):
    def get(self, request):
        if request.query_params.get("id") :
            return Response(team_base_extended.TeamBase_extended.describe_team(self,request), status=status.HTTP_200_OK)
        else:   
            return Response(team_base_extended.TeamBase_extended.list_teams(self), status=status.HTTP_200_OK)

    def post(self, request):
        try:          
            if len(request.query_params.get('description'))>64 or len(request.query_params.get('name'))>64:
                return Response({'Error': " description length  should be smaller than 64 "}, status=status.HTTP_428_PRECONDITION_REQUIRED)
            output=team_base_extended.TeamBase_extended.create_team(self,request)
            return Response(output, status=status.HTTP_200_OK)
        except:
            return Response({'Error': "team name can not be null"}, status=status.HTTP_428_PRECONDITION_REQUIRED)
    def put(self, request):
        try:
            if request.query_params.get('name'):
                if len(request.query_params.get('name'))>64:
                    return Response({'Error': " name should be less than 64"}, status=status.HTTP_428_PRECONDITION_REQUIRED)
            if request.query_params.get('display_name'):
                if len(request.query_params.get('Description'))>128:
                    return Response({'Error': " Description length  should be smaller than 128 "}, status=status.HTTP_428_PRECONDITION_REQUIRED)
            return Response(team_base_extended.TeamBase_extended.update_team(self,request), status=status.HTTP_200_OK)
        except:
            return Response({'Error': "key value error"}, status=status.HTTP_428_PRECONDITION_REQUIRED)

class add_users_to_team_api(APIView,team_base_extended.TeamBase_extended):
    def post(self, request):
        
        if "id" in request.query_params:
            return Response(team_base_extended.TeamBase_extended.add_users_to_team(self,request), status=status.HTTP_200_OK)
        else:   
            return Response({"Error in passing key value "}, status=status.HTTP_200_OK)

class remove_users_to_team_api(APIView,team_base_extended.TeamBase_extended):
    def post(self, request):
        if "id" in request.query_params:
            return Response(team_base_extended.TeamBase_extended.remove_users_from_team(self,request), status=status.HTTP_404_NOT_FOUND)
        else:   
            return Response({"Error in passing key value"}, status=status.HTTP_200_OK)

class list_team_users_api(APIView,team_base_extended.TeamBase_extended):    
    def get(self, request):
        if "id" in request.data:
            return Response(team_base_extended.TeamBase_extended.list_team_users(self,request), status=status.HTTP_404_NOT_FOUND)
        else:   
            return Response(team_base_extended.TeamBase_extended.list_team_users(self,request), status=status.HTTP_404_NOT_FOUND)

class board_base_api(APIView,project_board_base_extended.ProjectBoardBase):
    def post(self, request):
        try:
            if len(request.query_params.get('description'))>128 or len(request.query_params.get('name'))>64:
                return Response({'Error': " description length  should be smaller than 128 and  board name should b smaller than 64 "}, status=status.HTTP_428_PRECONDITION_REQUIRED)
            return Response(project_board_base_extended.ProjectBoardBase.create_board(self,request), status=status.HTTP_200_OK)
        except:
            json_object = json.dumps({'Error': "Constraint: board name must be unique for a team board ,name can be max 64 characters AND description can be max 128 characters" }) 
             
            return Response(json_object, status=status.HTTP_428_PRECONDITION_REQUIRED)

class add_task_api(APIView,project_board_base_extended.ProjectBoardBase):
    def post(self, request):
        try:
            if request.query_params.get('title') and request.query_params.get('user_id') and request.query_params.get('description')and request.query_params.get('creation_time'):
                if len(request.query_params.get('description'))>128 or len(request.query_params.get('title'))>64:
                    return Response({'Error': " description length  should be smaller than 128 and  board name should b smaller than 64 "}, status=status.HTTP_428_PRECONDITION_REQUIRED)
                return Response(project_board_base_extended.ProjectBoardBase.add_task(self,request), status=status.HTTP_200_OK)
            else:
                Response({"ERROR  : provide all required param"}, status=status.HTTP_200_OK)
        except:   
            return Response({"ERROR  : Status not Open"}, status=status.HTTP_200_OK)

class update_task_status_api(APIView,project_board_base_extended.ProjectBoardBase):
    def post(self, request):
        try:
            return Response(project_board_base_extended.ProjectBoardBase.update_task_status(self,request), status=status.HTTP_200_OK)
        except:
            return Response({"ERROR  : provide all required param"}, status=status.HTTP_404_NOT_FOUND)

class list_boards_api(APIView,project_board_base_extended.ProjectBoardBase):
    def get(self, request):
        try:        
            return Response(project_board_base_extended.ProjectBoardBase.list_boards(self,request), status=status.HTTP_200_OK)
        except:
            return Response({"ERROR  : provide all required param"}, status=status.HTTP_404_NOT_FOUND)

class close_board_api(APIView,project_board_base_extended.ProjectBoardBase):
    def post(self, request):
        try:
            return Response(project_board_base_extended.ProjectBoardBase.close_board(self,request), status=status.HTTP_200_OK)
        except:
            return Response({"ERROR  : provide all required param"}, status=status.HTTP_404_NOT_FOUND)


class export_board_api(APIView,project_board_base_extended.ProjectBoardBase):
    def post(self, request):
        try:
            return Response(project_board_base_extended.ProjectBoardBase.export_board(self,request), status=status.HTTP_200_OK)
        except:
            return Response({"ERROR  : provide all required param"}, status=status.HTTP_404_NOT_FOUND)