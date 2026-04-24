/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'surface': '#fff8f2',
        'surface-dim': '#e1d9cf',
        'surface-bright': '#fff8f2',
        'surface-container-lowest': '#ffffff',
        'surface-container-low': '#fbf2e8',
        'surface-container': '#f5ede3',
        'surface-container-high': '#efe7dd',
        'surface-container-highest': '#e9e1d7',
        'on-surface': '#1e1b15',
        'on-surface-variant': '#414849',
        'inverse-surface': '#343029',
        'inverse-on-surface': '#f8f0e5',
        'outline': '#72787a',
        'outline-variant': '#c1c8c9',
        'surface-tint': '#466368',
        'primary': '#466368',
        'on-primary': '#ffffff',
        'primary-container': '#b4d3d9',
        'on-primary-container': '#3f5c61',
        'inverse-primary': '#adccd2',
        'secondary': '#62578c',
        'on-secondary': '#ffffff',
        'secondary-container': '#cfc1fd',
        'on-secondary-container': '#584d81',
        'tertiary': '#6a577a',
        'on-tertiary': '#ffffff',
        'tertiary-container': '#ddc5ee',
        'on-tertiary-container': '#635073',
        'error': '#ba1a1a',
        'on-error': '#ffffff',
        'error-container': '#ffdad6',
        'on-error-container': '#93000a',
        'background': '#fff8f2',
        'on-background': '#1e1b15',
        'surface-variant': '#e9e1d7'
      },
      fontFamily: {
        'serif': ['"Noto Serif"', 'serif'],
        'sans': ['Manrope', 'sans-serif'],
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
