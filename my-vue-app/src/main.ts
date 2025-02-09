import { createApp } from 'vue';
import App from './App.vue';
import './assets/tailwind.css';
import router from './router'; // Import the router configuration
createApp(App)
  .use(router)  // Tell Vue to use the router
  .mount('#app');
