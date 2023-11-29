## Install Django and required packages
```bash
pip install django
pip install django djangorestframework
```

## CREATE PROJECT
```bash
django-admin startproject employee_data
```
## Enter in to project dir
```bash
cd employee_data
```
## CREATE APP
```bash
python3 manage.py startapp employee_attnd
```

## CREATE TABLE AND MAKE MIGRATIONS
```bash
python3 manage.py makemigrations
python3 manage.py migrate 
```

## Start server
```bash
python manage.py runserver
```

## TEST CASES
===============
# create employee
```bash
curl -X POST http://127.0.0.1:8000/api/create_employee/ -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "age": 30, "gender": "male", "phoneNo": "", "addressDetails": {"hno": "123", "street": "Main St", "city": "City", "state": "State"}, "workExperience": [{"companyName": "ABC Corp", "fromDate": "2020-01-01", "toDate": "2022-01-01", "address": "ABC Address"}], "qualifications": [{"qualificationName": "Bachelor'"'"'s", "fromDate": "2010-01-01", "toDate": "2014-01-01", "percentage": 80.0}], "projects": [{"title": "Project X", "description": "Description of Project X"}], "photo": ""}'
```
# update employee
```bash
curl -X PUT http://127.0.0.1:8000/api/update_employee/1/ -H "Content-Type: application/json" -d '{"name": "Updated Name"}'
```
# get all employees
```bash
curl http://127.0.0.1:8000/api/get_all_employees/
```
# delete employee
```bash
curl -X DELETE http://127.0.0.1:8000/api/delete_employee/1/
````
