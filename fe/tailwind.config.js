/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
        'serif': ['Playfair Display', 'serif'],
        'elegant': ['Cinzel', 'serif'],
        'script': ['Dancing Script', 'cursive'],
      },
    },
  },
  plugins: [],
};
