<template>
  <div id="justify-content" class="container">
    <div class="row justify-content-around">
      <p>오늘 이 영화 어떠세요?</p>
        <AlgorithmItem
        v-for="(movie) in recommend"
        :key="movie.id"
        :movie="movie"
        class="col-3"
        />
    </div>
    <br>
    <hr>
    <br>
    <div class="row justify-content-around">
      <p>실시간 랭킹 영화</p>
      <MovieViewItem
      v-for="(movie, index) in Movies"
      :movie='movie'
      :key="index"
      class="col-2"
      />
    </div>
    <br>
    <hr>
    <br>
    <div class="row justify-content-around">
      <p>{{genre}} 장르의 영화 어떠세요?</p>
      <GenreItem
      v-for="(movie,idx) in genre_movies"
      :movie="movie"
      :key="idx"
      class="col-3"/>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import MovieViewItem from '@/components/MovieViewItem.vue'
import AlgorithmItem from '@/components/AlgorithmItem.vue'
import GenreItem from '@/components/GenreItem.vue'

export default {
  name: 'MainView',
  components: {
    MovieViewItem,
    AlgorithmItem,
    GenreItem,
  },
  data() {
    return {
      Movies:[],
      genre: null,
      genre_movies: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movies() {
      return this.$store.state.movies
    },
    recommend() {
      return this.$store.state.recommend
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
    getRecommend() {
      if (this.isLogin) {
        this.$store.dispatch('getRecommend')
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
          this.Movies = _.sampleSize(response.data.results, 5)
        }) 
        .catch((error)=> {
          console.log(error)
        })
    },
    getGenreMovie() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/pages/genre/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
       .then((response) => {
        this.genre = response.data.genre
        this.genre_movies = response.data.movies
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getMovies()
    this.getTopMovie()
    this.getRecommend()
    this.getGenreMovie()
  },
  mounted() {

  }
  
}
</script>

<style>
.box {
  text-align: center;
  border: 0;
  width: 1000px;
  height: 1000px;
}

</style>