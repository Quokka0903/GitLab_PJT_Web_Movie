<template>
  <div>
    <br>
    <!-- {{moviename}} 들어갈 부분 -->
    <div v-if="movie">
      <iframe :src="`https://www.youtube.com/embed/${this.movie.id.videoId}`" width="640" height="360"></iframe>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

// export default {
//   name: 'MovieOstView',
//   data() {
//     return {
//       movie: null
//     }
//   },
//   props: {
//     moviename: String,
//   },
//   methods: {
//     GetSearch() {
//       const SearchText = this.moviename + ' ost 모음'
//       axios({
//         method: 'get',
//         url: `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${SearchText}&type=video&key=AIzaSyAnjtdd0bFO1UvwzXtPV-bBzT-LzotI3MM`
//       })
//         .then((res) => {
//           this.movie = res.data.items[0]
//         })
//         .catch((error) => {
//           console.log(error)
//         })
//     },
//   },
//   created() {
//     this.GetSearch()
//   },
// }
// </script>

// <style>

</style>