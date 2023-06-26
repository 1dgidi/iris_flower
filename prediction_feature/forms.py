from django import forms

from .models import MLModel, Prediction


class MLModelForm(forms.ModelForm):
    class Meta:
        model = MLModel
        fields = ['model_file']

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['sepal_width', 'sepal_length', 'petal_length', 'petal_width']

        widgets = {
            'sepal_width': forms.TextInput(attrs={
                'class': 'form-control',
                'Placeholder': 'Sepal Width',
            }),
            'sepal_length': forms.TextInput(attrs={
                'class': 'form-control',
                'Placeholder': 'Sepal Height',
            }),
            'petal_width': forms.TextInput(attrs={
                'class': 'form-control',
                'Placeholder': 'Petal Width',
            }),
            'petal_length': forms.TextInput(attrs={
                'class': 'form-control',
                'Placeholder': 'Petal Length'
            }),
        }


