<template>
  <div @click="MoveDetail(movie.id)"> 
    <div class="card mx-auto" style="height: 30rem">
      <div>
        <img :src="jpg" class="card-img-top" height=90%>
      </div>
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
      </div>
  </div>
  </div>
</template>

<script>
export default {
  name:'GenreItem',
    props: {
      movie : Object,
    },
  computed: {
    title() {
      return this.movie.title
    },
    jpg() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  },
  methods: {
    MoveDetail(id) {
      this.$router.push({name: 'MovieDetail', params:{id}})
    }
  } 
}
</script>

<style>
.card {
  margin-top: auto;
  background-size: cover;
}

.img {
  width : 270px;
  height : 300px;
}
</style>