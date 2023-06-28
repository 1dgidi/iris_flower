from django.shortcuts import render, reverse, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models  import MLModel, Prediction
from .forms import MLModelForm, PredictionForm
from .exceptions import DefaultMLModelException


# @login_required
def upload_model(request):
    template_name = 'prediction_feature/upload_model.html'

    if request.method == 'POST':
        form = MLModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_model_upload = MLModel(
                # uploaded_by = request.user,
                model_file = request.FILES['model_file']
            )
            new_model_upload.save()
            print(request.FILES)
        return HttpResponseRedirect(reverse('prediction_feature:make_prediction'))
    else:
        form = MLModelForm()
        context = { 'ml_model_form': form }
        return render(request, template_name, context)


def make_prediction(request):
    template_name = 'prediction_feature/index.html'

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # select last ml model uploaded to make predictions with
            try:
                latest_model = MLModel.objects.latest('id')

                # a future OSError would happe when it is time to make a new prediction
                # prevent that from happening
                if latest_model.model_file == 'NA':
                    raise DefaultMLModelException
                
            except (MLModel.DoesNotExist, DefaultMLModelException):
                # delete default model
                latest_model.delete()
                
                # redirect to ml model upload page
                return HttpResponseRedirect(reverse('prediction_feature:upload_model'))

            new_prediction = Prediction(
                sepal_width = form.cleaned_data['sepal_width'],
                petal_width = form.cleaned_data['petal_width'],
                sepal_length = form.cleaned_data['sepal_length'],
                petal_length = form.cleaned_data['petal_length'],
                ml_model = latest_model
            )

            new_prediction.save()
        return HttpResponseRedirect(reverse('prediction_feature:show_prediction', args=(new_prediction.id,)))
    else:
        form = PredictionForm()
        empty_prediction = Prediction()
        context = {
            'prediction_form': form,
            'prediction': empty_prediction
        }
        return render(request, template_name, context)


def show_prediction(request, prediction_id):
    prediction = get_object_or_404(Prediction, id=prediction_id)
    prediction_form = PredictionForm(instance=prediction)
    context = {
        'prediction': prediction,
        'prediction_form': prediction_form,
    }
    template_name = 'prediction_feature/index.html'
    return render(request, template_name, context)
