from django.contrib import admin

# Register your models here.

from.models import Author, Book, Genre, Language, Status, BookInstance
#admin.site.register(Author) 
#admin.site.register(Book) 
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Status) 
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',
    ('date_of_birth', 'date_of_death')]
class BooksInstanceInline(admin.TabularInline):
 model = BookInstance

admin.site.register(Author, AuthorAdmin)

@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'genre', 'language', 'display_author')
  list_filter = ('genre', 'author')
  inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
 list_display = ('book', 'status', 'borrower', 'due_back', 'id')
 list_filter = ('status', 'due_back')
 fieldsets = (
 (None, {
 'fields': ('book', 'imprint', 'inv_nom')
 }),
 ('Availability', {
 'fields': ('status', 'due_back', 'borrower')
 }),
 )
 def borowwer(self):
    BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')