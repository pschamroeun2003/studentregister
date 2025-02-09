import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import AboutPage from '../views/AboutPage.vue';
import ContactPage from '../views/ContactPage.vue';
import CoursePageVue from '../views/CoursePage.vue';
import HomePage from '../views/HomePage.vue';
import ServicesPage from '../views/ServicesPage.vue';
import StudentPage from '../views/StudentPage.vue';

// Define the routes
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage
  },
  {
    path: '/services',
    name: 'Services',
    component: ServicesPage
  },
  {
    path: '/contact',
    name: 'Contact',
    component: ContactPage
  },
  {
      path: '/student',
      name: 'Student',
      component:StudentPage
  },
  {
    path: '/course',
    name: 'Course',
    component: CoursePageVue
  }
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
