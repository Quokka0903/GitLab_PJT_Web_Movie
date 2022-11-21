<template>
  <div>
    <div class="card mx-auto" style="height: 100%">
      <div>
        <img :src="jpg" class="card-img-top" height=100%>
      </div>
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
      </div>
  </div>
  </div>
  </template>
  
  <script>
  export default {
    name:'MovieCard',
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