
In this project I have use Django and Django rest framework, as it is mention i have to use file storage system so i used csv file storage  system 

NOTE : For starting server 
move to the folder "FW\Factwise" 
where you can see manage.py file in this folder which is help in running the server
now open "cmd command prompt" 
and type "python manage.py runserver"
now we will see server will start running 

if we check on chrome browser or any other broser ex: http://127.0.0.1:8000/userbaseapi/getuserteams
then it will show Django rest framework interface face

total number of api=12

these api are for  UserBase.py( all the required param request are explain there with example and which we can use for our reference )
 first api according to  UserBase.py 

 for more reference read view.py file in apicall folder 
  http://127.0.0.1:8000/userbaseapi/user'
  this api have   get,post and put method 
Get method is for retrieving the data
If don’t pass id param the it will give us all the describe user list
If we send id as param than it will show the result of specific  user only 
So we can say it performing task of two function in one get method 
Post method is for creating new data 
ex:
        {
          "name" : "<user_name>",
          "display_name" : "<display name>"
        }
Put method is for updating  existing data
ex:         {
            "name" : "<user_name>",
            "display_name" : "<display name>",
            "creation_time" : "<some date:time format>"
          }
NOTE : all the required param are explain in userbase.py :  file 


http://127.0.0.1:8000/userbaseapi/getuserteams' 
for geting detail of userteam  we have 
get method and param request:
        {
          "id" : "<user_id>"
        }




these api are for teambaseapi.py

  http://127.0.0.1:8000/teambaseapi/team'
  Get method is for retrieving the data
If don’t pass id param the it will give us all the list_teams  list
If we send id as param than it will show the result of specific  describe_team  only 
So we can say it performing task of two function in one get method 
Post method is for creating new data 
ex:
:param request: A json string with the team details
        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "admin": "<id of a user>"
        }
Put method is for updating  existing data
ex: {
        "id" : "<team_id>",
        "name" : "<team_name>",
        "description" : "<team_description>",
        "admin": "<id of a user>"
          
    }
NOTE : all the required param are explain in userbase.py :  file 

  http://127.0.0.1:8000/teambaseapi/removeuser'

  this api have Post method to remove user 
  :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

  http://127.0.0.1:8000/teambaseapi/adduser' 
  this api have Post method to add user 
  :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }


  http://127.0.0.1:8000/teambaseapi/listteamusers' 
  in this Get method help us to get all the  list teamu sers
    :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }


these api are for teambaseapi.py
  http://127.0.0.1:8000/boardbaseapi/borad'

          :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}
  http://127.0.0.1:8000/boardbaseapi/addtask'
  in this Post method old user is replace by new user to whom we assigned the task 
  :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }

  http://127.0.0.1:8000/boardbaseapi/updatetaskstatus'
  this Post method help us to update the status of work 
        :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }

  http://127.0.0.1:8000/boardbaseapi/listboardsapi'
  this get method help us to get all the list of boards
          :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]

  http://127.0.0.1:8000/boardbaseapi/closeboardapi'
  In  this Post method is to update the board game status to CLOSE if it already completed is task 
        :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }
 
  http://127.0.0.1:8000/boardbaseapi/exportboardapi' 
  In this post method we create Excel file and store in "out"  name folder
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }

