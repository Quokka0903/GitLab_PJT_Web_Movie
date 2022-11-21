<template>
<div>
  <br>
  <h1>내가 평점 준 영화</h1>
  <hr>
  <br>
  <div class="row justify-content-around">
    <MyReviewItem
    v-for="review in my_reviews"
    :key="`my-review-${review.title}`"
    :review="review"
    />
  </div>
</div>
</template>

<script>
import MyReviewItem from '@/components/MyReviewItem'
import axios from 'axios'

export default {
  name: 'MyReviewView',
    data() {
    return {
      my_reviews: []
    }
  },
  components: {
    MyReviewItem,
  },
  computed: {
    userId() {
      return this.$route.params.user_id
    }
  },
  methods: {
    getReviews() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/infos/profile/${this.userId}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.my_reviews = res.data.my_reviews
        })
    }
  },
  created() {
    this.getReviews()
  }
}
</script>

<style>

</style>