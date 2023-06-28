from django.db import models
from django.contrib.auth.models import User

import keras
import numpy as np


class MLModel(models.Model):
    model_file = models.FileField(default='NA', upload_to='./resources/ml_models/', unique=True)
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.model_file.name.split('/')[-1]

    @classmethod
    def get_default_pk(cls):
        try:
            latest_model = cls.objects.latest('id')
        except cls.DoesNotExist:
            new_model, is_created = cls.objects.get_or_create(model_file='NA')
            return new_model.pk
        return latest_model.pk


class Prediction(models.Model):
    sepal_width = models.FloatField()
    petal_width = models.FloatField()
    sepal_length = models.FloatField()
    petal_length = models.FloatField()
    predicted_species = models.CharField(max_length=50, default='NA')

    # ml model prediction would be made with
    ml_model = models.ForeignKey(
        MLModel,
        on_delete=models.CASCADE,
        default=MLModel.get_default_pk
    )

    def predict_species(self):
        FLOWER_TYPES = {
            0 : 'setosa',
            1 : 'versicolor',
            2 : 'virginica'
        }

        model = keras.models.load_model(self.ml_model.model_file.name)
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
