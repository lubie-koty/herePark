import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    port: 8000
  },
  optimizeDeps: {
    include: [
        "vue-google-maps-community-fork",
        "fast-deep-equal",
    ],
  }
})
