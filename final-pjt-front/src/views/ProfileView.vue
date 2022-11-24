<template>
  <div>
    <img class="backimg" :src="require(`@/assets/back/cinema${num}.jpg`)" alt="">
  <div class="holderprofile">
    <form @submit.prevent="logIn">
      <!-- <h3>"{{username}}"님 환영합니다!</h3> -->
      <!-- <div class="box">
        <button class="button button--winona buttonprofile" data-text="Open Project"><span>Open Project</span></button>
        <button class="button button--winona buttonprofile" data-text="Create New"><span>Create New</span></button>
        <button class="button button--winona buttonprofile" data-text="Publish"><span>Publish</span></button>
      </div> -->

      <div @click="GoMovie" class="buttonprofile">평가한 영화 보기</div>
      <div @click="GoReview" class="buttonprofile">리뷰 남긴 영화 보기</div>
      <div @click="GoChange" class="buttonprofile">비밀번호변경</div>
      <div @click="LogOut" class="buttonprofile">로그아웃</div>
      <div class="buttonprofile" @click="DeleteUser">회원탈퇴</div>


    </form>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
export default {
  name: 'ProfileView',
  data() {
    return {
      user_id: null,
      username: null,
      num: null,
    }
  },
  methods: {
    getBack() {
      this.num = _.sample(_.range(1, 28))
    },
    LogOut() {
      this.$store.dispatch('logOut')
    },
    GoMovie() {
      const user_id = this.user_id
      this.$router.push({name:'MyMovieView', params: {user_id}})
    },
    GoReview() {
      const user_id = this.user_id
      this.$router.push({name:'MyReviewView', params: {user_id}})
    },
    GoChange() {
      const user_id = this.user_id
      this.$router.push({name:'ChangeView', params: {user_id}})
    },
    GetUserId() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.user_id = res.data.pk
          this.username = res.data.username
        })
    },
    DeleteUser() {
      this.$store.dispatch('DeleteUser', this.user_id)
    }
  },
  created() {
    this.GetUserId(),
    this.getBack()
  },
}
</script>

<style>

.backimg {
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

.holderprofile{
  background: rgba(255, 255, 255, 0.6);
  padding: 10px;
  width: 380px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0px 3px 8px rgba(0,0,0,0.25);
  border-radius: 15px;
  z-index: 1;
}

.buttonprofile {
  font-weight: bolder;
  font-size: 25px;
  font-family: 'YarpHanna';
  background: rgba(255, 255, 255, 0.9);
  margin : 20px auto;
  padding: 8px;
  width : 300px;
  height : 50px;
  overflow: hidden;
  text-align : center;
  cursor : pointer;
  border-radius: 15px;
  box-shadow: 0px 1px 2px rgba(0,0,0,2);
  transition: all 0.2s linear;
}

.buttonprofile:hover {
  transform: scale(1.1);
  z-index: 1;
}


/* Winona */
/* .button--winona {
  overflow: hidden;
  padding: 0;
  -webkit-transition: border-color 0.3s, background-color 0.3s;
  transition: border-color 0.3s, background-color 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
  transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
}
.button--winona::after {
  content: attr(data-text);
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 0;
  color: #26A69A;
  -webkit-transform: translate3d(0, 25%, 0);
  transform: translate3d(0, 25%, 0);
}
.button--winona > span {
  display: block;
}
.button--winona.button--inverted {
  color: #7986cb;
}
.button--winona.button--inverted:after {
  color: #fff;
}
.button--winona::after,
.button--winona > span {
  padding: 1em 2em;
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
  transition-timing-function: cubic-bezier(0.2, 1, 0.3, 1);
}
.button--winona:hover {
  border-color: #26A69A;
  background-color: rgba(63, 81, 181, 0.1);
}
.button--winona.button--inverted:hover {
  border-color: #21333C;
  background-color: #21333C;
}
.button--winona:hover::after {
  opacity: 1;
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
}
.button--winona:hover > span {
  opacity: 0;
  -webkit-transform: translate3d(0, -25%, 0);
  transform: translate3d(0, -25%, 0);
} */

</style>