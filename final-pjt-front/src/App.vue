<template>
  <div id="app">
    <!-- <nav> -->
      <!-- <router-link :to="{ name: 'ArticleView' }">Articles</router-link> |  -->
      <!-- <router-link :to="{ name: 'MovieView' }">MoviePage</router-link> |  -->
      <!-- <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> |  -->
      <!-- <router-link :to="{ name: 'LoginView' }">LoginPage</router-link> -->
    <!-- </nav> -->
    <router-view/>
  </div>
</template>

<script>
</script>

<style>
@font-face {
  font-family: "DuHanna";
  src: url(@/assets/font/BMHANNAPro.ttf) format("truetype");
  font-weight: normal;
}
@font-face {
  font-family: "YarpHanna";
  src: url(@/assets/font/BMHANNAAir_ttf.ttf) format("truetype");
  font-weight: normal;
}
@font-face {
  font-family: "Gicsseong";
  src: url(@/assets/font/BMDOHYEON_ttf.ttf) format("truetype");
  font-weight: normal;
}

#app {
  font-family: 'DuHanna' 'YarpHanna' 'Gicsseong';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}

h1 {
  font-family: 'DuHanna';
}

h2 {
  font-family: 'DuHanna';
}

h3 {
  font-family: 'DuHanna';
}

h4 {
  font-family: 'YarpHanna';
}

h5 {
  font-family: 'YarpHanna';
}

p {
  font-family: 'YarpHanna';
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
