from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Photo

# Create your views here.
def gallery(request):
    photos = Photo.all_images()
    return render(request, 'gallery.html', {"photos":photos})


def search_results(request):

    if 'photo' in request.GET and request.GET("photo"):
        search_term = request.GET.get("photo")
        searched_images = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "No photos under this category exist"
        return render(request, 'search.html',{"message":message})


def photo(request,image_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})
