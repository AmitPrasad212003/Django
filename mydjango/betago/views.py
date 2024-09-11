from django.shortcuts import render
from .models import chaiVarity,Store
from django.shortcuts import get_object_or_404
from .forms import ChaivarityFrom
# Create your views here.

def all_chai(request):
    chais = chaiVarity.objects.all()
    return render(request, 'betago/all_chai.html',{'chais': chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(chaiVarity,pk = chai_id)
    return render(request,'betago/chai_details.html', {'chai':chai})

def chai_store_view(request):
    stores = None
    if request.method == "POST":
        form = ChaivarityFrom(request.POST)    
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaivarityFrom()
    return render(request, 'betago/chai_store.html',{'stores' : stores, 'form': form})