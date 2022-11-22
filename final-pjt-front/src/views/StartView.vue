<template>
  <div id="start">
    <div>
      <div>
        <br>
        <img src="@/assets/logotext3.png" alt="">
        <br>
        <br>
        <img src="@/assets/logotext4.png" alt="">
        <br>
        <br>
        <br>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StartView',
  created() {
    setTimeout(() => {
      this.$router.replace({name: 'LoginView'})
      }, 4000)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#start {
/* background:url("@/assets/cinema/cinema00.jpg"); */
background-repeat: no-repeat;
background-size: cover;
background-position: center center;
width: 100%;
height: 100%;
}

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
  color: whitesmoke;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
}
img {
  width: 40%;
  height: 40%;
}

/* 페이지 전환(fade) */
.fade-enter {
  opacity: 0;
}
.fade-enter-active,
.fade-enter-active {
  transition: opacity 0.5s ease-out;
}
.fade-leave-to {
  opacity: 0;
}
</style>
