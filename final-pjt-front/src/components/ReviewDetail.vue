<template>
  <div>
    <p>작성자: {{review?.username}}</p>
    <p>좋아요 수: <span :id="`review-${review?.id}`">{{review?.like_users_count}}</span></p>
    <h4>{{review?.title}}</h4>
    <p>{{review?.content}}</p>
    <div v-if="userId != review?.user">
      <b-button v-if="review?.like_users.includes(userId)" :id="`button-${review?.id}`" @click="LikeReview(review.id)">좋아요 취소</b-button>
      <b-button v-else :id="`button-${review?.id}`" @click="LikeReview(review.id)">좋아요</b-button>
    </div>
    <div v-else>
      <b-button @click="ChangeReview(review.id)">수정</b-button>
      <b-button @click="DeleteReview(review.id)">삭제</b-button>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "ReviewDetail",
  data() {
    return {
      review: null,
      userId: null,
    }
  },
  watch: {
    review() {
      this.getReviews()
    }
  },
  props: {
    review_id: Number,
  },
  methods: {
    getReviews() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/reviews/${this.review_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.review = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    LikeReview(review_id) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/pages/reviews/${review_id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          const like = document.getElementById(`review-${res.data.pk}`)
          like.innerText = res.data.like_count
          const button = document.getElementById(`button-${res.data.pk}`)
          if (res.data.is_liked) {
            button.innerText = '좋아요 취소'
          } else {
            button.innerText = '좋아요'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUserId() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.userId = res.data.pk
        })
        .catch((err) => {
          console.log(err)
        })
    },
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
        }
      })
        .then((res) => {
          console.log(res)
          alert('리뷰가 삭제되었습니다!')
          this.$router.go()
        })
    },
  },
  created() {
    this.getReviews()
    this.getUserId()
  }
}
</script>

<style>

</style>