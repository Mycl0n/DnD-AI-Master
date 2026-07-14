/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f5f7ff',
          100: '#e9edff',
          200: '#d2d8ff',
          300: '#b7c0ff',
          400: '#94a1ff',
          500: '#6e7dff',
          600: '#4f60ff',
          700: '#3647e6',
          800: '#2733ad',
          900: '#1a236f'
        }
      }
    }
  },
  plugins: []
}

