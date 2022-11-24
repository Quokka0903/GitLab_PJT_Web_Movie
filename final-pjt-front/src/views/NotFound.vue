<template>
  <div>
    <img class="back" :src="require(`@/assets/404/404_${num}.gif`)" alt="">
  </div>
</template>

<script>
import _ from 'lodash'


export default {
  name: 'NotFound',
  data() {
    return {
      num: null,
    }
  },
  methods: {
    getImg() {
      this.num = _.sample(_.range(2, 3))
    }
  },
  created() {
    this.getImg()
  }
}
</script>

<style>

.back {
  height: 100%;
  width: 100%;
  content: "";
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  top: 0;
  left: 0;
  z-index: -1;
  position: absolute;
}