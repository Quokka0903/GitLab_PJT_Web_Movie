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
    // movies: [],
    recommend: [],
    token: null,
    selected: true
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
      console.log(state.selected)
      if (state.selected) {
        router.push({ name: 'MainView' })
      } else {
        router.push({name: 'RecordView'})
      }
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.selected = true
      state.recommend = []
      router.push({ name: 'StartView'})
    },
    GET_RECOMMEND(state, recommend) {
      state.recommend =recommend
    },
    CHANGE_CHECKED(state) {
      state.selected = false
    }
  },
  actions: {
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
          context.commit('CHANGE_CHECKED')
          context.commit('SAVE_TOKEN', res.data.key) 
        })
        .catch((err) => {
          console.log(err)
          alert('이미 존재하는 아이디거나 비밀번호가 서로 다릅니다!')
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
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
          alert('존재하지 않는 계정이거나 잘못된 비밀번호 입니다!')
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
        .then(() => {
          context.commit('DELETE_TOKEN')
          alert('비밀번호가 변경되었습니다. 다시 로그인하세요.')
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
    DeleteUser(context, user_id) {
      console.log('전달받음')
      console.log(user_id)
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'delete',
        url: `${API_URL}/infos/profile/${user_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(() => {
          alert('회원탈퇴 되었습니다!')
          context.commit('DELETE_TOKEN')
        })
        .catch((err) => {
          console.log(err)
          
        })
    }
  },
  modules: {
  }
})
