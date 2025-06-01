from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country', 'property_type', 'price_per_night', 'host', 'created_at')
    list_filter = ('property_type', 'city', 'country', 'has_wifi', 'has_kitchen', 'has_air_conditioning',
                  'has_heating', 'has_tv', 'has_parking', 'has_pool')
    search_fields = ('title', 'description', 'address', 'city', 'country', 'host__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'host', 'image')
        }),
        ('Location', {
            'fields': ('address', 'city', 'country')
        }),
        ('Property Details', {
            'fields': ('property_type', 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms')
        }),
        ('Amenities', {
            'fields': ('has_wifi', 'has_kitchen', 'has_air_conditioning', 'has_heating',
                      'has_tv', 'has_parking', 'has_pool')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'guest', 'check_in_date', 'check_out_date', 'status', 'total_price')
    list_filter = ('status', 'check_in_date', 'check_out_date')
    search_fields = ('listing__title', 'guest__username', 'guest__email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Booking Information', {
            'fields': ('listing', 'guest', 'status')
        }),
        ('Dates and Guests', {
            'fields': ('check_in_date', 'check_out_date', 'guests_count')
        }),
        ('Financial', {
            'fields': ('total_price',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'reviewer', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('listing__title', 'reviewer__username', 'comment')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Review Information', {
            'fields': ('listing', 'reviewer', 'booking')
        }),
        ('Review Content', {
            'fields': ('rating', 'comment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )