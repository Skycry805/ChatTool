import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base:"https://chat.niclas-sieveneck.de",

  server: {
    proxy: {
      '/send_message_to_server': {
        target: '127.0.0.1:5000',
        changeOrigin: true,
      }
    }
  }
})
