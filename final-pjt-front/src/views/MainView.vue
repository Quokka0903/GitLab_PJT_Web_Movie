<template>
  <div id="justify-content" class="container">
    <img class="backMain" src="@/assets/mainback/mainback00.jpg" alt="">
    <p v-if="!genre_movies" class="loading box">
      <img src="@/assets/loading.gif" alt="">
    </p>
    <div class="row justify-content-around">
      <hr>
      <img class="deep" src="@/assets/deep02.png" alt="">
      <h3> 여러분의 관심사와 흥미를 빅데이터로 분석하여 가장 높은 만족도를 이끌어낼 만한 영화 리스트를 도출했습니다. </h3>
      <br>
      <br>
      <br>
      <AlgorithmItem
      v-for="(movie) in recommend"
      :key="movie.id"
      :movie="movie"
      class="col-3 moviecard"
      />
    </div>
    <br>
    <hr>
    <br>
    <div class="row justify-content-around">
      <h3>오늘은 {{genre}} 장르의 영화 어떠세요?</h3>
      <br>      <br>    <br>
      <GenreItem
      v-for="(movie,idx) in genre_movies"
      :movie="movie"
      :key="idx"
      class="col-3 moviecard"/>
  </div>
  <br>
  <hr>
  <br>
  <div class="row justify-content-around">
      <h3> TOP RATED MOVIES </h3>
      <br>      <br>      <br>
      <MovieViewItem
      v-for="(movie, index) in Movies"
      :movie='movie'
      :key="index"
      class="col-3 moviecard"
      />
    </div>
    <br>
    <hr>
    <br>
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
      num: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    recommend() {
      return this.$store.state.recommend 
    }
  },
  methods: {
    getRecommend() {
      if (this.isLogin) {
        this.$store.dispatch('getRecommend')
      } else {
        alert('로그인이 필요합니다!')
        this.$router.push({name: 'LoginView'})
      }
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
          this.Movies = _.sampleSize(response.data.results, 4)
          console.log(this.Movies)
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
          this.$router.go()
        })
    },
    getBack() {
      this.num = _.sample(_.range(1, 28))
    }
  },
  created() {
    this.getTopMovie()
    this.getRecommend()
    this.getGenreMovie()
    this.getBack()
    window.scrollTo(0, 0);
  },
  mounted() {
  }
}
</script>

<style>
.card {
  margin-top: auto;
  background-size: cover;
}
.card-title{
  font-size: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding-top: 5px; 
}

.moviecard {
  transition: all 0.2s linear;
}
.moviecard:hover {
  transform: scale(1.1);
  z-index: 1;
}

.deep {
  width: 10% !important;
}

.box {
  border: 0;
}
.loading {
  z-index: 2;
  left: 40% !important;
  top: 40% !important;
}
.backMain {
  height: 340% !important;
  width: 100%;
  content: "";
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 30%;
  top: 0;
  left: 0;
  z-index: -1;
  position: absolute;

}
</style>