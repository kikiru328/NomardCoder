###### on admin page error:
no such table : django_session  
> Django need to find django_session Database

```bash
>>>db.sqilte3 << Database
```

why django find django_session table?  
Django make for admin  


### Migration?
modifies states Database

즉, 현재 DB가 비워져 있는데  
Djang는 18개의 Migraion(파일)을 가지고 있다.  
이것들은 우리의 DB를 수정할 것임. (module실행시)

```bash
>>> python manage.py migrate
>18개의 파일을 실행함.
>DB를 바꿈
```