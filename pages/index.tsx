import type { NextPage } from 'next';
import Head from 'next/head';
import Button from '../components/common/Button';
import Card from '../components/common/Card';
import { SAMPLE_LISTINGS } from '../constants';

const Home: NextPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <Head>
        <title>ALX Listing App</title>
        <meta name="description" content="Airbnb clone listing page" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className="text-3xl font-bold text-center mb-8">
          Welcome to ALX Listing App
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {SAMPLE_LISTINGS.map((listing) => (
            <Card key={listing.id}>
              <div className="relative h-48 w-full">
                <div className="absolute inset-0 bg-gray-200 flex items-center justify-center">
                  <p>Listing Image Placeholder</p>
                </div>
              </div>
              <div className="p-4">
                <h2 className="font-bold text-lg">{listing.title}</h2>
                <p className="text-gray-600">{listing.location}</p>
                <p className="font-semibold mt-2">${listing.price} / night</p>
                <div className="mt-4">
                  <Button>View Details</Button>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </main>
    </div>
  );
};

export default Home;