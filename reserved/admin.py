from django.contrib import admin
from models import SiteText, NamedObject, Addition, Category, Product, Timing, OpeningTime, Menu, Location, Customer, TelephoneType, Telephone, Company, Venue, Booking, Event

class SiteTextAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', )
    list_filter = ('name', 'value', )
    search_fields = ('name', 'value', )
    #fields = ('name', 'value', )
    filter_horizontal = ()
    #exclude = (,)

class NamedObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', )
    list_filter = ('name', 'icon_name', 'active', 'description', )
    search_fields = ('name', 'icon_name', 'active', 'description', )
    #fields = ('name', 'icon_name', 'active', 'description', )
    filter_horizontal = ()
    #exclude = (,)

class AdditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'min_count', 'max_count', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'min_count', 'max_count', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'min_count', 'max_count', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'min_count', 'max_count', )
    filter_horizontal = ()
    #exclude = (,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'parent', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'parent', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'parent', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'parent', )
    filter_horizontal = ()
    #exclude = (,)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'price', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'price', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'price', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'price', )
    filter_horizontal = ()
    #exclude = (,)

class TimingAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', )
    filter_horizontal = ()
    #exclude = (,)

class OpeningTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', 'timing_ptr', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', 'timing_ptr', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', 'timing_ptr', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', 'start_date', 'end_date', 'active_time', 'deactive_time', 'timing_ptr', )
    filter_horizontal = ()
    #exclude = (,)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', )
    list_filter = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', )
    search_fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', )
    #fields = ('name', 'icon_name', 'active', 'description', 'namedobject_ptr', )
    filter_horizontal = ()
    #exclude = (,)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'computed_address', 'latitude', 'longitude', 'geocode_error', 'address_ptr', 'name', 'location_id', )
    list_filter = ('address', 'computed_address', 'latitude', 'longitude', 'geocode_error', 'address_ptr', 'name', 'location_id', )
    search_fields = ('address', 'computed_address', 'latitude', 'longitude', 'geocode_error', 'address_ptr', 'name', 'location_id', )
    #fields = ('address', 'computed_address', 'latitude', 'longitude', 'geocode_error', 'address_ptr', 'name', 'location_id', )
    filter_horizontal = ()
    #exclude = (,)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    list_filter = ('name', 'email', )
    search_fields = ('name', 'email', )
    #fields = ('name', 'email', )
    filter_horizontal = ()
    #exclude = (,)

class TelephoneTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    #fields = ('name', )
    filter_horizontal = ()
    #exclude = (,)

class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'number', )
    list_filter = ('name', 'owner', 'number', )
    search_fields = ('name', 'owner', 'number', )
    #fields = ('name', 'owner', 'number', )
    filter_horizontal = ()
    #exclude = (,)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    #fields = ('name', )
    filter_horizontal = ()
    #exclude = (,)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'company', 'owner', )
    list_filter = ('name', 'address', 'company', 'owner', )
    search_fields = ('name', 'address', 'company', 'owner', )
    #fields = ('name', 'address', 'company', 'owner', )
    filter_horizontal = ()
    #exclude = (,)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated', 'arrival', 'depature', 'company', 'status', )
    list_filter = ('name', 'created', 'updated', 'arrival', 'depature', 'company', 'status', )
    search_fields = ('name', 'created', 'updated', 'arrival', 'depature', 'company', 'status', )
    #fields = ('name', 'created', 'updated', 'arrival', 'depature', 'company', 'status', )
    filter_horizontal = ()
    #exclude = (,)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'start_time', 'end_time', )
    list_filter = ('name', 'company', 'start_time', 'end_time', )
    search_fields = ('name', 'company', 'start_time', 'end_time', )
    #fields = ('name', 'company', 'start_time', 'end_time', )
    filter_horizontal = ()
    #exclude = (,)



admin.site.register(SiteText, SiteTextAdmin)
admin.site.register(NamedObject, NamedObjectAdmin)
admin.site.register(Addition, AdditionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Timing, TimingAdmin)
admin.site.register(OpeningTime, OpeningTimeAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(TelephoneType, TelephoneTypeAdmin)
admin.site.register(Telephone, TelephoneAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Event, EventAdmin)

