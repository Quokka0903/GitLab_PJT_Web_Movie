<template>
  <div>
    <img class="backimg" :src="require(`@/assets/back/cinema${num}.jpg`)" alt="">
  <div class="holderprofile">
    <form @submit.prevent="logIn">
      <!-- <h3>"{{username}}"님 환영합니다!</h3> -->
      <div @click="GoMovie" class="buttonprofile">평가한 영화 보기</div>
      <div @click="GoReview" class="buttonprofile">리뷰 남긴 영화 보기</div>
      <div @click="LogOut" class="buttonprofile">로그아웃</div>
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
}
</style>