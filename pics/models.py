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

class Location(models.Model):
    name = models.CharField(max_length =90, blank =True)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class categories(models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'articles/', blank=True)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ManyToManyField(categories)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def update_photo(cls,id,name,description,location,category):
        photo = cls.objects.get(pk=id)
        photo = cls(photo=photo,description=description,location=location,category=category,post_date=post_date)
        photo.save()

    @classmethod
    def get_image_by_id(cls, id):
        photo = cls.objects.get(pk=id)
        return photo

    @classmethod
    def filter_by_location(cls, location):
        photos = cls.objects.filter(location=location)
        return photos
    @classmethod
    def all_images(cls):
        photos = cls.objects.all()
        return photos

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
