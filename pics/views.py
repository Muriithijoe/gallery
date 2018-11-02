from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Photo

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pics_of_day(request):
    date = dt.date.today()
    pics = Photo.today_pics()

    return render(request, 'all-pics/today-pics.html', {"date": date,"pics":pics})

def convert_dates(dates):

    #Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    #Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_pics(request, past_date):
    try:
        #converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pics_today)

    pics = Photo.days_pics(date)
    return render(request, 'all-pics/past-pics.html',{"date": date,"pics":pics})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("article")
        searched_photos = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"photo":searched_photo})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pics/image.html", {"photo":photo})
