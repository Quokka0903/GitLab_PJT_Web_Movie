<template>
  <div class="row justify-content-around">
    {{review}}
    <div class="reviewimg col-4"> 
        <img :src="`https://image.tmdb.org/t/p/original/${review.movie_poster}`" 
              class="card-img-top"
              @click="MoveDetail(review.id)">
    </div>
      <div class="col-8 reviewitem">
        <p>영화 제목 : {{review.movie_title}}</p>
        <p>리뷰 제목 : {{review.title}}</p>
        <p>리뷰 내용 : {{review.content}}</p>
        <b-button @click="ChangeReview(review.id)">수정</b-button>
        <b-button @click="DeleteReview(review.id)">삭제</b-button>
        <hr>
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
.reviewimg {
    width : 400px;
    height : 600px;
  }

.reviewitem {
  padding-top : 3em;
  margin-top: 10em;
}
</style>