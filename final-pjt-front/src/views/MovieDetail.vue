<template>
  <div class="background">
    <p v-if="!background" class="loading">
      <img src="@/assets/loading.gif" alt="">
    </p>
    <div id="justify-content" class="container">
      <h1>{{movie?.title}}</h1>
      <br>
      <hr>
      <br>
      <div class="row justify-content-around">
        <div class="img col-4">
          <img :src="jpg" class="card-img-top">
            <hr>
            <p> {{movie?.title}}에게 : </p>
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
          <div style="width: 100%">
            <p>시놉시스 : </p>
            <div v-if="show">
              <p>{{movie?.overview.substr(0, 151)}} <span v-if="movie?.overview.length >= 150">...</span></p>
              <p @click="ShowChange" v-if="movie?.overview.length >= 150">더보기</p>
            </div>
            <div v-else>
              <p>{{movie?.overview}}</p>
              <p @click="ShowChange">닫기</p>
            </div>
          </div>
          <p>개봉일 : {{movie?.release_date}}</p>
          <div>
            <h5>리뷰</h5>
            <!-- <MakeReview
            :movie="movie"
            style="width:100%"
            />   -->
            <b-button @click="ShowModal">리뷰 남기기</b-button>
            <b-button @click="GoReview(movie.id)">리뷰 더보기</b-button>
            <ModalTemplate @close="closeModal" v-if="modal">
              <h3>리뷰 남기기</h3>
              <b-input
              v-model="title"
              @keyup.enter="createReview"
              placeholder="리뷰 제목"></b-input>
              <b-textarea
              @keyup.enter="createReview"
              placeholder="당신만의 한 줄을 남겨주세요"
              v-model="content"
              ></b-textarea>
              <template slot="footer">
                <button @click="createReview">제출</button>
              </template>
            </ModalTemplate>
          </div>
        </div>
      </div>
      <br>
      <br>
      <hr>
      <br>
      <h3> 같은 장르의 영화 </h3>
      <br>
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
import ModalTemplate from '@/components/ModalTemplate'
// import MakeReview from '@/components/MakeReview'
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
      genre_movies: [],
      show: true,
      title: '',
      content: '',
      modal: false,
    }
  },
  components:{
    RecordDetail,
    // MakeReview,
    ModalTemplate
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
              //배경설정
              document.documentElement.style.setProperty('--background', 'url("' + this.background + '")')
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
      console.log(id)
      this.$router.push({name: 'MovieDetail', params:{id}})
      // this.$router.go() -> 새로고침
      this.getMovieDetail()
    },
    ShowChange() {
      this.show = !this.show
    },
    createReview() {
      if (this.title.length === 0) {
        alert('제목을 입력해주세요!')
      } else if (this.content.length === 0) {
        alert('내용을 입력해주세요!')
      } else {
        const API_URL = 'http://127.0.0.1:8000'
        axios({
          method: 'post',
          url: `${API_URL}/pages/movies/${this.movie.id}/reviews/`,
          headers: {
              Authorization: `Token ${ this.$store.state.token }`
          },
          data: {
              movie: this.movie.id,
              title: this.title,
              content: this.content,
          }
        })
          .then((res) => {
              console.log('리뷰', res)
              this.title = ''
              this.content = ''
          })
          .catch((err) => {
            console.log(err)
          })
      }
      this.closeModal()
    },
    GoReview(movie_id) {
      this.$router.push({name: 'ReviewListView', params: {movie_id: movie_id}})
    },
    ShowModal() {
      this.modal = true
    },
    closeModal() {
      this.modal = false
      this.title = ''
      this.content = ''
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
  }
.background::after {
  height: 100%;
  width: 100%;
  content: "";
  background-image: linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0) 70%,
            rgba(255, 255, 255, 0.5) 80%,
            rgba(255, 255, 255, 0.75) 90%,
            rgb(255, 255, 255) 100%
          ), var(--background);
  
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
.loading {
  position: absolute;
  z-index: 2;
  left: 40% !important;
  top: 40% !important;
}
</style>