<template>
<div>
  <br>
  <h1>내가 평점 준 영화</h1>
  <hr>
  <br>
  <div class="row justify-content-around">
    <MyMovieItem
    v-for="movie in my_movies"
    :key="`my-movie-${movie.movie_id}`"
    :movie="movie"
    class="col-3"/>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import MyMovieItem  from '@/components/MyMovieItem'

export default {
  name: 'MyMovieView',
  data() {
    return {
      my_movies: []
    }
  },
  components: {
    MyMovieItem,
  },
  computed: {
    userId() {
      return this.$route.params.user_id
    }
  },
  methods: {
    getMovies() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/infos/profile/${this.userId}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.my_movies = res.data.my_movies
        })
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>