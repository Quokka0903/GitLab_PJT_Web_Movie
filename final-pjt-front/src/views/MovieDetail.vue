<template>
  <div class="background">
    <div id="justify-content" class="container">
      <h1>{{movie?.title}}</h1>
      <div class="row justify-content-around">
        <div class="img col-4">
          <img :src="jpg" class="card-img-top">
            <h5>별점</h5>
            <RecordDetail
            :movie="movie"
            />
        </div>
        <div class="col-8" style="font-weight: bold; font-size: 1rem;">
          <p>장르 : 
            <span v-for="(genre, index) in movie?.genres" :key="index">
              {{genre.name}} /
            </span>
          </p>
          <p>TMDB 평점 : {{movie?.vote_average}}</p>
          <p>시놉시스 : </p>
          <p>{{movie?.overview}}</p>
          <p>개봉일 : {{movie?.release_date}}</p>
          <div>
            <h5>리뷰</h5>
            <MakeReview
            :movie="movie"
            style="width:100%"
            />  
          </div>
        </div>
      </div>
      <hr>
      <h3>같은 장르의 영화 추천드립니다!</h3>
      <div class='row row-cols-md-4'>
        <div v-for="movie in genre_movies"
        :key="movie.id"
        class='col'>
        <div class="card h-100" @click="MoveDetail(movie.id)">
          <img class="card-img-top" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="">
        </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RecordDetail from '@/components/RecordDetail'
import MakeReview from '@/components/MakeReview'
import _ from 'lodash'


export default {
  name: 'MovieDetail',
  data() {
    return {
      movie: null,
      movie_id: null,
      jpg: null,
      detail: null,
      background: null,
      genre_movies: []
    }
  },
  components:{
    RecordDetail,
    MakeReview,
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
          this.movie_id = movie_id
          this.jpg = `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
          return { real_movie_id: this.movie.movie_id, movie_id: movie_id}
        })
        .then((res) => {
          axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/${res.real_movie_id}?api_key=97facdf795694b266aef7a0828a53e1f&language=ko-KR`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              this.detail = res.data
              this.background = `https://image.tmdb.org/t/p/original/${this.detail.backdrop_path}`
              // console.log(this.background)
              
              document.documentElement.style.setProperty('--background', 'url("' + this.background + '")')
              
              const background = document.querySelector('.background')
              const backStyle = window.getComputedStyle(background,'::after')
              console.log(backStyle.backgroundImage)
              // backStyle.backgroundImage = 'url("' + this.background + '")'
              // console.log(backStyle)
            })
          return {movie_id: res.movie_id}
        })
        .then((res) => {
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/pages/genre_algo/${res.movie_id}/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              this.genre_movies = _.sampleSize(res.data, 4)
            })
            .catch((err) => {
              console.log(err)
            })
        })
    },
    MoveDetail(id) {
      this.$router.push({name: 'MovieDetail', params:{id}})
      // this.$router.go() -> 새로고침
      this.getMovieDetail()
    }
  },
  created() {
    this.getMovieDetail()
  },
  
}
</script>

<style>
.img {
    width : 30%;
    height : 30%;
  }
.background {
  height: 100%;
  /* overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat; */
  }
.background::after {
  height: 100%;
  width: 100%;
  content: "";
  background-image: var(--background);
  
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