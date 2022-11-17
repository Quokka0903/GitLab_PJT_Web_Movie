<template>
<div>
  <h1>MainPage</h1>
</div>
</template>

<script>
export default {
  name: 'MovieView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        this.$store.dispatch('getMovies')
      } else {
        alert('로그인이 필요합니다!')
        this.$router.push({name: 'LoginView'})
      }
    },
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>