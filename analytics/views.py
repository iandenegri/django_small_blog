from django.shortcuts import render

from .models import FeatureSurvey
from .forms import FeatureSurveyForm

# Create your views here.

def FeatureSurveyIndex(request):
    if request.method == "POST":
        form = FeatureSurveyForm(request.POST)
        if form.is_valid():
            chosen_feature = form.cleaned_data.get('chosen_feature_option', '')
            suggested_feature = form.cleaned_data.get('feature_suggestion', '')
            FeatureSurvey.vote(chosen_feature)  # Vote for a feature (if you voted.)
            FeatureSurvey.vote(suggested_feature)  # Submit your feature (if you submitted one.)
            pass
        message = "Thank you for your feedback!"
    elif request.method == "GET":
        message = ""

    form = FeatureSurveyForm()

    context = {
        "form": form,
        "message": message
    }

    return render(request, "analytics/survey_form.html", context=context)
    