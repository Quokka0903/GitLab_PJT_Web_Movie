<template>
  <div>
    <p>title: {{review.title}}</p>
    <p>content: {{review.content}}</p>
    <b-button @click="ChangeReview(review.id)">수정</b-button>
    <b-button @click="DeleteReview(review.id)">삭제</b-button>
    <hr>
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
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'put',
        url: `${API_URL}/pages/reviews/${review_id}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
        })
    },
    DeleteReview(review_id) {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'delete',
        url: `${API_URL}/pages/reviews/${review_id}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          alert('리뷰가 삭제되었습니다!')
          this.$router.go()
        })
    },
  }
}
</script>

<style>

</style>