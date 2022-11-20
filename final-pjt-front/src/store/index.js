import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

import _ from 'lodash'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    recommend: [],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MainView' })
    },
    DELETE_TOKEN(state) {
      state.token = null
      router.push({ name: 'LoginView'})
    },
    GET_MOVIES(state, movies) {
      state.movies =movies
    },
    GET_RECOMMEND(state, recommend) {
      state.recommend =recommend
      // console.log(state.recommend)
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/pages/movies`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getRecommend(context) {
      axios({
        method: 'get',
        url: `${API_URL}/pages/algo`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          res.data = _.sampleSize(res.data, 4)
          context.commit('GET_RECOMMEND', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log('token', res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    login(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          console.log('로그인')
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    change(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1: payload.newpassword,
          new_password2: payload.newpassword2,
          // old_password: payload.original,
        },
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log('로그아웃', res)
          context.commit('DELETE_TOKEN')
        })
        .catch((err) => {
          console.log(err)
        }) 
    },
    RecordScore(context, payload) {
      console.log('payload', payload)
      axios({
        method: 'post',
        url:`${API_URL}/pages/score/`,
        data: {
          score: payload.score,
          movie_pk: payload.movie_pk,
          // user: payload.userId
        },
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res)=> {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
