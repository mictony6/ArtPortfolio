from django.contrib import admin

from pages.models import ArtWork, Request


class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    orderering = ['id']
    list_filter = ['featured', 'date']

    actions = ['set_featured', 'unfeature']

    def set_featured(modeladmin, request, queryset):
        queryset.update(featured=True)

    def unfeature(modeladmin, request, queryset):
        queryset.update(featured=False)


# Register your models here.
admin.site.register(ArtWork, ArtWorkAdmin)
admin.site.register(Request)
