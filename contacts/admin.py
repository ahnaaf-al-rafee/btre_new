from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('listing', 'name', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
