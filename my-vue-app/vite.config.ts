import vue from '@vitejs/plugin-vue';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // Allow access on any network interface
    port: 5001,       // Change the port to 5000
    strictPort: true, // Ensure Vite uses exactly port 5000 (fails if the port is in use)
  },
});
