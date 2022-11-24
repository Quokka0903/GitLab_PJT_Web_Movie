<template>
  <div>
    <div id="holder">
      <form @submit.prevent="logIn">
        <label class="inputText" @keyup.enter="logIn" for="username"> ID :  </label> <input class="input inputLogin" type="text" id="username" v-model="username"><br>
        <label class="inputText" @keyup.enter="logIn" for="password"> PW :  </label> <input class="input inputLogin" type="password" id="password" v-model="password"><br>
        <div class="button">
          <p class="btnText">READY?</p>
          <div class="btnTwo">
            <p class="btnText2">GO!
              <input class="hidden" type="submit" value="GO!">
            </p>
          </div>
        </div>        
      </form>
    <div class="button" @click="SignUp()">
      <p class="btnText">FIRST HERE</p>
      <div class="btnTwo">
        <p class="btnText2">SIGN UP!</p>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      if (username.length === 0) {
        alert('아이디를 입력해주세요')
        return
      } else if (password.length === 0) {
        alert('비밀번호를 입력해주세요')
        return
      }
      else {
        const payload = {
          username: username,
          password: password,
        }
        this.$store.dispatch('login', payload)
      }
    },
    Check() {
      if (this.isLogin) {
        console.log('보냄')
        this.$router.replace({name: 'MainView'})
      }
    },
    SignUp() {
      this.$router.push({name: 'SignUpView'})
    }
  },
  created() {
    this.Check()
  }
}
</script>

<style>
.input {
        width: 150px;
        margin: 9px 0;
}
.input:focus {
  animation-name: border-focus;
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
}
.hidden {
  width: 300%;
  left: -5px;
  opacity: 0%;
  position: absolute;
}

@keyframes border-focus {
  from {
    border-radius: 0;
  }
  to {
    border-radius: 30px;
  }
}

#holder{
  background: rgba(255, 255, 255, 0.512);
  padding: 10px;
  width: 350px;
  margin: 0 auto;
  position: relative;
  top: 12rem;
  transform: translateY(-65%);
  box-shadow: 0px 3px 8px rgba(0,0,0,0.25);
  border-radius: 2px;
}
/* 인풋 스타일 */
.inputLogin {
    width: 60%;
    border-radius: 20px;
    border: 2px solid #bbb;
    margin: 10px 0;
    padding: 10px 12px;
}
.inputText{
  font-size: 20px;
}
/* 버튼 스타일 */
.button {
  background: #3D4C53;
  margin : 20px auto;
  padding: 8px;
  width : 200px;
  height : 40px;
  overflow: hidden;
  text-align : center;
  transition : .1s;
  cursor : pointer;
  border-radius: 3px;
  box-shadow: 0px 1px 2px rgba(0,0,0,.2);
}
.btnTwo {
  position : relative;
  width : 250px;
  height : 100px;
  margin-top: -100px;
  padding-top: 2px;
  background : #26A69A;
  top: -5px;
  left : -250px;
  transition : .3s;
}
.btnText {
  color : white;
  transition : .3s;
}
.btnText2 {
  margin-top : 63px;
  margin-left : -55px;
  color : #FFF;
}
.button:hover .btnTwo{ /*When hovering over .button change .btnTwo*/
  left: 0px;
}
.button:hover .btnText{ /*When hovering over .button change .btnText*/
  margin-left : 65px;
}
.button:active { /*Clicked and held*/
  box-shadow: 0px 5px 6px rgba(0,0,0,0.3);
}

</style>