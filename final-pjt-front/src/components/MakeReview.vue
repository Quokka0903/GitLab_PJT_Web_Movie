<template>
  <div>
    <!-- <ReviewDetail
      v-for="(review, index) in reviews"
      :review='review'
      :key="index"
      /> -->
    <input type="text" v-model="title" placeholder="리뷰 제목">
    <textarea
    placeholder="당신만의 한 줄을 남겨주세요"
    v-model="context"
    ></textarea>
    <button @click="createReview(movie)">리뷰 남기기</button>
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
        reviews: [],
        API_URL: 'http://127.0.0.1:8000',
    }
  },
  component: {
    // ReviewDetail,
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
            console.log(res)
            this.title = ''
            this.context = ''
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // ReadReview(movie) {
    //     console.log('리뷰목록 불러오기')
    //     const movie_id = movie.id
    //     axios({
    //         method: 'get',
    //         url: `${this.API_URL}/pages/movies/${movie_id}/reviews/`,
    //     })
    // }
  },
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>