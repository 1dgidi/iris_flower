# Generated by Django 4.2.2 on 2023-06-28 08:21

from django.db import migrations, models
import django.db.models.deletion
import prediction_feature.models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_feature', '0004_remove_mlmodel_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='ml_model',
            field=models.ForeignKey(default=prediction_feature.models.MLModel.get_default_pk, on_delete=django.db.models.deletion.CASCADE, to='prediction_feature.mlmodel'),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='model_file',
            field=models.FileField(default='NA', unique=True, upload_to='./resources/ml_models/'),
        ),
    ]
