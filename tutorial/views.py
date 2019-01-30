from django.shortcuts import render
from django.shortcuts import render, redirect
from tutorial.models import *
import ipfsapi
from ipfs_storage import InterPlanetaryFileSystemStorage

def index(request):
    return render(request, 'tutorial/index.html')

def upload(request):
    api = ipfsapi.connect('127.0.0.1', 5001)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'tutorial/upload.html', {'form':form})
