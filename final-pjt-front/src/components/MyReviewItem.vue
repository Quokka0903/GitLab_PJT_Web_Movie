<template>
  <div class="card reviewcard col-lg-6 col-md-12"> 
      <div class="row"> 
        <div class="col-4"> 
        <img :src="`https://image.tmdb.org/t/p/original/${review.movie_poster}`" 
        class="card-img-top"
        @click="MoveDetail(review.movie_id)">
        <h5 class="reviewtitle">{{review.movie_title}}</h5>
      </div>
      <div class="reviewitem col-8">
        <h4>리뷰 제목</h4>
        <h5>{{review.title}}</h5>
        <br>
        <h4>리뷰 내용</h4>
        <p>{{review.content}}</p>
        <div>
          <b-button @click="ChangeReview(review.id)">수정</b-button>
          <b-button @click="DeleteReview(review.id)">삭제</b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyReviewItem',
  props: {
    review: Object
  },
  methods: {
    ChangeReview(review_id) {
      this.$emit('change_review', review_id)
    },
    DeleteReview(review_id) {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'delete',
        url: `${API_URL}/pages/reviews/${review_id}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then((res) => {
          console.log(res)
          alert('리뷰가 삭제되었습니다!')
          this.$router.go()
        })
    },
    MoveDetail(id) {
      this.$router.push({name: 'MovieDetail', params:{id}})
    }
  }
}
</script>

<style>
</style>