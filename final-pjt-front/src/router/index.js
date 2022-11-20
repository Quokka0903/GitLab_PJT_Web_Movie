import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '@/views/StartView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import MainView from '@/views/MainView'
import ChangeView from '@/views/ChangeView'
import ProfileView from '@/views/ProfileView'
import OnBoardingView from '@/views/OnBoardingView'
import RecordView from '@/views/RecordView'
import IndexNav from '@/views/IndexNav'
import IndexNotNav from '@/views/IndexNotNav'
import MovieDetail from '@/views/MovieDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: '',
    component: IndexNotNav,
    children: [{
      path: '/',
      name: 'StartView',
      component: StartView,
    }]
  },
  {
    path: '/signup',
    name: '',
    component: IndexNotNav,
    children: [{
      path: '/',
      name: 'SignUpView',
      component: SignUpView,
    }]
  },

  {
    path: '/login',
    name: '',
    component: IndexNotNav,
    children: [{
      path: '/',
      name: 'LoginView',
      component: LoginView,
    }]
  },
  {
    path: '/main',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'MainView',
      component: MainView,
    }]
  },
  {
    path: '/profile',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'ProfileView',
      component: ProfileView,
    }]
  },
  {
    path: '/movie/:id',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'MovieDetail',
      component: MovieDetail,
    }]
  },
  // 여기까지 Nav Bar 노출/비노출 적용한 라우터들입니다
  {
    path: '/onboarding',
    name: 'OnBoardingView',
    component: OnBoardingView
  },
  {
    path: '/password',
    name: 'ChangeView',
    component: ChangeView
  },
  {
    path: '/record',
    name: 'RecordView',
    component: RecordView
  },
  
  

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
