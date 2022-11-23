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
        <div class="img col-4 moviecardHeart">
          <div>
          <img :src="jpg" class="card-img-top">
          </div>
            <hr>
            <h4> {{movie?.title}}에게 : </h4>
            <RecordDetail
            :movie="movie"
            />
        </div>
        <div class="col-8" style="font-weight: bold; font-size: 1rem;">
          <h4>장르 : 
            <span v-for="(genre, index) in movie?.genres" :key="index">
              {{genre.name}} /
            </span>
          </h4>
          <br>
          <h4>TMDB 평점 : {{movie?.vote_average}}</h4>
          <br>
          <div style="width: 100%">
            <h4>시놉시스 : </h4>
            <br>
            <div v-if="show" class="overview">
              <h4>{{movie?.overview.substr(0, 151)}} <span v-if="movie?.overview.length >= 150">...</span></h4>
              <h4 @click="ShowChange" v-if="movie?.overview.length >= 150">더보기</h4>
            </div>
            <div v-else>
              <h4>{{movie?.overview}}</h4>
              <h4 @click="ShowChange">닫기</h4>
            </div>
          </div>
          <br>
          <h4>개봉일 : {{movie?.release_date}}</h4>
          <br>
          <hr>
          <br>
          <hr>
          <br>
          <div  class="btn-review-container">
            <h3>베스트 리뷰</h3>
            <br>
            <!-- <MakeReview
            :movie="movie"
            style="width:100%"
            />   -->
            <div v-if="status">
              <h4>첫 번째 리뷰의 주인공이 되어보세요!</h4>
              <br>
              <br>
            </div>
            <div v-else>
              <div v-for="top in topreviews"
              :key="`top-${top.id}`">
              <hr class="hr-dotted">
              <img class="medal" src="@/assets/medal.png" alt="medal">
              <br> 
              <h3>{{top.title}}</h3>
              <br>
              <p>{{top.content}}</p>
             </div>
              <hr class="hr-dotted">
              <br>
              <br>
            </div>  
            <div>
            <button @click="GoReview(movie.id)" class="custom-btn btn-review"><span>Click!</span><span>리뷰 더보기</span></button>
            <br>
            <button @click="ShowModal" class="custom-btn btn-review"><span>Click!</span><span>리뷰 남기기</span></button>
            </div>
            <!-- 리뷰 모달 -->
            <ModalTemplate @close="closeModal" v-if="modal">
              <h3>리뷰 남기기</h3>
              <b-input
              v-model="title"
              @keyup.enter="createReview"
              placeholder="리뷰 제목"></b-input>
              <br>
              <b-textarea
              @keyup.enter="createReview"
              placeholder="당신만의 리뷰를 남겨주세요"
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
      <div id="justify-content-center" class="container">
        <div class='row justify-content-around'>
          <div v-for="movie in genre_movies"
          :key="movie.id"
          class='col-3'>
          <div class="card mb-3" @click="MoveDetail(movie.id)">
            <img class="card-img-top detailitem" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`">
          </div>
        </div>
      </div>
    </div>
    </div>
    <br>
    <br>
    <hr>
    <br>
    <button v-if="ost" @click="ShowOst" class="custom-btn btn-heart btn-center">OST 닫기</button>
    <button v-else @click="ShowOst" class="custom-btn btn-heart btn-center">OST 보기</button>
    <!-- <MovieOst
    v-if="ost"
    :moviename="movie?.title"
    /> -->
    <br>
    <br>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import RecordDetail from '@/components/RecordDetail'
import ModalTemplate from '@/components/ModalTemplate'
// import MovieOst from '@/components/MovieOst'

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
      status: null,
      topreviews: [],
      ost: false
    }
  },
  components:{
    RecordDetail,
    // MakeReview,
    ModalTemplate,
    // MovieOst,
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
      this.GetTopReview()
      this.show = false
      window.scrollTo(0, 0);
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
    },
    GetTopReview() {
      const API_URL = 'http://127.0.0.1:8000'
      const movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/pages/reviews/top/${movie_id}/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        },
      })
        .then((res) => {
          if (res.status === 204) {
            this.status = true
          } else {
            this.status = false
            this.topreviews = res.data 
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ShowOst() {
      this.ost = !this.ost
    }
  },
  created() {
    this.getMovieDetail()
  },
  
}
</script>

<style>
.detailitem {
  padding: 0;
  width : 200px;
  height : 300px !important;
}

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

.overview {
  width: 90%;
  padding-left: 5rem;
}

.loading {
  position: absolute;
  z-index: 2;
  left: 40% !important;
  top: 40% !important;
}

.custom-btn {
  left: -9%;

  width: 240px;
  height: 40px;
  padding: 10px 25px;
  border: 0px solid #26A69A;
  font-family: 'DuHanna';
  font-weight: 500;
  font-size: 1.5rem;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}
.btn-heart {
  line-height: 40px;
  padding: 0;
  background: transparent;
  position: relative;
  z-index: 2;
  color: #fff;
  -webkit-perspective: 300px;
  perspective: 300px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
}
.btn-heart:hover{
  color: #26A69A;
}
.btn-heart:after {
  position: absolute;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #26A69A;
  z-index: -1;
  -webkit-transform-origin: center bottom;
  transform-origin: center bottom;
  -webkit-transform: rotateX(0);
  transform: rotateX(0);
  transition: all 0.3s ease;
}
.btn-heart:hover:after {
  -webkit-transform: rotateX(-180deg);
  transform: rotateX(-180deg);
}

.btn-review-container {
  position: static;
}
.btn-review{
  position: relative;
  left: -1.5rem !important;
  font-size: 1.5rem;
  bottom: 20px;
  border:none;
  width: 130px;
  height: 40px;
  line-height: 40px;
  -webkit-perspective: 230px;
  perspective: 230px;
}
.btn-review span {
  display: block;
  position: absolute;
  width: 100%;
  height: 40px;
  border: 2px solid #26A69A;
  margin:0;
  text-align: center;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all .3s;
  transition: all .3s;
}
.btn-review span:nth-child(1) {
  box-shadow:
   -7px -7px 20px 0px #fff9,
   -4px -4px 5px 0px #fff9,
   7px 7px 20px 0px #0002,
   4px 4px 5px 0px #0001;
  -webkit-transform: rotateX(90deg);
  -moz-transform: rotateX(90deg);
  transform: rotateX(90deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}
.btn-review span:nth-child(2) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
  -webkit-transform-origin: 50% 50% -20px;
  -moz-transform-origin: 50% 50% -20px;
  transform-origin: 50% 50% -20px;
}
.btn-review:hover span:nth-child(1) {
  -webkit-transform: rotateX(0deg);
  -moz-transform: rotateX(0deg);
  transform: rotateX(0deg);
}
.btn-review:hover span:nth-child(2) {
  background: #26A69A;
  color: #26A69A;
  -webkit-transform: rotateX(-90deg);
  -moz-transform: rotateX(-90deg);
  transform: rotateX(-90deg);
}
p.button {
  display: block;
  position: absolute;
  left: 59.3%;
  float: left;
  width: 250px;
  padding: 0;
  margin: 10px 20px 10px 0;
  font-weight: 600;
  font-size: 130%;
  text-align: center;
  line-height: 45px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
}
.btnBlueGreen {
  background: #26A69A;
}
.btnFade.btnBlueGreen {
  width: 85px;
  font-size: 100%;
}
.btnFade.btnBlueGreen:hover {
  background: #14554f;
}
.btnPush:hover {
  margin-top: 15px;
  margin-bottom: 5px;
}
.btnBlueGreen.btnPush {
  box-shadow: 0px 5px 0px 0px #14554f;
}
.btnBlueGreen.btnPush:hover {
  box-shadow: 0px 0px 0px 0px #14554f;
}

.btn-center {
  left: 0%
}

.moviecardHeart {
  position: static;
}

.hr-dotted {
border : 0px;
border-top: 2px dotted #8866aa;
width: 50%;
margin-left: 25%;
}

.medal {
  height: 5%;
  width: 5%;
}
</style>