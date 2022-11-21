<template>
  <div>
    <RecordDetail
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />
  </div>
</template>

<script>
import RecordDetail from '@/components/RecordDetail'

export default {
  name: "RecordView",
  components:{
    RecordDetail
  },
  computed: {
    // movies() {
    //   return this.$store.state.movies
    // }
  }
}
</script>

<style>

</style>