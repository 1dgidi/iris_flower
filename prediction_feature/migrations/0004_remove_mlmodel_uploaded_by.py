# Generated by Django 4.2.2 on 2023-06-27 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_feature', '0003_alter_prediction_petal_length_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mlmodel',
            name='uploaded_by',
        ),
    ]
