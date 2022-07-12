from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import MovieForm
from .models import Movie

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name , uploaded_file)
        url = fs.url(name)

        context["url"] = url
    return render(request, 'upload.html', context)

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {"movies": movies})

def add_movie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST , request.FILES)
        if form.is_valid:
            form.save()
            return redirect('core:movie_list')
    return render(request, 'add_movie.html',{'form' : form})

def delete_movie(request, pk: int):
    if request.method == "POST":
        movie_obj = Movie.objects.filter(pk=pk).first()
        if movie_obj:
            movie_obj.delete()
    return redirect('core:movie_list')

def update_movie(request, pk:int):
    movie_obj = Movie.objects.filter(pk=pk).first()
    if not movie_obj:
        return redirect('core:movie_list')

    form = MovieForm(instance=movie_obj)

    if request.method =="POST":
        form = MovieForm(request.POST , request.FILES, instance=movie_obj)
        if form.is_valid():
            form.save()
            return redirect('core:movie_list')
    

    return render(request, 'update_movie.html',{'form' : form})
