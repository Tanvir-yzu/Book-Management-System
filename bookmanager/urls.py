from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('books.urls')),  # Make sure 'books.urls' exists
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
admin.site.site_header = "Book Management Admin"
admin.site.site_title = "Book Management Portal"
admin.site.index_title = "Welcome to Book Management System"
