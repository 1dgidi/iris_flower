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

### Start the server
```shell
python manage.py runserver
```

### Upload iris model
visit [http://127.0.0.1:8000/upload](http://127.0.0.1:8000/upload)

### Iris Model (example)
You would find an example model to test the system in the [example-iris-model](https://github.com/1dgidi/iris_flower/tree/master/example-iris-model) folder

### Accessing the admin interface
If you want to see previous predictions or the models you have uploaded, run the following command to create a superuser
```shell
python manage.py createsuperuser
```
Follow the prompts to create the superuser.\
Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to log into the admin panel.
