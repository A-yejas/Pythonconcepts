#Difference between AJax & Json
'''
Ajax:- Stans for Asynchronous javascript and XM,
1.Itis used to communicate with server without refreshing the web page and thus increasing the user exp & perfrmance
2.There are 2 types of requests synchronous as well as Asynchronous.
3.synchronous requests are the one which follows sequentially i.e., if the one process is going on at the same
time another process wants to be executed, it will be not allowed that means the only one process
at a time will be eexcuted.
Advantages:- 1.Speed is enhanced as there is no need to reload the page again.
Disadavntage:- Ajax is dependent on JS.If there is some JS Problem with the browser or in the OS Ajax will not sprt.
-> Blend, energetic, server-side information
---->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Json:- Stands javascript object notation
'''
#URL:- Uniform resource Locator
'''
Command for generate allure report 
pytest test_case_name.py -v --alluredir=allure-reports
generating report temporary :- allure serve reports 
allure generate --clean -- to delete the folder values

'''
import requests
import pytest

@pytest.mark.positive
def test_positive_case():
    URL="https://restful-booker.herokuapp.com/booking/"
    headers = {'content-type':'application/json'}
    json_payload={
        "firstname" : "Amit",
        "lastname"  : "Brown",
        "totalprice":111,
          "depositpaid": True,
        "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Amit", "Failed Message - Incorrect FirstName"
#405 -> Method Not allowed

@pytest.mark.negative
def test_create_booking_negative():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500
'''
What is framework:- 
Best practise, Guidlines to create a structure code that you can maintain , Reuse, Scaled.
data driven framework means:- when you ingest some data into from external source to your test scripts then
your test runs multiple times.
Where we will use this data driven testing :-  we can use this DDT is for example create Auth, For example
for create Authentication , suppose i want to test my 100 users for admin 

'''
##Create Virtual ENV:- virtualenv (name_any eg:- venv)
#for activae For linux :-  Source  venu/bin/activate , For deactivate:- deactivate
#README.md is a create documentation file
'''
#If you make package as if you make folder as a package Python interpreter will recognize. 
#2. If you creating a python package it is basically telling to python interpreter that every thing is good.same time
intelliJ also recognize it is fast execution
pip lst :- you can see all install packages
# To freeze your package version use below commads:-
pip freeze > requirements.txt
#To Install the freeze versions use below command
pip install -r requirements.txt

'''
#What is static method, Static method is basically a method which can be used by using the class name a API
#For Static fucntions you can call methods name like Classname.functionname() suppose which your calling that is
#not static method so in this case you can call as like Classname().function() [explanation is :- Create a instance of api call then cal]
'''
From Linkdin cpoies this.
How do you prioritize test cases when you have limited time for testing?
To prioritize test cases?

1. Focus on critical functionality that has the highest impact on the business
2. Consider areas with the highest risk of failure
3. Test new features and changes first
4. Use the defect history to identify problematic areas
5. Prioritize tests based on customer usage patterns

Do like , comment & repost , if you find it helpful.

'''
#Framework Structure:-
#src folder :-
#Under helpers folder:-
    #constants folder :- Keep Constants
    #helper folder :- creating Generic methods like Get,Post,Put,Delete
    #resource folder: Like storing the Excel,.csv,json resouces files
'''
#Figure out the Operations for API Automation:-
1.CRUD Operations.
2.URLS
3.Payloads
4.Headers (Auth-Basic Api Key)
5.Verification Part - (Assert Pytest)
'''
#Install pytest-xdist check about this tool first in google,actually it allowed to user run there test cases multiple CPU"S
#pytest -n auto test_case_names
"""
#IF ypu wamt run test cases parallely
1.Your test case should be atomic ->1
test cases per method or file
2.They should not depend each other.
3.They depend -> make them a separate each other.
"""

#1.More test cases for Token create:-
'''
1.Valid Input
2.Invalid user name
3. Invalid Password
4.Alpha 123@ewq
5.{}empty
6.Null
7.Special Characters
8.arabic
9.Invalid Url , invalud headers, limit username & pwd 
'''
#pip install python-dotenv --> it will help you secure your variables
#Json Schema validate only - Key, required type of Data type
# To Verify the JSon schema using tiny validator in postman
#pip install json schema
#Cron tab guru -- Set timing in Jenkins
#########
'''
# Install jenkins at same time install jdk as well
#For package(plugins) install go to "Manage Jenkins" -> Plugins -> Available Plugnis -> search for HTML Publisher
# -> Python Plugin e.t.c., select check boxes what ever you want click on install button located at right side ->
#download jdk from google .
#-> Manage Jenkins -> Go to "tools" -> Add Name as JDK -> Add JDK Path -> Go to down add Allure commands
#New File -> Enter an item name - > Click on freestyle -> Click on Ok  -> Source code management -> Selecct
#-> Git -> Add Git repo path - > Branch as same git -> Next Add build step ->Build env -> Windows bash command -> 
Select check box of window bash command  -> set path "add python install path(eg:- e.t.c.,/python312)"
 -> set path "add python Scripts path (eg:- e.t.c.,/Scripts)" -> pip install requirements.txt ->
 pytest (File path/folder path .py file) --alluredir=allure-results.
 _-------
 Configure the pipeline:- 
 Jenkins - > new job --> give any name in searcg bar - > select pipeline option  ->  click on Ok ->
 Build Triggers select time - > 
 
 -->>jenkins:- Commit -> Build -> test -> Stage -> Deploy 
 #Cron tab (to excute) for timing
 #######
 for email-> go to configuration -> add plugin which is called as email extended plug if you want to customize 
 more if you dont want to do it just go to your manage jenkins configuraton - > add you smtp settings and 
 enter your email & pwd after that in the post build section of any job that you want to get emaild id  emails
 you just need to add post build sections and add the email id where you want to get the email.
 ####For multi brancn run -> same steps insted of free style project select multibranch pipe line option
 -> click on ok -> 
 ########## 
 ### there 5 steps:- 
 1.General:- 
 2.Source Code management
 3.Build Triggers  :- select "Build priodically" if yow want to run.
 4.Build Steps:- 
 5.Post Build Actions:-  Add which type of report required example hTml
 Dummy:- pip install requests pytest pytest-html faker allure-pytest jsonschema 
'''
# -----------------------
# JSON:- Javascript object notaion
# JSON Object:- {}
# JSON Array :- []
# Simple Json :- {'key':'value'}
# complex:- { 'key':{
#     'key2':'value'
# },
#     'keyArray':[{
#         'apple':'fruit',
#         'banana':'fruit'
#     }
#     ]
#
# }
# --------------
# To Run all Apis from command prompt use Newman keyword :
# Download the Newman and node.js and npm install
#npm install -g newman
#newman "post man collection path" -r cli, htmlextra
# Postman
# javascript:-pm.test("Status code is 200",function() {
# pm.response.to.have.status(200);
# Representational state transfer means:- tranfer the data from client to server
# -------------
# // Write the JS Code which can do the Automation or Automation Checking or Verify the response.
# console.log("Hello pramod")
# console.log(pm.response.json())
# var response = pm.response.json();
# console.log(response["bookingid"])
# console.log(response["booking"]["firstname"])
# if(response["bookingid"] != 0){
# console.log("Passed")
# }
##
# framework_structure:
# src:- Source directory will contains all the things which are not related to test.
#tests:- and testd contain are belongs to test
#git ignore:- get the link from toptal.com , select pycharm :- basicall use of you dont basically upload the
#this virtual env
#helpers folder:- make you help on make the request and common verification


# ___________
# # Import Module
# import json
#
# # Create geeks function
#
#
# def geeks():
#
# 	# Define Variable
# 	language = "Python"
# 	company = "GeeksForGeeks"
# 	Itemid = 1
# 	price = 0.00
#
# 	# Create Dictionary
# 	value = {
# 		"language": language,
# 		"company": company,
# 		"Itemid": Itemid,
# 		"price": price
# 	}
#
# 	# Dictionary to JSON Object using dumps() method
# 	# Return JSON Object
# 	return json.dumps(value)
#
#
# # Call Function and Print it.
# print(geeks())
''' 29/08/2024'''
'''
1.Communication between client and server its light weight nature text based message
2.XML was not human friendly , its tag based system.
3.Json-Data Types:- [] :- -> array means Bunch of Objects/items with single data type.
{}->Json Object , 
Key always be string, if key is "int" that is not a valid json.
4.if the json starting point is {} curly braces access with the '.dot' if starting point array access with array[]
5.You cannot send the javascript object to server Yoy can only send the strings.
API Test Case verified:-
1.Headers, 2.Response Body,3,Response Time, 4.Status Code, 5.Structire of response
PostMans-supports only csv files not excel format files.
mockaro.com --> is generate the data for testing 
-----
Vriable means to store a data
Types of variables in postman:-
1.Global variable, 2. Collection variable,3.Environment variables,4.data variabkes,5. Local variable
payload means  dada
------------
var loca_var=pm.response.json()
var booking_id=loca_var['booking_id']
pm.environment.set("bookingid",bookingid)
---
var token=local_var['token]
pm.environment.set("token",token)
----
pm.globals.set("gtoken", token)
--------
pm.collectionVariables.set("cToken", token)
---------
To pass the data from one request to another request you use the environment variable.
----
check the email :-
pm.test("Email is in a valid format",function(){
    const responseData=pm.response.json();
    
    pm.expect(responseData).to.be.an('object');
    pm.expect(responseData.email).not.to.be.null;
    
    
    });
'''
# --------------
'''
JSON:- Json schema validate the structure and type only not the values.
Json schema regex:- ^[A-Za-z0-9 -_]+_Prog\\.(exe |EXE)$"
Auth 2.0
Only path the Client_id & Client_Secret
'''
#Idempotent means whenever i calling this put api entire the particular API the entire object will be updated
#it will not create a new row in the database it will not create a new user in the db
'''
curl --location --request GET 'https://edge--non-prod--elasticsearch.hirealchemy.com:9205/hcl--dev--ta--candidates-02/_search' \
--header 'Authorization: Basic ZWRnZS0tbm9uLXByb2QtLWVsYXN0aWNzZWFyY2gtLXVzci0wMTplZGdlLS1ub24tcHJvZC0tZWxhc3RpY3NlYXJjaC0tdXNyLTAxLUVkR0UyMDE5' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": {
        "match": {
            "resume_ids": "1446118"
        }
    }
}'
-----------------------
ELASTIC SEARCH:-
{
   "doc":{
      "projects":[
         
         {
            "project_name":"AIGI-Consulting Services",
            "project_id":"C070941",
            "assignment_start_date":"2021-01-01",
            "assignment_end_date":"2022-12-31",
            "responsibilities":null,
            "is_current_employee":null,
            "skills":[
               
            ],
            "allocation_percentage":100,
            "cand_proj_id":"",
            "is_company_project":true
         },
         {
            "project_name":"AIG sunamerica Chennai",
            "project_id":"C115269",
            "assignment_start_date":"2023-01-01",
            "assignment_end_date":"2023-12-31",
            "responsibilities":null,
            "is_current_employee":null,
            "skills":[
               
            ],
            "allocation_percentage":100,
            "cand_proj_id":"",
            "is_company_project":true
         }
      ]
   }
}
-----------------------


'''
