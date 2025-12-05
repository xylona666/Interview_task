import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Events from '../views/Events.vue';
import AddEvent from '../views/AddEvent.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/events', name: 'Events', component: Events },
  { path: '/add-event', name: 'AddEvent', component: AddEvent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 