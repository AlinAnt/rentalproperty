from django.contrib import admin

# Register your models here.
from .models import Area, TypeArea, Communication


#admin.site.register(Area)
#admin.site.register(TypeArea)
admin.site.register(Communication)


class AreaInline(admin.TabularInline):
    model = Area


@admin.register(TypeArea)
class TypeAreaAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [AreaInline]


class AreaAdmin(admin.ModelAdmin):
    list_display = ('square', 'typeArea', 'rent', 'price', 'floor', 'display_communication')
    list_filter = ('status', 'typeArea')

    fieldsets = (
        ('Main', {
            'fields': ('square', 'typeArea', 'price')
        }),
        ('Detail', {
            'fields': ('floor', 'communication', 'address', 'status', 'endOfRental', 'rent', 'begofRental')
        }),
    )


admin.site.register(Area, AreaAdmin)



