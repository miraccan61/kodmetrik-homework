from django.shortcuts import render
from .forms import FormBuilderForm
from .models import FormBuilder
from django.http import JsonResponse


def home(request):
    form = FormBuilderForm()
    if request.is_ajax():
        form = FormBuilderForm(request.POST)
        print(request.body)
        if form.is_valid():
            hash_id = form.cleaned_data['hash_id']
            print(hash_id)
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'work1/index.html', {'form': form})