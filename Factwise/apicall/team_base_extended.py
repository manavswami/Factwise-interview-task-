import sys
from factwise_python import team_base
import shortuuid
import pandas as pd 
import json 
import datetime
from rest_framework.response import Response
from rest_framework import status
import os
directory = os.getcwd()

class TeamBase_extended(team_base.TeamBase):
    def create_team(self, request: str) -> str:
        Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')
        team_user_id=pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv')
        team_name=request.query_params.get('name').strip()      
        if team_name  in set(Team_Base['team_name']):
            return ( {'Error': " name is already present in team_name "})
        if team_name=="":
            raise  Exception("team name can not be null")
        admin=request.query_params.get('admin')
        team_id=shortuuid.uuid()
        creation_time = datetime.datetime.now()
        description=request.query_params.get("description")
        dict = {'team_id': team_id, 'team_name': team_name,'description':description, 'admin':admin, 'creation_time':creation_time}
        dict2={'team_id': team_id,"user_id":admin}
        Team_Base = Team_Base.append(dict, ignore_index = True)
        team_user_id=team_user_id.append(dict2, ignore_index = True)
        json_object = json.dumps({'id': team_id})
        Team_Base.to_csv(directory+r'\factwise_python\db\Team_Base.csv', index=False)
        team_user_id.to_csv(directory+r'\factwise_python\db\team_user_id.csv', index=False)
        return(json_object)

    # list all teams
    def list_teams(self) -> str:      
        Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')
        name=Team_Base[['team_name',"description",'creation_time',"admin"]]
        json_object =name.to_json(orient='records')
        return(json_object)
    
    def list_team_users(self, request: str):        
        try:
            Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')            
            team_id=request.query_params.get('id')
            data=Team_Base.loc[Team_Base['team_id'] == team_id]
            json_object=json.dumps({'Error': "no data" })
            if len(data)>0:
                json_object = json.dumps({'id': list(data["admin"])[0],'team_name':list(data["team_name"])[0],'admin':list(data["admin"])[0]})
            return(json_object)
        except:
            return(json.dumps({'Error': "id not present"}))

    def add_users_to_team(self, request: str):
        team_id=request.query_params.get('id')
        users=set(request.query_params.get('users').split(","))
        team_user_id=pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv')
        filterdata=team_user_id.loc[team_user_id['team_id'] == team_id]
        length=len(filterdata)
        if length>=50:
            return json.dumps({'Error': "max len limit reach" })
        olduser=filterdata["user_id"].to_list()
        for user in users:
            if user not in olduser and length<50 and user.strip()!="":
                dict={'team_id': team_id,"user_id":user}
                team_user_id = team_user_id.append(dict, ignore_index = True)
                length+=1
        team_user_id.to_csv(directory+r'\factwise_python\db\team_user_id.csv', index=False)    
        json_object=json.dumps({'sucess': "data enter" })
        return json_object

    def remove_users_from_team(self, request: str):
        team_id=request.query_params.get('id')
        users=set(request.query_params.get('users').split(","))
        team_user_id=pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv')
        for user in users:            
            team_user_id.drop(team_user_id[(team_user_id['team_id'] == team_id) &  (team_user_id['user_id'] == user)].index, inplace=True)
        team_user_id.to_csv(directory+r'\factwise_python\db\team_user_id.csv', index=False)    
        json_object=json.dumps({'sucess': "data deleted " })
        return json_object

    def list_team_users(self, request: str):
        team_id=request.query_params.get('id')
        team_user_id=pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv')
        User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
        team_user_id=team_user_id[(team_user_id["team_id"]==team_id) ]  
        filter_data=pd.merge(User_Base,team_user_id,left_on='user_id',right_on='user_id')
        name=filter_data[["user_id","name","display_name"]]
        json_object =name.to_json(orient='records')
        return json_object
   
    def update_team(self, request: str) -> str:
        Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')
        team_id=request.query_params.get('id')
        filter=Team_Base[Team_Base['team_id'] == team_id ]
        if len(filter)>0:
            filter=filter["team_name"].to_list()[0]
        if request.query_params.get('name').strip()  in set(Team_Base['team_name']) and (filter!=request.query_params.get('name')):
            return ( {'Error': " name is already present in team_name "})
        if request.query_params.get('name'):
            Team_Base.loc[Team_Base['team_id'] == team_id, 'team_name'] = request.query_params.get('name').strip()
        if request.query_params.get('description'):
            Team_Base.loc[Team_Base['team_id'] == team_id, 'description'] = request.query_params.get('description').strip()
        if request.query_params.get('admin'):
            Team_Base.loc[Team_Base['team_id'] == team_id, 'admin'] = request.query_params.get('admin').strip()
        json_object=json.dumps({'sucess': "data updated " })
        Team_Base.to_csv(directory+r'\factwise_python\db\Team_Base.csv', index=False) 
        return json_object

    def describe_team(self, request: str) -> str:
        Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')
        team_id=request.query_params.get('id')
        Team_Base=Team_Base[Team_Base['team_id'] == team_id ]
        name=Team_Base[["team_name","description","creation_time","admin"]]
        json_object =name.to_json(orient='records')
        return json_object

