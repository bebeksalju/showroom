from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Mobil, Service
from .forms import MobilForm, ServiceForm

def daftar_mobil(request):
    mobil_list = Mobil.objects.all()
    return render(request, 'mobil/daftar_mobil.html', {'mobil_list': mobil_list})

def detail_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    services = mobil.services.all()
    return render(request, 'mobil/detail_mobil.html', {'mobil': mobil, 'services': services})

def tambah_mobil(request):
    if request.method == 'POST':
        form = MobilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_mobil')
    else:
        form = MobilForm()
    return render(request, 'mobil/tambah_mobil.html', {'form': form})

def tambah_service(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.mobil = mobil
            service.save()
            return redirect('detail_mobil', mobil_id=mobil_id)
    else:
        form = ServiceForm()
    return render(request, 'mobil/tambah_service.html', {'form': form, 'mobil': mobil})

def hapus_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    mobil.delete()
    return redirect('daftar_mobil')

def edit_mobil(request, mobil_id):
    mobil = get_object_or_404(Mobil, id=mobil_id)
    if request.method == 'POST':
        form = MobilForm(request.POST, instance=mobil)
        if form.is_valid():
            form.save()
            return redirect('detail_mobil', mobil_id=mobil_id)
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'mobil/edit_mobil.html', {'form': form, 'mobil': mobil})
