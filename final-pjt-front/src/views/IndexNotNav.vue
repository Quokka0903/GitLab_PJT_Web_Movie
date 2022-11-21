<template>
  <div class="index">
    <img class="back" :src="require(`@/assets/back/cinema${num}.jpg`)" alt="">
    <br>
    <img class="logo" src="@/assets/moms.png" alt="mom_logo">
    <nav>
    </nav>
    <transition name="slide-fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<script>

import _ from 'lodash'


export default {
  name: 'LogInView',
  data() {
    return {
      num: null,
    }
  },
  methods: {
    getBack() {
      this.num = _.sample(_.range(1, 28))
      console.log(this.num)
    }
  },
  created() {
    this.getBack()
  }
}
</script>

<style>
.index {
  width: 100%;
  height: 100%;
  font-style: initial;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-weight: 400;
  color: azure;
  
}
.back {
  height: 100%;
  width: 100%;
  content: "";
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 70%;
  
  top: 0;
  left: 0;
  z-index: -1;
  position: absolute;

}
.logo {
  width: 30%;
}

/* fade 라우터 전환 */
.fade-enter {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}

.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.2s ease;
}

.slide-fade-leave-to {
  transform: translateX(-10px);
  opacity: 0;
}
</style>