/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
  // Explicitly use Pages Router
  reactStrictMode: true,
  swcMinify: true,
  // Ensure no app directory features are used
  pageExtensions: ['tsx', 'ts', 'jsx', 'js']
};

module.exports = nextConfig;
