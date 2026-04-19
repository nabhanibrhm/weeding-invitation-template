/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'mulyo-cream': '#FDFBF7',
        'mulyo-gold': '#D4AF37',
        'mulyo-charcoal': '#333333',
        'mulyo-light': '#F4F1EA',
      },
      fontFamily: {
        'playfair': ['"Playfair Display"', 'serif'],
        'sans': ['Inter', 'sans-serif'],
      },
      animation: {
        'float': 'float 10s ease-in-out infinite',
        'slide-up': 'slideUp 1s ease-out forwards',
        'fade-in': 'fadeIn 1.5s ease-out forwards',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0) scale(1)' },
          '50%': { transform: 'translateY(-2%) scale(1.02)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(50px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        }
      }
    },
  },
  plugins: [],
}
