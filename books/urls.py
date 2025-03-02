from django.urls import path
from .views import HomeView, BookDetailView, BookUpdateView, BookCreateView, BookDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-update'),
    path('books/', HomeView.as_view(), name='book-list'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
