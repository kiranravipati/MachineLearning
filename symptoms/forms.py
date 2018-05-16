from django import forms
from dal import autocomplete

def get_choice_list():
    return ['France', 'Fiji', 'Finland', 'Switzerland']


class SymptomsForm(forms.Form):
    print('Hello world')
    symptoms = forms.CharField(label="Select symptoms",
                               widget=autocomplete.ListSelect2(url='symptoms-autocomplete'))

    symptomsList = (
        ('fever', 'fever'),
        ('chest pain', 'chest pain'),
        ('cough', 'cough'),
        ('nausea', 'nausea'),
        ('fatigue', 'fatigue'),
        ('shortness of breath', 'shortness of breath')
    )

    symptoms = forms.MultipleChoiceField(label="Select symptoms",
                                         choices=symptomsList,
                                         widget=forms.CheckboxSelectMultiple(),
                                         required=False)

