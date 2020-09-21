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

# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        hash_id = request.POST.get('hash_id', None) # getting data from input first_name id
        print(hash_id)
        FormBuilder.objects.create(hash_id=hash_id)
        if hash_id: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response)