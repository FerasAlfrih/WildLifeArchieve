import { createRouter, createWebHistory } from 'vue-router'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/plants',
    name: 'Plants',
    component: () => import('../views/plants.vue')

  },
  {
    path: '/animals',
    name: 'Animals',
    component: () => import('../views/animals.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    
    path: '/animals/:animal_slug',
    name: 'Animal',
    component: () => import('../views/animal.vue')

  },  {
    
    path: '/plants/:plant_slug',
    name: 'Plant',
    component: () => import('../views/plant.vue')

  }, 
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
