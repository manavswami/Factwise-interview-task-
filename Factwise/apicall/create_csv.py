import pandas as pd
import os
directory = os.getcwd()
def loadOrCreateCSV():
    try :
        pd.read_csv(directory+r'\factwise_python\db\User_Base.csv')
    except:
        dict = {'user_id':[],'name': [], 'display_name': [],'creation_time':[]} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\User_Base.csv', index=False)
    try :
        pd.read_csv(directory+r'\factwise_python\db\Team_Base.csv')
    except:
        dict = {'team_id':[],'team_name': [], 'description': [],"admin":[],'creation_time':[]} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\Team_Base.csv', index=False)
    try :
        pd.read_csv(directory+r'\factwise_python\db\project_board_base.csv')
    except:
        dict = {"board_id":[],'name': [], 'description': [], 'team_id': [], 'creation_time': []} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\project_board_base.csv', index=False)
    try :
        pd.read_csv(directory+r'\factwise_python\db\team_user_id.csv')
    except:
        dict = {'team_id': [], 'user_id': []} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\team_user_id.csv', index=False)
    try :
        pd.read_csv(directory+r'\factwise_python\db\task_board_id.csv')
    except:
        dict = {'team_id': [], 'user_id': []} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\task_board_id.csv', index=False)
    try :
        pd.read_csv(directory+r'\factwise_python\db\task_id.csv')
    except:
        dict = {'task_id':[],'title': [], 'description': [],'user_id': [], 'creation_time': [],"status":[]} 
        df = pd.DataFrame(dict)
        df.to_csv(directory+r'\factwise_python\db\task_id.csv', index=False)


    