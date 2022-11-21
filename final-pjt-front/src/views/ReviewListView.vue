<template>
  <div>
    <p>리뷰리스트</p>
    <ReviewDetail
    v-for="(id, index) in review_ids"
    :review_id="id.id"
    :key="`review-${index}`"/>
  </div>
</template>

<script>
import ReviewDetail from '@/components/ReviewDetail'
import axios from 'axios'

export default {
  name: 'ReviewListView',
  data() {
    return {
      review_ids: []
    }
  },
  components: {
    ReviewDetail,
  },
  methods: {
    
    getReviewids() {
      const movie_id = this.$route.params.movie_id
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/movies/reviews/${movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.review_ids = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getReviewids()
  }
}
</script>

<style>

</style>