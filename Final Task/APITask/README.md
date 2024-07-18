# API Task Details.



The Django Server can be run using 

`python manage.py runserver`

This Assignment project has API to fetch data from CSV and Put into Database (`POST`)
And Has Another API to fetch those records from database. (`GET`)

In order to check APIs one has to Use tools like Postman or Django Rest Framework Interface.

Let's See the `GET` api.

1. After starting the server you will get the url of server in Terminal.
   like this -> Starting development server at `http://127.0.0.1:8000/.`

2. Go to this URL and see the response of `GET` api.
 
## Output 
![alt text](image.png)


Let's see the `POST` API.
1. Just add `/csv` to base url. to see the magic.
2. Now press the `POST` button on screen to post the request.

### Intitial Page
![alt text](image-2.png)

### After Posting the Request to server.
![alt text](image-3.png)


## Regular Expression for Emails

It checks the occurence of characters from (a-zA-Z). `+` sign check for atleast one occurence.

then check it sees wheter numbers [0-9] are present or not. `*` denotes zero or more time.

followed by check of `@` sign.
then it sees any charachter from alphabets. for example, `hot` or `g` etc(zero or more time).

then it checks for sequence `mail`

followed by `.` in mailid's

lastly `com` sequence.

`[a-zA-Z]+[0-9]*@[a-zA-Z]*(mail).(com)+`

#### Output
![alt text](image-1.png)

## ER - Diagram of Database.
![alt text](image-4.png)

## To do 
1. JWT authentication.
2. Adding Company table with unique constraint.
3. Foreign Key and Primary Key for Employee and Company.