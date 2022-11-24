<template>
  <div>
    <div class="inner d-flex justify-content-center">
    <div class="star-rating row justify-content-around">
      <div
        class="star col-2"
        v-for="index in 5"
        :key="index"
        @click="check(index)"
        >
        <span v-if="index <= score">❤️</span>
        <span v-if="index > score">🤍</span>
      </div>
    </div>
  </div>
    <br>
    <p @click="RecordScore(movie)" title="Button push blue/green" class="button btnPush btnBlueGreen btn-align">하트 주기</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecordDetail',
  data() {
    return {
      score: null,
    }
  },
  methods: {
    RecordScore(movie) {
      const score = Number(this.score)
      const movie_pk = movie.id
      const payload = {
        score,
        movie_pk,
      }
      alert('하트를 성공적으로 보냈습니다!')
      this.$store.dispatch('RecordScore', payload)
    },
    getScored() {
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
          const movie_pk = this.movie.id
          return { user_pk: userId, movie_pk: movie_pk }
        })
        .then((res) => {
          axios({
            method: 'get',
            url: `${API_URL}/pages/score/${res.movie_pk}/${res.user_pk}`,
            headers: {
                Authorization: `Token ${ this.$store.state.token }`
            }
          })
            .then((res) => {
              if (res.status === 204) {
                this.score = 0
              } else {
                this.score = res.data.score
              }
            })
            .catch((err) => {
              console.log(err)
            })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    check(index) {
      this.score = index;
    },
  },
  props: {
    movie: Object
  },
  created() {
    this.getScored()
  }
}

</script>

<style>


.btn-align {
  position: relative !important;
  left: 20% !important;
  width: 60% !important;
}
</style>