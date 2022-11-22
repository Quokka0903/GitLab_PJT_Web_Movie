<template>
  <div>
    <div class="card mx-auto" style="height: 100%">
      <div>
        <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" height=90%>
      </div>
      <div class="card-body row justify-content-around">
        <h5 class="card-title">{{movie?.title}}</h5>
        <div
        class="star col-2"
        v-for="index in 5"
        :key="index"
        @click="checkscore(index, movie)"
        >
          <span v-if="index <= score">❤️</span>
          <span v-if="index > score">🤍</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FirstRecord',
  props: {
    movie: Object
  },
  data() {
    return {
      score: 0,
      checked: false
    }
  },
  methods: {
    checkscore(index, movie) {
      this.score = index;
      const score = Number(this.score)
      const movie_pk = movie.id
      const payload = {
        score,
        movie_pk,
      }
      this.$store.dispatch('RecordScore', payload)
      if (!this.checked) {
        this.$emit('checked', movie.pk)
        this.checked = true
      }
    },
  }
}
</script>

<style>

</style>