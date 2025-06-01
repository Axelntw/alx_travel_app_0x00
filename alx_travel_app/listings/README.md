# Listings App

This Django app provides a RESTful API for managing property listings, bookings, and reviews for the ALX Travel App.

## Models

### Listing

Represents a property listing with the following fields:

- `title`: The title of the listing
- `description`: Detailed description of the property
- `address`: Street address
- `city`: City name
- `country`: Country name
- `price_per_night`: Cost per night in decimal format
- `property_type`: Type of property (apartment, house, villa, cabin, condo, other)
- `max_guests`: Maximum number of guests allowed
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `image`: Optional image of the property
- Amenities: Boolean fields for various amenities (wifi, kitchen, air conditioning, etc.)
- `host`: Foreign key to User model representing the property owner
- Timestamps: `created_at` and `updated_at`

### Booking

Represents a booking made by a user for a specific listing:

- `listing`: Foreign key to Listing model
- `guest`: Foreign key to User model representing the guest
- `check_in_date`: Date of check-in
- `check_out_date`: Date of check-out
- `guests_count`: Number of guests for this booking
- `total_price`: Total price calculated based on nights and listing price
- `status`: Current status (pending, confirmed, cancelled, completed)
- Timestamps: `created_at` and `updated_at`

### Review

Represents a review left by a guest for a listing:

- `listing`: Foreign key to Listing model
- `reviewer`: Foreign key to User model representing the reviewer
- `booking`: One-to-one relationship with Booking model
- `rating`: Rating from 1 to 5
- `comment`: Text review
- Timestamps: `created_at` and `updated_at`

## Serializers

### ListingSerializer

Serializes Listing model with nested host and reviews data. Includes a calculated `average_rating` field.

### BookingSerializer

Serializes Booking model with nested guest and listing data. Includes validation for:
- Check-out date must be after check-in date
- Guest count must not exceed listing's max_guests
- No booking conflicts with existing bookings

### ReviewSerializer

Serializes Review model with nested reviewer data.

## API Endpoints

### Listings

- `GET /api/listings/`: List all listings with filtering and search options
- `POST /api/listings/`: Create a new listing (authenticated users only)
- `GET /api/listings/{id}/`: Retrieve a specific listing
- `PUT /api/listings/{id}/`: Update a listing (owner only)
- `DELETE /api/listings/{id}/`: Delete a listing (owner only)
- `GET /api/listings/{id}/bookings/`: Get all bookings for a listing
- `GET /api/listings/{id}/reviews/`: Get all reviews for a listing

### Bookings

- `GET /api/bookings/`: List user's bookings (as guest or host)
- `POST /api/bookings/`: Create a new booking (authenticated users only)
- `GET /api/bookings/{id}/`: Retrieve a specific booking
- `PUT /api/bookings/{id}/`: Update a booking (owner or admin only)
- `DELETE /api/bookings/{id}/`: Delete a booking (owner or admin only)

### Reviews

- `GET /api/reviews/`: List all reviews
- `POST /api/reviews/`: Create a new review (only for completed bookings)
- `GET /api/reviews/{id}/`: Retrieve a specific review
- `PUT /api/reviews/{id}/`: Update a review (reviewer or admin only)
- `DELETE /api/reviews/{id}/`: Delete a review (reviewer or admin only)

## Filtering and Searching

### Listings

- Filter by city, country, property type, amenities, etc.
- Search by title, description, address, city, country
- Order by price or creation date

### Bookings

- Filter by status, listing, guest
- Order by check-in date, check-out date, creation date

### Reviews

- Filter by listing, reviewer, rating
- Order by rating, creation date

## Seed Command

The app includes a management command to populate the database with sample data.

### Usage

```bash
python manage.py seed [options]
```

### Options

- `--users`: Number of users to create (default: 5)
- `--listings`: Number of listings to create (default: 20)
- `--bookings`: Number of bookings to create (default: 50)
- `--reviews`: Number of reviews to create (default: 30)

### Example

```bash
python manage.py seed --users 10 --listings 30 --bookings 100 --reviews 50
```

This will create:
- 10 random users
- 30 property listings
- 100 bookings with various statuses
- 50 reviews for completed bookings

An admin user is also created with:
- Username: admin
- Email: admin@example.com
- Password: admin123