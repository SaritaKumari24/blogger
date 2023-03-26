from django.contrib import admin
from .models import BloggerPost,Category
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    def delete_button(self, obj):
        return format_html("<a href='/admin/cms/category/{}/delete'>Delete</a>", obj.id)
    def update_button(self, obj):
        return format_html("<a href='/admin/cms/category/{}/change'>Edit</a>", obj.id)


    list_display = ["id","title","description","slug", 'delete_button','update_button']
    list_display_links = ['title','slug']

    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    search_fields = ['id','title',]
    list_display = ('title', 'description', 'status',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BloggerPost, PostAdmin)
