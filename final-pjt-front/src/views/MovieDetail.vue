<template>
  <div class="background">
    <h1>{{movie?.title}}</h1>
    <div>
      <h3>영화 정보</h3>
      <div class="img">
        <img :src="jpg" class="card-img-top">
      </div>
      <p>장르 : 
        <span v-for="(genre, index) in movie?.genres" :key="index">
          {{genre.name}}
        </span>
      </p>
      <p>개봉일 : {{movie?.release_date}}</p>
      <p>평점 : {{movie?.vote_average}}</p>
      <p>줄거리 : {{movie?.overview}}</p>
    </div>
    <div>
      <h3>별점</h3>
      <RecordDetail
      :movie="movie"
      />
    </div>
    <div>
      <h3>리뷰</h3>
      <MakeReview
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RecordDetail from '@/components/RecordDetail'
import MakeReview from '@/components/MakeReview'


export default {
  name: 'MovieDetail',
  data() {
    return {
      movie: null,
      movie_id: null,
      jpg: null,
      detail: null,
      background1: null,
      background2: null,
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
        })
    },
    getBackdrop() {
      console.log(this.movie) 
      const movie_id = this.movie.movie_id
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}?api_key=97facdf795694b266aef7a0828a53e1f&language=ko-KR`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.detail = res.data
          console.log(this.detail)
          console.log(this.detail.backdrop_path)
          console.log(this.detail.belongs_to_collection)
          this.background1 = `https://image.tmdb.org/t/p/original/${this.detail.backdrop_path}`
          this.background2 = `https://image.tmdb.org/t/p/original/${this.detail.belongs_to_collection.backdrop_path}`
          console.log(this.background1)
          console.log(this.background2)
        })
    }
  },
  created() {
    this.getMovieDetail()

  },
  mounted() {
    this.getBackdrop()
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
  overflow: hidden;
  background-size: cover;
  background-position: center;
  }
</style>