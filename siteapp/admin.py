from django.contrib import admin
from .models import Author
from .models import Book
from .models import BookGenre
from .models import BookRate
from .models import Country
from .models import Genre
from .models import Publisher

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug', 'location']
    search_fields = ['first_name', 'last_name', 'slug', 'popular_name', 'location']
    prepopulated_fields = {'slug': ('popular_name',)}

class BookAdmin(admin.ModelAdmin):
    list_display = ['title_pt', 'author', 'publisher', 'year']
    search_fields = ['title_pt', 'title_original', 'author__author', 'year', 'publisher', 'isbn10', 'isbn13', 'cdu', 'cdd', 'slug']
    prepopulated_fields = {'slug': ('title_pt',)}

class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['book', 'genre']
    search_fields = ['book', 'genre']

class BookRateAdmin(admin.ModelAdmin):
    list_display = ['book', 'rate']
    search_fields = ['book', 'rate']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code']
    search_fields = ['name', 'slug', 'code']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookGenre, BookGenreAdmin)
admin.site.register(BookRate, BookRateAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Genre)
admin.site.register(Publisher)
