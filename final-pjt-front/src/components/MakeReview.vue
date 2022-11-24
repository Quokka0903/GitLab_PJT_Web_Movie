<template>
  <div>
    <b-input v-model="title" placeholder="리뷰 제목"></b-input>
    <b-textarea
    placeholder="당신만의 한 줄을 남겨주세요"
    v-model="context"
    ></b-textarea>
    <b-button @click="createReview(movie)">리뷰 남기기</b-button>
    <b-button @click="GoReview(movie.id)">리뷰 더보기</b-button>
  </div>
</template>

<script>
import axios from 'axios'
// import ReviewDetail from '@/components/ReviewDetail'

export default {
    name: "MakeReview",
    data() {
    return {
        title: '',
        context: '',
        // reviews: [],
        API_URL: 'http://127.0.0.1:8000',
    }
  },
  methods: {
    createReview(movie) {
        console.log('리뷰 남기기')
      const movie_id = movie.id
      axios({
        method: 'post',
        url: `${this.API_URL}/pages/movies/${movie_id}/reviews/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        },
        data: {
            movie: movie.id,
            title: this.title,
            content: this.context,
        }
      })
        .then((res) => {
            console.log('리뷰', res)
            this.title = ''
            this.context = ''
        })
        .catch((err) => {
          console.log(err)
        })
    },
    GoReview(movie_id) {
      this.$router.push({name: 'ReviewListView', params: {movie_id: movie_id}})
    },
  },
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>