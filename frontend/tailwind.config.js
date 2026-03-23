/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",   // (optional, safe)
    "./components/**/*.{js,ts,jsx,tsx}", // (future use)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}