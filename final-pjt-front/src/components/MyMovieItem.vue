<template>
  <div @click="MoveDetail(movie.movie_id)">
    <div class="card mx-auto" style="height: 100%">
      <div>
        <img :src="imgUrl" class="card-img-top" height=90%>
      </div>
      <div class="card-body">
        <h5 class="card-title">{{detailmovie?.title}}</h5>
        <p>점수: {{movie.score}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MyMovieItem',
  props: {
    movie: Object
  },
  data () {
    return {
      detailmovie: [],
      imgUrl: ''
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/movies/${this.movie.movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
       .then((res) => {
        console.log(res)
          this.detailmovie = res.data
          this.imgUrl = `https://image.tmdb.org/t/p/original/${res.data.poster_path}`
        })
    },
    MoveDetail(id) {
      this.$router.push({name: 'MovieDetail', params:{id}})
    }
  },
  created() {
    this.getMovieDetail()
  }
}
</script>

<style>

</style>