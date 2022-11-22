<template>
  <div class="row justify-content-start">
    <br>
    <h3>취향에 맞는 영화 추천을 위해 최소 10개의 영화 평점을 입력해주세요!</h3>
    <br>
    <h1>{{count}} 개의 영화가 선택되었습니다!</h1>
    <FirstRecord
    v-for="movie in movies"
    :key="movie.id"
    :movie ="movie"
    class="col-4"
    @checked="CountNumber"
    />
    <b-button @click="Submit">선택완료</b-button>
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
      if (this.count >= 10) {
        this.$store.commit('CHANGE_CHECKED')
        this.$router.push({name: 'MainView'})
      } else {
        alert('10개 이상의 영화의 평점을 입력해주세요!')
      }
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>