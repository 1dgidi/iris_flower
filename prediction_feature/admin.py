from django.contrib import admin

from .models import MLModel, Prediction

admin.site.register(MLModel)
admin.site.register(Prediction)
