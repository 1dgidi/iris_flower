from django.urls import path

from . import views

app_name = 'prediction_feature'

urlpatterns = [
    path('', views.make_prediction, name='make_prediction'),
    path('upload/', views.upload_model, name='upload_model'),
    path('show/<int:prediction_id>', views.show_prediction, name='show_prediction'),
]
