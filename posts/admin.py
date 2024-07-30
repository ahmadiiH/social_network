from django.contrib import admin
from .models import Post , PostFile

# Register your models here.

class PostFileInlineAdmin(admin.TabularInline):
    model = PostFile
    fields = ['file']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'is_active' , 'created_time')
    inlines = [PostFileInlineAdmin]

@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    pass



