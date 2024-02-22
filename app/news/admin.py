from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at','updated_at','is_published', 'get_photo')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)
    fields = ('title','category','content','photo','get_photo','is_published','views','created_at','updated_at')
    readonly_fields = ('get_photo','views','created_at','updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            # print("Herrreeeee")
            # print(obj.photo.url)
            # return mark_safe(f'<img src"{obj.photo.url}" width="75" />')
            return mark_safe(f'<img width="50px" src="{obj.photo.url}" />')
        else:
            return '-'
        
    get_photo.short_description = 'Img of News'
        

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'This is admin of my site'
admin.site.site_header = 'This is admin of my site'