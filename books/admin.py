from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin View for Book model"""
    list_display = ('title', 'author', 'isbn', 'status', 'rating', 'date_added')
    list_filter = ('status', 'rating', 'genre')
    search_fields = ('title', 'author', 'isbn')
    ordering = ('title', 'author')
    readonly_fields = ('date_added',)
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'isbn', 'publication_date', 'genre')
        }),
        ('Description', {
            'fields': ('description', 'cover_image')
        }),
        ('Status', {
            'fields': ('status', 'rating')
        }),
        ('Metadata', {
            'fields': ('date_added',),
            'classes': ('collapse',)
        }),
    )
    
    # Customizing admin panel styles
    class Media:
        css = {
            'all': ('css/admin.css',)
        }