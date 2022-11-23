<template>
  <div>
    <div id="holderSign">
    <h1>Sign Up</h1>
    <br>
    <form @submit.prevent="signUp">
      <label class="inputText" for="username">ID : </label> <input @input="CheckUser" class="inputSignup" type="text" id="username" v-model="username">
      <p v-show="!sameusername">아이디를 입력해주세요</p>
      <p v-show="sameusername">아이디는 1글자 이상 입력되어야 합니다</p>
      <!-- <br> -->
      <label class="inputText" for="password1"> PW : </label> <input @input="CheckPassword" class="inputSignup" type="password" id="password1" v-model="password1">
      <p v-show="!samepassword">비밀번호를 입력해 주세요</p>
      <p v-show="samepassword">비밀번호는 8글자 이상 입력되어야 합니다</p>
      <!-- <br> -->
      <label class="inputText" for="password2"> PW AGAIN : </label> <input @input="CheckPassword2" class="inputSignup" type="password" id="password2" v-model="password2">
      <p v-show="!samepassword2"><br></p>
      <p v-show="samepassword2">비밀번호가 일치하지 않습니다</p>
      <!-- <br> -->
      <!-- <a href="#"><span data-attr="Sign">Sign</span><span data-attr="Up">Up</span></a> -->
      <div class="button">
          <p class="btnText">DONE?</p>
          <div class="btnTwo">
            <p class="btnText2">SIGNUP!
              <input class="hidden" type="submit" value="GO!">
            </p>
          </div>
      </div>
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
      sameusername: false,
      samepassword: false,
      samepassword2: false,
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
    CheckUser() {
      const username = this.username
      if (username.trim().length === 0) {
        this.sameusername = true
      } else {
        this.sameusername = false
      }
    },
    CheckPassword() {
      const password1 = this.password1
      if (password1.trim().length < 8) {
        this.samepassword = true
      } else {
        this.samepassword = false
      }
    },
    CheckPassword2() {
      console.log('working')
      const password2 = this.password2
      const password1 = this.password1
      if (password2 === password1) {
        this.samepassword2 = false
      } else {
        this.samepassword2 = true
      }
    },
  },
  created() {
    this.Check()
  }
}
</script>

<style>
#holderSign{
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
.inputSignup {
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

/* .center {
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
}  */
</style>