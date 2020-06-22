from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

admin.site.register(Post)
admin.site.register(Category)