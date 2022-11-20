<template>
  <div>
    <nav>
      <router-link :to="{ name: 'MainView' }">메인 페이지</router-link> |
      <span> 근처 극장 찾기 </span> | 
      <router-link :to="{ name: 'ProfileView'}">나의 프로필</router-link>
    </nav>
    <router-view/>
    </div>
</template>

<script>
</script>