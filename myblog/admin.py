from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','comment']
    list_filter = ['title']
    search_fields = ('title',)
    list_editsble = ('title','comment')



admin.site.register(Post,BlogAdmin)