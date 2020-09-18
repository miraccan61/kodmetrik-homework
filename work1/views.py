from django.shortcuts import render
from .forms import FormBuilderForm
from .models import FormBuilder

def home(request):
    forms = FormBuilderForm()
    if request.method == 'POST':
        hash_id = request.POST.get('hash_id')
        print(hash_id)
    context={
        'forms':forms
    }
    return render(request,'work1/index.html',context)