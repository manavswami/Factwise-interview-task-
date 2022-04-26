from ast import Or
import sys
from factwise_python import project_board_base
import shortuuid
import pandas as pd 
import json 
import datetime
import os
directory = os.getcwd()
class ProjectBoardBase(project_board_base.ProjectBoardBase):
    # create a board
    def create_board(self, request: str):
        name=request.query_params.get('name')
        description=request.query_params.get('description')
        board_id=shortuuid.uuid()
        team_id=request.query_params.get('team_id')
        creation_time=request.query_params.get('creation_time')
        project_board_base=pd.read_csv(directory+r'\factwise_python\db\project_board_base.csv')
        if name in project_board_base["name"].to_list() or  len(name)>64 or len(description)>128 :
            raise Exception("")
        if (len(project_board_base[(project_board_base['team_id'] == team_id) & ( project_board_base['name'] == name)])<1):
            dict = {"board_id":board_id,'team_id': team_id, 'name': name, 'description': description,'creation_time':creation_time}
            project_board_base = project_board_base.append(dict, ignore_index = True)
            json_object = json.dumps({'team_id': board_id})
            project_board_base.to_csv(directory+r'\factwise_python\db\project_board_base.csv', index=False)
            return(json_object)
        else:
            json_object = json.dumps({'Error': "data alredy present with same  value "}) 
            return(json_object)
    def add_task(self, request: str) -> str:
        title=request.query_params.get('title')
        description=request.query_params.get('description')
        user_id=request.query_params.get('user_id')
        creation_time=request.query_params.get('creation_time')
        project_board_base=pd.read_csv(directory+r'\factwise_python\db\task_id.csv')
        data=project_board_base[project_board_base['title'] == title ]
        if data["status"].to_list()[0]!="OPEN":
            raise Exception("")
        task_id=shortuuid.uuid()
        project_board_base.loc[project_board_base['title'] == title, 'task_id'] = task_id
        project_board_base.loc[project_board_base['title'] == title, 'title'] =title
        project_board_base.loc[project_board_base['title'] == title, 'description'] = description
        project_board_base.loc[project_board_base['title'] == title, 'user_id'] = user_id
        project_board_base.loc[project_board_base['title'] == title, 'end_time'] = datetime.datetime.now()       
        json_object = json.dumps({'task_id': task_id})
        project_board_base.to_csv(directory+r'\factwise_python\db\task_id.csv', index=False)
        return(json_object)

    def update_task_status(self, request: str):
        task_id=request.query_params.get('id')
        status=request.query_params.get('status').upper()
        data=pd.read_csv(directory+r'\factwise_python\db\task_id.csv')
        data.loc[data['task_id'] == task_id, 'status'] = status
        data.to_csv(directory+r'\factwise_python\db\task_id.csv', index=False)

    def list_boards(self, request: str) -> str:
        team_id=request.query_params.get('id')
        data=pd.read_csv(directory+r'\factwise_python\db\project_board_base.csv')
        data=data[data['team_id'] == team_id ]
        json_object =data.to_json(orient='records')
        return(json_object)

    def close_board(self, request: str) -> str:
        board_id=request.query_params.get('id')
        data=pd.read_csv(directory+r'\factwise_python\db\project_board_base.csv')
        data=data[data['board_id'] == board_id ]
        name=data["name"].to_list()[0]
        idd=data["team_id"].to_list()[0]
        taskdata=pd.read_csv(directory+r'\factwise_python\db\task_id.csv')
        data1=taskdata[(taskdata['user_id'] == idd) & ( taskdata['title'] == name)]
        task_id=data1["task_id"].to_list()[0]
        status=data1["status"].to_list()[0]
        if status == "COMPLETE":
            taskdata.loc[taskdata['task_id'] == task_id, 'status'] = "CLOSED"
            taskdata.loc[taskdata['task_id'] == task_id, 'end_time'] = datetime.datetime.now()
        taskdata.to_csv(directory+r'\factwise_python\db\task_id.csv', index=False)
 
    def export_board(self, request: str) -> str:
        board_id=request.query_params.get('id')
        data=pd.read_csv(directory+r'\factwise_python\db\project_board_base.csv')
        data=data[data['board_id'] == board_id ]
        data2=pd.read_csv(directory+r'\factwise_python\db\task_id.csv')
        col=data.columns.to_list() 
        for i in range(len(col)):
            if(col[i]!="team_id"):
                col[i]="project_board_"+col[i]
                
        data.columns=col
        col=data2.columns.to_list() 
        for i in range(len(col)):
            if(col[i]!="user_id"):
                col[i]="task_"+col[i]                
        data2.columns=col
        final=pd.merge(data,data2,left_on='team_id',right_on='user_id')        
        final.to_excel(directory+r"\factwise_python\out\\"+board_id+".xlsx", index=False)
        json_object = json.dumps({'file name': directory+r"\factwise_python\out\\"+board_id+".csv"})
        return(json_object)