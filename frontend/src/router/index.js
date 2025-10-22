import { createRouter, createWebHistory } from 'vue-router'

import ProductsView from '../views/ProductsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/products',
      name: 'products-view',
      component: ProductsView,
    },
  ],
})

export default router
