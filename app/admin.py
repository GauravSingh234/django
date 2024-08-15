from django.contrib import admin
from app.models import Book,Author,Publisher
from django.contrib.admin import SimpleListFilter
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse


class MyAdminSite(AdminSite):
    site_header = 'My Bookstore Admin'
    site_title = 'Bookstore Admin'
    index_title = 'Welcome to the Bookstore Admin Dashboard'

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('my-custom-dashboard/', self.admin_view(self.custom_dashboard_view))
        ]
        return custom_urls + urls

    def custom_dashboard_view(self, request):
        # Your custom logic and rendering here
        context = dict(
            self.each_context(request),
            key_stats=Book.objects.count(),  # Example of passing context data
        )
        return TemplateResponse(request, "admin/my_custom_dashboard.html", context)

admin_site = MyAdminSite()


class PriceRangeFilter(SimpleListFilter):
    title = 'price range'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Low (< $20)'),
            ('medium', 'Medium ($20 - $50)'),       
            ('high', 'High (> $50)'),
        )
    def queryset(self, request, queryset):
        print(f"Filter value: {self.value()}")  # Debugging
        if self.value() == 'low':
            return queryset.filter(price__lt=20)
        if self.value() == 'medium':
            return queryset.filter(price__gte=20, price__lt=50)
        if self.value() == 'high':
            return queryset.filter(price__gte=50)
        return queryset
    


def mark_as_published(modeladmin, request, queryset):
    queryset.update(status='published')  # Assuming you have a status field

mark_as_published.short_description = "Mark selected books as published"    

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'publisher', 'price', 'stock')
    search_fields = ('title', 'author__name', 'publisher__name')
    list_filter = ('publication_date', 'author', 'publisher', 'price',PriceRangeFilter)
    ordering = ('-publication_date','price')  # Default ordering by publication_date descending
    list_per_page = 20  # Number of items per page
    actions = [mark_as_published]


admin.site.register(Book, BookAdmin)







class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography', 'dob')
    search_fields = ('name', 'biography', 'dob')
    list_filter = ('name', 'biography', 'dob')
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)





class publishadmin(admin.ModelAdmin):
    list_display = ('name','address','mobile')
    search_fields =  ('name','address','mobile')
    list_filter = ('name','address','mobile')

admin.site.register(Publisher,publishadmin)    