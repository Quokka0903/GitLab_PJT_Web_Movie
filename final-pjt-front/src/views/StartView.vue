<template>
  <div class="hello">
    <img src="@/assets/mom.jpg" alt="mom_logo">

    <h4>
      당신만을 위한 영화 맞춤 서비스
    </h4>
    
    <h4>Movie On Map,</h4>
    <h4>My Own Movies,</h4>
    <br>
    <h2>MOM</h2>
    
    <router-link :to="{ name: 'LoginView' }">이용하기</router-link>
  </div>
</template>

<script>
export default {
  name: 'StartView',

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
img {
  width: 40%;
  height: 40%;
}
</style>
