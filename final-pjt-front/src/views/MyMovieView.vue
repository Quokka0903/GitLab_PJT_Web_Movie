
<template>
<div>
  <img class="backMain" src="@/assets/mainback/mainback00.jpg" alt="">
  <br>
  <h1>내가 평점 준 영화</h1>
  <div id="justify-content-center" class="container">
    <div class="row justify-content-left">
      <hr>
      <MyMovieItem
      v-for="movie in my_movies"
      :key="`my-movie-${movie.movie_id}`"
      :movie="movie"
      class="col-3 mb-4"/>
      </div>
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
.mycard {
  margin-top: auto;
  margin-bottom: 10px;
  background-size: cover;
  box-shadow: 0px 3px 8px rgba(0,0,0,0.25);
  transition: all 0.2s linear;
}
.mycard:hover {
  transform: scale(1.1);
  z-index: 1;
}


.mycard-title {
  font-size: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding-top: 10px; 
  margin-bottom: 10px;
}
</style>