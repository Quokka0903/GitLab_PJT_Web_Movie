<template>
  <div @click="MoveDetail(movie.id)">
    {{movie.title}}
  </div>
</template>

<script>
export default {
  name: 'AlgorithmItem',
  props: {
    movie: Object,
  },
  methods: {
    MoveDetail(id) {
      this.$router.push({name: 'MovieDetail', params:{id}})
    }
  }
}
</script>

<style>

</style>