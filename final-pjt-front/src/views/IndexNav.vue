<template>
  <div class="idxback">
    <nav class="navbarCustom">
      <router-link :to="{ name: 'MainView' }">메인 페이지</router-link> |
      <router-link :to="{ name: 'SearchView' }"> 영화 검색 </router-link> | 
      <router-link :to="{ name: 'ProfileView'}">나의 프로필</router-link>
    </nav>
    <!-- fade 라우터 전환 -->
    <transition name="slide-fade" mode="out-in">
      <router-view/>
    </transition>
    </div>
</template>

<script>

</script>

<style>
.navbarCustom {
  font-family: 'Gicsseong';
  font-size: 180%;
  text-decoration: none;
}
/* .idxback {
} */

a {
  text-decoration: none!important;
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