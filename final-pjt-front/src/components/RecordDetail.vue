<template>
  <div>
    <span class="star">
      ★★★★★
      <span>★★★★★</span>
      <input type="range" oninput="drawStar(this)" value="0.5" step="0.5" min="0" max="5">
    </span>
    <input v-model="score" type="number" min="0" max="5" step="0.5">
    <input type="submit" @click="RecordScore(movie)">
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecordDetail',
  data() {
    return {
      score: null,
    }
  },
  methods: {
    drawStar(target) {
      console.log(target)
    document.querySelector(`.star span`).style.width = `${target.value * 10}%`;
    },
    RecordScore(movie) {
      const score = Number(this.score)
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          const userId = res.data.pk
          const movie_pk = movie.id
          const payload = {
            score,
            movie_pk,
            userId
          }
          this.$store.dispatch('RecordScore', payload)
          
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  props: {
    movie: Object
  }
}
</script>

<style>
  .star {
    position: relative;
    font-size: 2rem;
    color: #ddd;
  }
  
  .star input {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    opacity: 0;
    cursor: pointer;
  }
  
  .star span {
    width: 0;
    position: absolute; 
    left: 0;
    color: rosybrown;
    overflow: hidden;
    pointer-events: none;
  }
</style>