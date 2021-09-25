from django.shortcuts import render
from .forms import SamplingStationForm

def create_station(request):
    if request.method == 'GET':
        return render(request,'sampling_stations/create.html',{'form':SamplingStationForm()})
    else:
        form = SamplingStationForm(request.POST)
        form.save()
        return redirect('station_data')
