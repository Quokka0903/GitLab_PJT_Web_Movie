<template>
  <div>
    <h1>MainPage</h1>
    <AlgorithmItem
    v-for="(movie) in movies"
    :key="movie.id"
    :movie="movie"
    />
    <div class="box">
      <p>알고리즘</p>
      <div class="mx-auto ms-auto row g-3">
    </div>
    </div>
    <div class="mx-auto ms-auto row g-3">
      <MovieViewItem
      v-for="(movie, index) in Movies"
      :movie='movie'
      :key="index"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieViewItem from '@/components/MovieViewItem.vue'
import AlgorithmItem from '@/components/AlgorithmItem.vue'

export default {
  name: 'MainView',
  components: {
    MovieViewItem,
    AlgorithmItem,
  },
  data() {
    return {
      Movies:[]
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요합니다!')
        this.$router.push({name: 'LoginView'})
      }
    },
    getlist() {

    },
    getTopMovie(){
      axios({
        method : 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated?',
        params:{
          api_key:'3b039b524fe9061bc79cb30956f2b673',
          language:'ko-KR',
          page:'1',
          }       
      })
        .then((response) => {
          console.log(response)
          this.Movies = response.data.results
        }) 
        .catch((error)=> {
          console.log(error)
        })
    }
  },
  created() {
    this.getMovies()
    this.getTopMovie()
  },
  mounted() {

  }
  
}
</script>

<style>
.box {
  text-align: center;
  border: 1px solid;
  width: 1000px;
  height: 1000px;
}
</style>