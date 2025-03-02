from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Book
from .forms import BookForm
# Class-based view


class HomeView(ListView):
    """View for listing all books."""
    model = Book
    context_object_name = 'books'
    template_name = 'home.html'
    paginate_by = 8  # Show 8 books per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | 
                Q(author__icontains=query) |
                Q(isbn__icontains=query) |
                Q(genre__icontains=query)
            )
        return Book.objects.all()
    

class BookDetailView(DetailView):
    """View for displaying book details."""
    model = Book
    context_object_name = 'book'
    template_name = 'book_detail.html'
  
    
class BookCreateView(SuccessMessageMixin, CreateView):
    """View for creating a new book."""
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('home')
    success_message = "Book '%(title)s' was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Book'
        context['button_text'] = 'Add Book'
        return context
 
    
class BookUpdateView(SuccessMessageMixin, UpdateView):
    """View for updating a book."""
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('home')
    success_message = "Book '%(title)s' was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Book'
        context['button_text'] = 'Update Book'
        return context


class BookDeleteView(SuccessMessageMixin, DeleteView):
    """View for deleting a book."""
    model = Book
    context_object_name = 'book'
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Book was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message)
        return super(BookDeleteView, self).delete(request, *args, **kwargs)
