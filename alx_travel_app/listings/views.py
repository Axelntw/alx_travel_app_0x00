from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Listing instances"""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['city', 'country', 'property_type', 'max_guests', 'bedrooms', 'bathrooms',
                       'has_wifi', 'has_kitchen', 'has_air_conditioning', 'has_heating',
                       'has_tv', 'has_parking', 'has_pool']
    search_fields = ['title', 'description', 'address', 'city', 'country']
    ordering_fields = ['price_per_night', 'created_at']
    
    def perform_create(self, serializer):
        serializer.save(host=self.request.user)
    
    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        """Get all bookings for a listing"""
        listing = self.get_object()
        bookings = Booking.objects.filter(listing=listing)
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews for a listing"""
        listing = self.get_object()
        reviews = Review.objects.filter(listing=listing)
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Booking instances"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'listing', 'guest']
    ordering_fields = ['check_in_date', 'check_out_date', 'created_at']
    
    def get_queryset(self):
        """Filter bookings based on user role"""
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(guest=user) | Booking.objects.filter(listing__host=user)
    
    def get_permissions(self):
        """Set custom permissions for different actions"""
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            # For update, partial_update, destroy
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Review instances"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['listing', 'reviewer', 'rating']
    ordering_fields = ['rating', 'created_at']
    
    def get_permissions(self):
        """Set custom permissions for different actions"""
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated, IsBookingGuest]
        else:
            # For update, partial_update, destroy
            permission_classes = [permissions.IsAuthenticated, IsReviewerOrAdmin]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


# Custom permissions
class IsOwnerOrAdmin(permissions.BasePermission):
    """Custom permission to only allow owners of a booking or admins to edit it"""
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.guest == request.user


class IsReviewerOrAdmin(permissions.BasePermission):
    """Custom permission to only allow reviewers or admins to edit a review"""
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.reviewer == request.user


class IsBookingGuest(permissions.BasePermission):
    """Custom permission to only allow guests who have booked to leave a review"""
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True
        
        # Check if the user has a completed booking for the listing
        listing_id = request.data.get('listing')
        if not listing_id:
            return False
        
        return Booking.objects.filter(
            listing_id=listing_id,
            guest=request.user,
            status='completed'
        ).exists()