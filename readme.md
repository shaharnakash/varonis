#Varonis task
###Tools
1. pycharm
2. bitbucket

##packages
1. pytest
2. pytest-sugar
3. requests

##preparation
pipenv install pytest
create class Person
create class MagicList
create pytest test_MagicList

### python version 3.7

###tree
```
.
├── MagicList.py
├── Person.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── readme.md
├── test_interview_server.py
└── test_MagicList.py
```


##Task 1 Magic List
install python dependencies 
`pipenv install`

execute via terminal `pytest . -m magic`

##Task 2 interview server
install python dependencies 
`pipenv install`

execute via terminal `pytest . -m api_server`

###files in details
1. MagicList.py - the logic of MagicList ability
2. Person.py - define extended class attr
3. Pipfile - all python dependencies 
4. pipfile.lock - versions of installed dependencies
5. pytest.ini - define markers and addopts
6. test_MagicList.py - pytest tests
7. test_interview_server.py
