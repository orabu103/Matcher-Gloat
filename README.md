# Matcher-Gloat :mag_right:


## How To Setup:


```shell
setup.sh
```


## How To Run: 


```shell
python manage.py runserver
```
## Starting server at
 ``` shell
 http://127.0.0.1:8000/
 ```

# Navigation Bar
<img width="500" alt="portfolio_view" src="./png/Nav.png">

## Skill
* Option to add skills to a database
* Displays all the skills that are in a database

## Title
* Option to add titles to a database
* Displays all the titles that are in a database

## Job
* Option to add Job to a database
  * Selecting a title from a database
  * Selecting a skills from a database
* Displays all the Job that are in a database

## Candidate
* Option to add Candidate to a database
  * Selecting a title from a database
  * Selecting a skills from a database
* Displays all the Candidate that are in a database

## CandidateFinder
* Selecting a job from the jobs that is in the database
* Receiving the most suitable candidates for the job
  * Match by title
  * Match by skills
* Sorted by the high amount of skills
# DataBase:
## SQLite

##### TABLE Skill
```
    id int AUTO_INCREMENT PK
    name varchar(200)
```
##### TABLE Title
```
    id int AUTO_INCREMENT PK
    name varchar(200)
```
##### TABLE Job
```
    id int AUTO_INCREMENT PK
    title FK(Title)
    skill Many-to-Many(Skill)
```
##### TABLE Candidate
```
    id int AUTO_INCREMENT PK
    title FK(Title)
    skill Many-to-Many(Skill)
```

