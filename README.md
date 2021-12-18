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

