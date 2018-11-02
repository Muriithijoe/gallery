from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'articles/', blank=True)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(post_date__date = today)
        return pics

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(post_date__date = date)
        return pics

    @classmethod
    def search_by_title(cls,search_term):
        pics=cls.objects.filter(title__icontains=search_term)
        return pics
