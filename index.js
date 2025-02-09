import { createRouter, createWebHistory } from 'vue-router';

// Import your components or views for the routes
import Dashboard from '@/views/Dashboard.vue';
import Kanban from '@/views/Kanban.vue';
import Inbox from '@/views/Inbox.vue';
import Users from '@/views/Users.vue';
import Products from '@/views/Products.vue';
import SignIn from '@/views/SignIn.vue';
import SignUp from '@/views/SignUp.vue';

// Define the routes
const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard,
  },
  {
    path: '/kanban',
    name: 'kanban',
    component: Kanban,
  },
  {
    path: '/inbox',
    name: 'inbox',
    component: Inbox,
  },
  {
    path: '/users',
    name: 'users',
    component: Users,
  },
  {
    path: '/products',
    name: 'products',
    component: Products,
  },
  {
    path: '/sign-in',
    name: 'sign-in',
    component: SignIn,
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUp,
  },
];

// Create the Vue Router instance
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
