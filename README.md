# ALX Travel App

A modern Airbnb clone application with a Next.js frontend and Django REST Framework backend. This project aims to recreate the listing page functionality of Airbnb, providing users with a clean and intuitive interface to browse property listings.

## Project Structure

### Frontend (Next.js)

- **pages/**: Contains all the page components using Next.js Pages Router
  - `index.tsx`: The home page displaying property listings
  
- **components/**: Reusable UI components
  - **common/**: Basic UI components used throughout the application
    - `Button.tsx`: Reusable button component with various styles
    - `Card.tsx`: Card component for displaying property information
  
- **interfaces/**: TypeScript interfaces for type safety
  - `index.ts`: Contains interfaces like CardProps and ButtonProps
  
- **constants/**: Application constants and configuration
  - `index.ts`: Contains API URLs, UI constants, and sample data
  
- **public/assets/**: Static assets like images and icons
  - Contains property images and UI icons exported from Figma

- **styles/**: Global styles and Tailwind CSS configuration
  - `globals.css`: Contains Tailwind imports

### Backend (Django)

- **alx_travel_app/**: Main Django project directory
  - `settings.py`: Project settings and configuration
  - `urls.py`: Main URL routing
  - `wsgi.py` & `asgi.py`: Web server entry points

- **listings/**: Django app for property listings
  - `models.py`: Database models (Listing, Booking, Review)
  - `serializers.py`: REST API serializers
  - `views.py`: API views and endpoints
  - `urls.py`: URL routing for the listings app
  - `admin.py`: Django admin configuration
  - **management/commands/**: Custom management commands
    - `seed.py`: Command to populate the database with sample data

## Getting Started

### Prerequisites

- Node.js 14.x or later
- Python 3.8 or later
- npm or yarn
- pip

### Frontend Installation

Run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Backend Installation

1. Navigate to the backend directory:

```bash
cd alx_travel_app
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Seed the database with sample data:

```bash
python manage.py seed
```

7. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000/api/](http://localhost:8000/api/)

The admin interface will be available at [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Learn More

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Django Documentation](https://docs.djangoproject.com/) - learn about Django.
- [Django REST Framework](https://www.django-rest-framework.org/) - learn about DRF.

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.
