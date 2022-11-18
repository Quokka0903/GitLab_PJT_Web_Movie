import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '@/views/StartView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import MovieView from '@/views/MainView'
import ChangeView from '@/views/ChangeView'
import ProfileView from '@/views/ProfileView'
import OnBoardingView from '@/views/OnBoardingView'
import RecordView from '@/views/RecordView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'StartView',
    component: StartView
  },
  {
    path: '/onboarding',
    name: 'OnBoardingView',
    component: OnBoardingView
  },
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
    path: '/main',
    name: 'MainView',
    component: MovieView
  },
  {
    path: '/password',
    name: 'ChangeView',
    component: ChangeView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/record',
    name: 'RecordView',
    component: RecordView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
