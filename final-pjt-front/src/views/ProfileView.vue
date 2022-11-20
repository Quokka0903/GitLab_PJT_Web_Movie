<template>
  <div>
    <p @click="LogOut">로그아웃</p>
    <p>내가 평점 준 영화</p>
    <p>{{my_movies}}</p>
    <p>내가 남긴 리뷰</p>
    <p>{{my_reviews}}</p>
    <!-- <p v-for="review in my_reviews"
    :key= review.id>{{review?.title}}</p> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileView',
  data() {
    return {
      my_movies: [],
      my_reviews: [],
    }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('logOut')
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
          const userId = res.data.pk
          return { user_id: userId}
        })
        .then((res) => {
          //  console.log(res)
          axios({
            method: 'get',
            url: `${API_URL}/infos/profile/${res.user_id}`,
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              this.my_reviews = res.data.my_reviews
              this.my_movies = res.data.my_movies
            })
        })
        .catch((err) => {
          console.log(err)
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