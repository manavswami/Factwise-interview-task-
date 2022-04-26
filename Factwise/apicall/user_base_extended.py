import sys
from factwise_python import user_base
import shortuuid
import pandas as pd 
import json 
import datetime
import os
directory = os.getcwd()

class UserBase_extended(user_base.UserBase):
  def create_user(self, request: str) -> str:
    User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
    name=request.query_params.get('name').strip()
    display_name=request.query_params.get('display_name').strip()
    user_id=shortuuid.uuid()
    creation_time = datetime.datetime.now()
    if display_name== "" or name =="" or (name in set(User_Base['name'])) or  len(request.query_params.get('display_name'))>64 or len(request.query_params.get('name'))>64 :
      raise Exception("")
    dict = {'user_id': user_id, 'name': name, 'display_name': display_name,'creation_time':creation_time}
    User_Base = User_Base.append(dict, ignore_index = True)
    json_object = json.dumps({'user_id': user_id})
    User_Base.to_csv(directory+r'\factwise_python\db\User_Base.csv', index=False)
    return(json_object)
      
  def list_users(self) -> str:
    User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
    name=User_Base[['name','display_name','creation_time']]
    json_object =name.to_json(orient='records')
    return(json_object)

  def describe_user(self, request: str) -> str:
    try:
        User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
        user_id=request.query_params.get('id')
        data=User_Base.loc[User_Base['user_id'] == user_id]       
        json_object = json.dumps({'name': list(data["name"])[0],'display_name':list(data["display_name"])[0],'creation_time':list(data["creation_time"])[0]})
        return(json_object)
    except:
        return(json.dumps({'Error': "id not present"}))
  def update_user(self, request: str) -> str:
    User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
    if  len(request.query_params.get('display_name'))>128 :
      raise Exception("")       
    index=User_Base.index[User_Base['user_id'] == request.query_params.get('id')].tolist()[0]
    User_Base[index:index+1]["display_name"]=request.query_params.get('display_name')
    User_Base.to_csv(directory+r'\factwise_python\db\User_Base.csv', index=False)  
    return (json.dumps({'success': "updated record  successfully"}))    

  def get_user_teams(self, request: str) -> str:    
    User_Base=pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
    team_user_id=pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv') 
    Team_Base=pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv') 
    user_id=request.query_params.get('id')
    User_Base=User_Base[User_Base['user_id'] == user_id ]
    teamid=team_user_id[team_user_id['user_id'] == user_id ]["team_id"].to_list()[0]
    teamname=Team_Base[Team_Base['team_id'] == teamid ]
    result=teamname[["team_name","description","creation_time"]]
    json_object =result.to_json(orient='records')
    return(json_object)