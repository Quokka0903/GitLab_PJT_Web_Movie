import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '@/views/StartView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import MainView from '@/views/MainView'
import ChangeView from '@/views/ChangeView'
import ProfileView from '@/views/ProfileView'
// import CinemaLocation from '@/views/CinemaLocation'
// import RecordView from '@/views/RecordView'
import IndexNav from '@/views/IndexNav'
import IndexNotNav from '@/views/IndexNotNav'
// import MovieDetail from '@/views/MovieDetail'
import ReviewListView from '@/views/ReviewListView'
import MyMovieView from '@/views/MyMovieView'
import MyReviewView from '@/views/MyReviewView'
import SearchView from '@/views/SearchView'
import NotFound from '@/views/NotFound'

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
      component: () => import('../views/MovieDetail.vue'),
    }]
  },
  {
    path: '/mymovie/:user_id',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'MyMovieView',
      component: MyMovieView,
    }]
  },
  {
    path: '/myreview/:user_id',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'MyReviewView',
      component: MyReviewView,
    }]
  },
  {
    path: '/reviews/:movie_id',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'ReviewListView',
      component: ReviewListView,
    }]
  },
  {
    path: '/password',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'ChangeView',
      component: ChangeView,
    }]
  },
  // 여기까지 Nav Bar 노출/비노출 적용한 라우터들입니다
  {
    path: '/cinema',
    name: 'CinemaLocation',
    component: () => import('../views/CinemaLocation.vue')
  },
  {
    path: '/record',
    name: 'RecordView',
    component: () => import('../views/RecordView.vue')
  },

  {
    path: '/search',
    name: '',
    component: IndexNav,
    children: [{
      path: '/',
      name: 'SearchView',
      component: SearchView,
    }]
  },
  // {
  //   path: '/ost/:moviename',
  //   name: 'MovieOstView',
  //   component: () => import('../views/MovieOstView.vue')
  // },
  { 
    path: '*',
    redirect: '/404',
    component: NotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
