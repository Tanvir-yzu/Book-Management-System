from django.db import models
from django.urls import reverse

class Book(models.Model):
    """Model representing a book in the library."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length=13, unique=True, 
                           help_text='13 Character ISBN number')
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    
    # Rating from 1 to 5
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    
    # Status of the book (available, borrowed, etc.)
    STATUS_CHOICES = (
        ('a', 'Available'),
        ('b', 'Borrowed'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='a',
        help_text='Book availability',
    )
    
    # Date added to the library
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title', 'author']
    
    def __str__(self):
        """String representing the book."""
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])