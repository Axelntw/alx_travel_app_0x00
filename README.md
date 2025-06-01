# ALX Listing App

A modern Airbnb clone application built with Next.js and TypeScript. This project aims to recreate the listing page functionality of Airbnb, providing users with a clean and intuitive interface to browse property listings.

## Project Structure

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

## Getting Started

### Prerequisites

- Node.js 14.x or later
- npm or yarn

### Installation

1. Clone the repository:

First, run the development server:

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

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
