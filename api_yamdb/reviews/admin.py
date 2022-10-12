from .models import (User, Category, Genre, Title,
                     GenreTitles, Review, Comment)

from django.contrib import admin


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitles)
admin.site.register(Review)
admin.site.register(Comment)
