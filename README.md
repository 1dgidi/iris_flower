# Predicting the type of iris flower based on sepal and petal shapes

## Run the following commands to get started

### Clone the repository

```shell
git clone https://github.com/1dgidi/iris_flower.git
```

### Move into the project folder
```shell
cd iris_flower
```

### Install the requirements (Internet connection required)
```shell
pip install -r requirements.txt
```

### Create database and database tables
```shell
python manage.py migrate
```

### Load data into the database
```shell
python manage.py loaddata datadump.json
```

### Start the server
```shell
python manage.py runserver
```
