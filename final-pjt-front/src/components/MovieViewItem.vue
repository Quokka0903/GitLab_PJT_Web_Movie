<template>
  <div>
    <a :href="link" target='_blank' class="toWebSite">
    <div class="card mx-auto" style="height: 100%">
      <img :src="jpg" class="card-img-top" height=90%>
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
      </div>
    </div>
    </a>
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
      link() {
        return `https://www.themoviedb.org/movie/${this.movie.id}`
      }
    }
  }
  </script>
  
  <style>
  .toWebSite {
    text-decoration: none;
    color: black;
  }
  </style>