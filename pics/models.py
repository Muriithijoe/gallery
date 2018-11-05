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
    name = models.CharField(max_length =90)

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
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,name,description,location,category):
        image = cls.objects.get(pk=id)
        image = cls(name=name,description=description,location=location,category=category)
        image.save()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(pk=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
