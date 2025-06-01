from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    reviewer = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'listing', 'reviewer', 'booking', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model"""
    host = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'property_type', 'max_guests', 'bedrooms',
            'bathrooms', 'image', 'has_wifi', 'has_kitchen', 'has_air_conditioning',
            'has_heating', 'has_tv', 'has_parking', 'has_pool', 'created_at',
            'host', 'reviews', 'average_rating'
        ]
        read_only_fields = ['id', 'created_at', 'host']
    
    def get_average_rating(self, obj):
        """Calculate average rating for a listing"""
        reviews = obj.reviews.all()
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return None


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    guest = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(),
        write_only=True,
        source='listing'
    )
    review = ReviewSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_id', 'guest', 'check_in_date', 'check_out_date',
            'guests_count', 'total_price', 'status', 'created_at', 'review'
        ]
        read_only_fields = ['id', 'created_at', 'guest', 'total_price']
    
    def validate(self, data):
        """Validate booking data"""
        # Check if check_out_date is after check_in_date
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        
        # Check if guests_count is within listing's max_guests
        if data['guests_count'] > data['listing'].max_guests:
            raise serializers.ValidationError(f"This listing can only accommodate {data['listing'].max_guests} guests")
        
        # Check for booking conflicts
        listing = data['listing']
        check_in = data['check_in_date']
        check_out = data['check_out_date']
        
        # Exclude current booking when updating
        existing_bookings = Booking.objects.filter(
            listing=listing,
            status__in=['pending', 'confirmed'],
        )
        
        if self.instance:
            existing_bookings = existing_bookings.exclude(pk=self.instance.pk)
        
        for booking in existing_bookings:
            if (check_in <= booking.check_out_date and check_out >= booking.check_in_date):
                raise serializers.ValidationError("This listing is already booked for the selected dates")
        
        return data
    
    def create(self, validated_data):
        """Create a new booking and calculate total price"""
        # Calculate number of nights
        nights = (validated_data['check_out_date'] - validated_data['check_in_date']).days
        
        # Calculate total price
        validated_data['total_price'] = validated_data['listing'].price_per_night * nights
        
        # Set the guest to the current user
        validated_data['guest'] = self.context['request'].user
        
        return super().create(validated_data)