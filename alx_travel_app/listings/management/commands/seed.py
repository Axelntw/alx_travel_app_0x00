import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from listings.models import Listing, Booking, Review
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            default=5,
            type=int,
            help='Number of users to create'
        )
        parser.add_argument(
            '--listings',
            default=20,
            type=int,
            help='Number of listings to create'
        )
        parser.add_argument(
            '--bookings',
            default=50,
            type=int,
            help='Number of bookings to create'
        )
        parser.add_argument(
            '--reviews',
            default=30,
            type=int,
            help='Number of reviews to create'
        )

    def handle(self, *args, **options):
        # Get the number of records to create
        num_users = options['users']
        num_listings = options['listings']
        num_bookings = options['bookings']
        num_reviews = options['reviews']

        self.stdout.write(self.style.SUCCESS(f'Starting to seed database with {num_users} users, {num_listings} listings, {num_bookings} bookings, and {num_reviews} reviews'))

        # Create admin user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        # Create users
        self.create_users(num_users)
        self.stdout.write(self.style.SUCCESS(f'Created {num_users} users'))

        # Create listings
        self.create_listings(num_listings)
        self.stdout.write(self.style.SUCCESS(f'Created {num_listings} listings'))

        # Create bookings
        self.create_bookings(num_bookings)
        self.stdout.write(self.style.SUCCESS(f'Created {num_bookings} bookings'))

        # Create reviews
        self.create_reviews(num_reviews)
        self.stdout.write(self.style.SUCCESS(f'Created {num_reviews} reviews'))

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))

    @transaction.atomic
    def create_users(self, count):
        """Create sample users"""
        for _ in range(count):
            username = fake.user_name()
            while User.objects.filter(username=username).exists():
                username = fake.user_name()

            User.objects.create_user(
                username=username,
                email=fake.email(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )

    @transaction.atomic
    def create_listings(self, count):
        """Create sample listings"""
        users = list(User.objects.all())
        property_types = [choice[0] for choice in Listing.PROPERTY_TYPES]
        cities = ['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco', 'Seattle', 'Boston', 'Austin']
        countries = ['United States']

        for _ in range(count):
            host = random.choice(users)
            city = random.choice(cities)
            property_type = random.choice(property_types)
            bedrooms = random.randint(1, 5)
            bathrooms = random.randint(1, 3)

            Listing.objects.create(
                title=fake.sentence(nb_words=6)[:-1],  # Remove period
                description=fake.paragraph(nb_sentences=5),
                address=fake.street_address(),
                city=city,
                country=random.choice(countries),
                price_per_night=random.randint(50, 500),
                property_type=property_type,
                max_guests=random.randint(1, 10),
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                has_wifi=random.choice([True, False]),
                has_kitchen=random.choice([True, False]),
                has_air_conditioning=random.choice([True, False]),
                has_heating=random.choice([True, False]),
                has_tv=random.choice([True, False]),
                has_parking=random.choice([True, False]),
                has_pool=random.choice([True, False]),
                host=host
            )

    @transaction.atomic
    def create_bookings(self, count):
        """Create sample bookings"""
        users = list(User.objects.all())
        listings = list(Listing.objects.all())
        statuses = [choice[0] for choice in Booking.STATUS_CHOICES]

        for _ in range(count):
            listing = random.choice(listings)
            guest = random.choice(users)
            
            # Ensure guest is not the host
            while guest == listing.host:
                guest = random.choice(users)

            # Generate random dates
            start_date = datetime.now().date() + timedelta(days=random.randint(-30, 60))
            duration = random.randint(1, 14)  # 1 to 14 nights
            end_date = start_date + timedelta(days=duration)

            # Calculate total price
            total_price = listing.price_per_night * duration

            Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in_date=start_date,
                check_out_date=end_date,
                guests_count=random.randint(1, listing.max_guests),
                total_price=total_price,
                status=random.choice(statuses)
            )

    @transaction.atomic
    def create_reviews(self, count):
        """Create sample reviews"""
        # Get completed bookings without reviews
        completed_bookings = Booking.objects.filter(
            status='completed'
        ).exclude(
            id__in=Review.objects.values_list('booking_id', flat=True)
        )

        # If there are not enough completed bookings, mark some as completed
        if completed_bookings.count() < count:
            bookings_to_update = Booking.objects.filter(
                status__in=['confirmed', 'pending']
            ).exclude(
                id__in=Review.objects.values_list('booking_id', flat=True)
            )[:count - completed_bookings.count()]
            
            for booking in bookings_to_update:
                booking.status = 'completed'
                booking.save()
            
            # Refresh the completed bookings queryset
            completed_bookings = Booking.objects.filter(
                status='completed'
            ).exclude(
                id__in=Review.objects.values_list('booking_id', flat=True)
            )

        # Create reviews for completed bookings
        bookings_for_review = list(completed_bookings[:count])
        
        for booking in bookings_for_review:
            Review.objects.create(
                listing=booking.listing,
                reviewer=booking.guest,
                booking=booking,
                rating=random.randint(1, 5),
                comment=fake.paragraph(nb_sentences=3)
            )