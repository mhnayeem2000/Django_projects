from django.contrib import admin
from my_app.models import musicians, album 
# Register your models here.

admin.site.register(musicians)
admin.site.register(album)