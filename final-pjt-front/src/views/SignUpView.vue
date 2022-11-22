<template>
  <div>
    <div id="holder">
    <h1>Sign Up</h1>
    <form @submit.prevent="signUp">
      <label for="username">ID : </label><br>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> PW : </label><br>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> PW agian : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <br>
      <a href="#"><span data-attr="Sign">Sign</span><span data-attr="Up">Up</span></a>
      <input type="submit" value="SignUp">
      <br>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)
    },
    Check() {
      if (this.isLogin) {
        this.$router.replace({name: 'MainView'})
      }
    },
  },
  created() {
    this.Check()
  }
}
</script>

<style>
#holder{
  background: rgba(255, 255, 255, 0.512);
  padding: 10px;
  width: 250px;
  margin: 0 auto;
  position: relative;
  top: 12rem;
  transform: translateY(-65%);
  box-shadow: 0px 3px 8px rgba(0,0,0,0.25);
  border-radius: 2px;
}
.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
a {
    text-decoration: none;
    text-transform: uppercase;
    font-size: 30px;
}
a span {
    padding: 15px;
    transition: .5s;
    position: relative;
}
a span:nth-child(1) {
    color: #fff;
    background: #00000071;
}
a span:nth-child(2) {
    color: #fff;
    background: #ff363660;
}
a span:nth-child(1):before {
    content: attr(data-attr);
    position: absolute;
    top: 0;
    left: 0;
    background: #ff363645;
    padding: 15px;
    transition: 0.5S;
    transform-origin: top;
    transform: rotateX(90deg) translateY(-50%);
}
a:hover span:nth-child(1):before {
    transform: rotateX(0deg) translateY(0%);
} 
a span:nth-child(2):before {
    content: attr(data-attr);
    position: absolute;
    top: 0;
    left: 0;
    background: #262626;
    padding: 15px;
    transition: 0.5S;
    transform-origin: bottom;
    transform: rotateX(90deg) translateY(50%);
}
a:hover span:nth-child(2):before {
    transform: rotateX(0deg) translateY(0%);
} 
a  span:nth-child(1):after {
  content: attr(data-attr);
  padding: 15px;
  position: absolute;
  top: 0;
  left: 0;
  background: #262626;
  transform-origin: bottom;
  transform: rotateX(0deg) translateY(0%);
  transition: 0.5s;
}
a:hover span:nth-child(1):after {
  transform: rotateX(90deg) translateY(50%);
}
a span:nth-child(2):after {
    content: attr(data-attr);
    position: absolute;
    top: 0;
    left: 0;
    background: #ff3636;
    padding: 15px;
    transition: 0.5S;
    transform-origin: top;
    transform: rotateX(0deg) translateY(0%);
}
a:hover span:nth-child(2):after {
    transform: rotateX(90deg) translateY(-50%);
} 
</style>