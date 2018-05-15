from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SymptomsForm
from dal import autocomplete

# Create your views here.


class PredictDisease(TemplateView):
    def get(self, request, **kwargs):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request
            form = SymptomsForm(request.post)
            # check if the form data is valid

        else:
            form = SymptomsForm()

        return render(request, 'index.html', {'form': form})


class AboutPageView(TemplateView):
    template_name = "about.html"


class SymptomsAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        print('Im in autocomplete')
        return ["Chest pain", "Fever", "Cold"]
