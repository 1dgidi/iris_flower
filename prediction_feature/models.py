from django.db import models
from django.contrib.auth.models import User

import keras
import numpy as np

class MLModel(models.Model):
    model_file = models.FileField(default='NA', upload_to='./resources/ml_models/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.model_file.name.split('/')[-1]


class Prediction(models.Model):
    sepal_width = models.FloatField()
    petal_width = models.FloatField()
    sepal_length = models.FloatField()
    petal_length = models.FloatField()
    predicted_species = models.CharField(max_length=50, default='NA')

    def predict_species(self):
        FLOWER_TYPES = {
            0 : 'setosa',
            1 : 'versicolor',
            2 : 'virginica'
        }

        # latest_model_file = MLModel.objects.filter(uploaded_by=request.user).latest('id')
        latest_model = MLModel.objects.latest('id')
        model = keras.models.load_model(latest_model.model_file.name)
        model_input = [[
            self.sepal_length, self.sepal_width,
            self.petal_length, self.petal_width
        ]]
        prediction = model.predict(model_input)
        
        return FLOWER_TYPES[np.argmax(prediction)]


    def save(self, *args, **kwargs):
        # make prediction before saving instance
        self.predicted_species = self.predict_species()
        super().save(self, *args, **kwargs)

    def __str__(self):
        return f'SW: { self.sepal_width } | SL: { self.sepal_length } | PW: { self.petal_width } | PL: { self.petal_length } | P: { self.predicted_species }'


