<template>
<div>
  <div @click="MoveDetail(result.id)">
    <div class="card mx-auto" style="height: 100%">
      <div>
        <img :src="imgUrl" class="card-img-top" height=90%>
      </div>
      <div class="card-body">
        <h5 class="card-title">{{result?.title}}</h5>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'SearchItem',
  props: {
    result: Object,
  },
  computed: {
    imgUrl() {
      const url = `https://image.tmdb.org/t/p/original/${this.result.poster_path}`
      return url
    }
  }
}
</script>

<style>

</style>