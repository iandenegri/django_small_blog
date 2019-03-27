from django import forms
from .models import FeatureSurvey

class FeatureSurveyForm(forms.Form):
    chosen_feature_option = forms.ChoiceField(choices=[],
                                        label='Feature Name',
                                        required=False,
                                        widget=forms.Select(
                                            attrs={
                                                "class": "form-control"
                                                }
                                            )
                                        )
    feature_suggestion = forms.CharField(label="Suggestion", 
                                          max_length=150, 
                                          required=False, 
                                          widget=forms.TextInput(
                                              attrs={
                                                  "class": "form-control", 
                                                  "placeholder": "Have a suggestion for a new feature?",
                                                }
                                            )
                                        )
                                    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_features = FeatureSurvey.objects.filter(active=True).order_by('feature_name').values_list('feature_name', flat=True).distinct()
        self.fields['chosen_feature_option'].choices = [(feature_name, feature_name) for feature_name in unique_features]
