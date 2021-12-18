# Matcher-Gloat :mag_right:


## How To Setup:
##### cmd: ```.../web_site```

```shell
setup.sh
```


## How To Run: 
##### cmd: ```.../web_site```

```shell
python manage.py runserver
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

