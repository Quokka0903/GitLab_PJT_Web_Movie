<template>
  <div>
    <header>
      <nav class="header">  
        <br>
        <h3>이미 관람하신 영화의 평점을 매겨주세요!</h3>
        <h3>{{count}} 개의 영화가 선택되었습니다.</h3>
        <div class="button" @click="Submit">
          <p class="btnText">READY?</p>
          <div class="btnTwo">
            <p class="btnText2">GO!
              <input class="hidden" type="submit" value="GO!">
            </p>
          </div>
        </div>
        <h5>more you rate, more effective it is.</h5>
      </nav>
    </header>
    <main class="justify-content-start main">
      <div class="row justify-content-around">
        <FirstRecord
        v-for="movie in movies"
        :key="movie.id"
        :movie ="movie"
        class="col-lg-2 col-md-3 col-sm-4 mb-4 mx-auto"
        @checked="CountNumber"
        />
      </div>
    </main>
  </div>
</template>

<script>
import FirstRecord from '@/components/FirstRecord'
import axios from 'axios'

export default {
  name: "RecordView",
  components:{
    FirstRecord
  },
  data() {
    return {
      movies: [],
      count: 0
    }
  },
  methods: {
    getMovies() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/pages/like`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.movies = res.data
        })
    },
    CountNumber() {
      this.count++
      console.log(this.count)
    },
    Submit() {
      if (this.count >= 3) {
        this.$store.commit('CHANGE_CHECKED')
        this.$router.push({name: 'MainView'})
      } else {
        alert('최소 3개 이상의 평점을 입력해주세요!')
      }
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  
  height: 280px;
  padding: 1rem;
  color: white;
  background: linear-gradient(
            to bottom,
            #26A69A 60%,
            #26a699a1 74%,
            #26a6995f 88%,
            #26a69900 100%
          ),#26a69900;
  font-weight: bold;
  font-size: 1rem;
  z-index: 1;
}
.main {
  padding-top: 300px;
  z-index: 0;
}
/* 카드 스타일 */
.recordcard {
 height: 460px;
} 

/* 버튼 스타일 */
.button {
  background: #3D4C53;
  margin : 20px auto;
  padding: 8px;
  width : 200px;
  height : 40px;
  overflow: hidden;
  text-align : center;
  transition : .1s;
  cursor : pointer;
  border-radius: 3px;
  box-shadow: 0px 1px 2px rgba(0,0,0,.2);
}
.btnTwo {
  position : relative;
  width : 250px;
  height : 100px;
  margin-top: 0px;
  padding-top: 2px;
  background : #26A69A;
  top: -15px;
  left : -10px;
  transition : .3s;
}
.btnText {
  color : white;
  transition : .3s;
}
.btnText2 {
  margin-top : 55px;
  margin-left : -45px;
  color : #FFF;
}
.button:hover .btnTwo{ /*When hovering over .button change .btnTwo*/
  bottom: 0px;
  left: -10px;
}
.button:hover .btnText{ /*When hovering over .button change .btnText*/
  margin-bottom : -65px;
}
.button:active { /*Clicked and held*/
  box-shadow: 0px 5px 6px rgba(0,0,0,0.3);
}
</style>