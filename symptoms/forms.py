from django import forms
from dal import autocomplete


class SymptomsForm(forms.Form):
    print('Hello world')
    symptoms = forms.ChoiceField(label="Select symptoms",
                               widget=autocomplete.ListSelect2(url='symptoms-autocomplete'))