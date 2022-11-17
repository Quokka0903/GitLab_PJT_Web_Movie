import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import MovieView from '@/views/MovieView'
import ChangeView from '@/views/ChangeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/password',
    name: 'ChangeView',
    component: ChangeView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
