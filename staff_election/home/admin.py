from django.contrib import admin
from .models import posts, candidates, booths

class postsAdmin(admin.ModelAdmin):
    list_display = ('title','name')
    search_fields = ('title','name')  
    filter_horizontal = ()

class candidatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'votes')
    search_fields = ('name', 'post', 'votes')
    filter_horizontal = ()


class boothsAdmin(admin.ModelAdmin):
    list_display = ('name', 'submitted')
    search_fields = ('name', 'submitted')
    filter_horizontal = ()