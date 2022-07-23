from dataclasses import field
from django.contrib import admin

from .models import Book, BookInstance, Author


def display_genre(self):
    return ', '.join(genre.name for genre in self.genre.all()[:3])

display_genre.short_description = 'Genre'

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', display_genre)

    inlines = [BooksInstanceInline]



@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    
    list_filter = ('status', 'due_back')

    fieldets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back') 
        })
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('last_name','first_name', 'date_of_birth', 'date_of_death')
    
    fields = (('last_name','first_name'), ('date_of_birth', 'date_of_death'))
    



