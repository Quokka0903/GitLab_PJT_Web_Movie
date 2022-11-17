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
    }
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        console.log('영화 불러오기')
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