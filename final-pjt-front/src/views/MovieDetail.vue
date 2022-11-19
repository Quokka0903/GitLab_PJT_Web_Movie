<template>
  <div>
    <h1>detail</h1>
    <p>{{movie?.title}}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieDetail',
  data() {
    return {
      movie: null,
    }
  },
  methods: {
    getMovieDetail() {
      const movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/movies/${movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.movie = res.data
        })
    }
  },
  created() {
    this.getMovieDetail()
  }
}
</script>

<style>

</style>