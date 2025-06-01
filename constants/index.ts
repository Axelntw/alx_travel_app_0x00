// API URLs
export const API_BASE_URL = 'https://api.example.com';
export const LISTINGS_ENDPOINT = `${API_BASE_URL}/listings`;

// UI Constants
export const CURRENCY_SYMBOL = '$';
export const DEFAULT_PAGINATION_LIMIT = 20;

// Filter Options
export const PROPERTY_TYPES = [
  'Apartment',
  'House',
  'Unique space',
  'Bed and breakfast',
  'Boutique hotel'
];

// Placeholder Data (for development)
export const SAMPLE_LISTINGS = [
  {
    id: 1,
    title: 'Cozy apartment in downtown',
    location: 'New York, NY',
    price: 120,
    rating: 4.8,
    image: '/assets/64f7c1f4b80255b1d9de659574de3ad943cdc204.png'
  },
  {
    id: 2,
    title: 'Modern loft with city view',
    location: 'San Francisco, CA',
    price: 200,
    rating: 4.9,
    image: '/assets/c811f30edfff8de9c9b079139dd9782018c7e7c0.jpg'
  }
];