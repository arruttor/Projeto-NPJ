from django.shortcuts import render,redirect
from core.forms import beneficiaryModelForm


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def new_beneficiary_view(request):
    if request.method == 'POST':
        new_beneficiary_form = beneficiaryModelForm(request.POST)
        print(new_beneficiary_form.is_valid())
        if new_beneficiary_form.is_valid(): 
            new_beneficiary_form.save()
            return redirect('dashboard')
    else:    
        new_beneficiary_form = beneficiaryModelForm()

    return render(request, 'new_beneficiary.html', {'new_beneficiary_form': new_beneficiary_form})