# Create your views here.
from django.shortcuts import render, redirect
from forms import FileForm

def index(request):
    return render(request, 'download_files/index.html')

def download(request):
    if request.method == "POST":
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FileForm()
    return render(request, 'download_files/download.html', {'form': form})

def success(request):
    return render (request, 'download_files/success.html')