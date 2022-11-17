<template>
  <div>
    <p @click="LogOut">로그아웃</p>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  methods: {
    LogOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style>

</style>