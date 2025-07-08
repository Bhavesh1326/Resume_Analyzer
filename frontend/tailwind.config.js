export default {
  darkMode: "class",
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        orange: {
          50: '#fff7ed',
          100: '#fef3e7',
          200: '#fde6c0',
          300: '#fbd39a',
          400: '#f9c274',
          500: '#f8b150',
          600: '#d9913d',
          700: '#b0712a',
          800: '#875117',
          900: '#5e3104',
        },
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
