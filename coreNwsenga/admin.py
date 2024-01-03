from django.contrib import admin

from coreNwsenga.models import City, Country, Neighborhood, Buy, Bill

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Neighborhood)
# admin.site.register(Buy)
admin.site.register(Bill)


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'city', 'country', 'neighborhood', 'owner_name', 'date', 'update_date')
    search_fields = ('area', 'direction')
    list_filter = ('city', 'country', 'neighborhood', 'type', 'bill')

    fieldsets = [
        ('Buy Information', {
            'fields': (
                "type",
                "city",
                "country",
                "neighborhood",
                "area",
                "documentation",
                "direction",
                "max_price",
                "min_price",
                "owner_name",
                "owner_phone",
                "notes",
                "link",
            ),
        }),
        ('Pswla Information', {
            'fields': ('bill', 'installment', 'advance_payment'),
            'classes': ('collapse',),  # Fields under this section will be collapsed by default
        }),
        ('Bax Information', {
            'fields': ('fence', 'electric', 'water', 'water_depth', 'house', 'tree'),
            'classes': ('collapse',),  # Fields under this section will be collapsed by default
        }),
    ]
