# Create your views here.
from django.shortcuts import render, redirect
from forms import FileForm, RegistrationForm


def index(request):
    text = r'hello'
    return render(request, 'download_files/index.html', {'text': text})

def download(request):
    if request.method == "POST":
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileForm()
    return render(request, 'download_files/download.html', {'form': form})


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('download')
    else:
        form = RegistrationForm()
    return render(request, 'download_files/registration.html', {'form': form})
