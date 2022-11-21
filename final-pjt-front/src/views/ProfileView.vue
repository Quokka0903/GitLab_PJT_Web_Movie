<template>
<div>
  <br>
  <h3>{{username}} 님 환영합니다!</h3>
  <br>
  <br>
  <hr>
  <div @click="LogOut">
    <p>로그아웃</p>
  </div>
  <hr>
  <div @click="GoMovie">
    <p>내가 평점 준 영화</p>
  </div>
  <hr>
  <div @click="GoReview">
    <p>내가 남긴 리뷰</p>
  </div>
  <hr>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileView',
  data() {
    return {
      user_id: null,
      username: null
    }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('logOut')
    },
    GoMovie() {
      const user_id = this.user_id
      this.$router.push({name:'MyMovieView', params: {user_id}})
    },
    GoReview() {
      const user_id = this.user_id
      this.$router.push({name:'MyReviewView', params: {user_id}})
    },
    GetUserId() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.user_id = res.data.pk
          this.username = res.data.username
        })
    }
  },
  created() {
    this.GetUserId()
  }

}
</script>

<style>

</style>