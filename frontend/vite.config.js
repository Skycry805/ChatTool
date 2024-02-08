import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base:"https://chat.niclas-sieveneck.de",

  server: {
    proxy: {
      '/api': {
        target: 'https://chat.niclas-sieveneck.de',
        changeOrigin: true,
      }
    }
  }
})
