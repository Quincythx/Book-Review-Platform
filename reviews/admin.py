from django.contrib import admin
from .models import Genre, Review, Comment

# Register your models here.
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)