from django.contrib import admin
from .models import Editor,Location,categories,Photo

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Photo)
