from django.contrib import admin
from .models import Stock, City


class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ("product", "city", "quantity")
    search_fields = ("product", "city", "quantity")
    list_display_links = ("product", "city", "quantity")


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = (
        "city_name",
        "state_name",
        "country"
    )
    search_fields = ("city_name", "state_name", "country")
    list_display_links = ("city_name", "state_name", "country")


admin.site.register(Stock, StockAdmin)
admin.site.register(City, CityAdmin)
