# GetAJob_Site

This site is designed to take in JSON formatted job applicant data and display all job applicants on the 'applicant listings' page. On the applicant listings page users can sort by position type and experience. Full user functionality has not been implemented however a 'dummy' user admin1 has been created to show functionality of saving and deleting applicants as desired. 

This site is meant to take in JSON formatted job listings in the following format:
{
       "id": 11,
       "name":"Dana White",
       "position":"Sports Official",
       "applied":"02/12/16",
       "experience":6,
       "availability":{
          "M":1,
          "T":1,
          "W":1,
          "Th":1,
          "F":1,
          "S":4,
          "Su":4
       },
       "questions":[
          {
             "text":"Are you authorized to work in the United States?",
             "answer":"Yes"
          },
          {
             "text":"Have you ever been convicted of a felony?",
             "answer":"No"
          }
       ]
    },
    
 ...
 
 These entries can be loaded using the addDB method which parses input and inserts data into sqlite3 database.
 
 To run the site just navigate to the saved directory and type [jobsys manage.py runserver] in the cmd line. Then enter http://localhost:8000/listings/ in a browser to access the site. 
