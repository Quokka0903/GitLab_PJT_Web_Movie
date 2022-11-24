<template>
  <div>
    {{ischanged}}
    <p>작성자: {{review?.username}}</p>
    <p>좋아요 수: <span :id="`review-${review?.id}`">{{review?.like_users_count}}</span></p>
    <h4>{{review?.title}}</h4>
    <p>{{review?.content}}</p>
    <div v-if="userId != review?.user">
      <p class="button btnFade btnBlueGreen like-neoby" v-if="review?.like_users.includes(userId)" :id="`button-${review?.id}`" @click="LikeReview(review.id)">좋아요 취소</p>
      <p class="button btnFade btnBlueGreen like-neoby" v-else :id="`button-${review?.id}`" @click="LikeReview(review.id)">좋아요</p>
    </div>
    <div v-else>
      <p @click="ChangeReview(review.id)" class="button btnFade btnBlueGreen neoby1">수정</p>
      <p @click="DeleteReview(review.id)" class="button btnFade btnBlueGreen neoby2">삭제</p>
    </div>
    <br>
    <br>
    <hr class="hr-dotted">
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "ReviewDetail",
  data() {
    return {
      review: null,
      userId: null,
    }
  },
  props: {
    review_id: Number,
    ischanged: Number
  },
  methods: {
    getReviews() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/reviews/${this.review_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.review = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    LikeReview(review_id) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/pages/reviews/${review_id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          const like = document.getElementById(`review-${res.data.pk}`)
          like.innerText = res.data.like_count
          const button = document.getElementById(`button-${res.data.pk}`)
          if (res.data.is_liked) {
            button.innerText = '좋아요 취소'
          } else {
            button.innerText = '좋아요'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUserId() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.userId = res.data.pk
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ChangeReview(review_id) {
      this.$emit('change_review', review_id)
    },
    DeleteReview(review_id) {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'delete',
        url: `${API_URL}/pages/reviews/${review_id}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          alert('리뷰가 삭제되었습니다!')
          this.$router.go()
        })
    },
  },
  created() {
    this.getReviews()
    this.getUserId()
  },
  watch: {
    ischanged() {
      if (this.ischanged === this.review_id) {
        this.getReviews()
        this.$emit('resetid')
      }
    }
  }
}
</script>

<style>
.neoby1 {
  left: 30% !important;
}
.neoby2 {
  left: 60% !important; 
}
.custom-btn {
  left: -9%;

  width: 240px;
  height: 40px;
  padding: 10px 25px;
  border: 0px solid #26A69A;
  font-family: 'DuHanna';
  font-weight: 500;
  font-size: 1.5rem;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}
.btn-heart {
  line-height: 40px;
  padding: 0;
  background: transparent;
  position: relative;
  z-index: 2;
  color: #fff;
  -webkit-perspective: 300px;
  perspective: 300px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
}
.btn-heart:hover{
  color: #26A69A;
}
.btn-heart:after {
  position: absolute;
  content: "";
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #26A69A;
  z-index: -1;
  -webkit-transform-origin: center bottom;
  transform-origin: center bottom;
  -webkit-transform: rotateX(0);
  transform: rotateX(0);
  transition: all 0.3s ease;
}
.btn-heart:hover:after {
  -webkit-transform: rotateX(-180deg);
  transform: rotateX(-180deg);
}

p.button {
  display: block;
  position: absolute;
  left: 59.3%;
  float: left;
  width: 250px;
  padding: 0;
  margin: 10px 20px 10px 0;
  font-weight: 600;
  font-size: 130%;
  text-align: center;
  line-height: 45px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
}
.btnBlueGreen {
  background: #26A69A;
}
.btnFade.btnBlueGreen {
  width: 85px;
  font-size: 100%;
}
.btnFade.btnBlueGreen:hover {
  background: #14554f;
}
.btnPush:hover {
  margin-top: 15px;
  margin-bottom: 5px;
}
.btnBlueGreen.btnPush {
  box-shadow: 0px 5px 0px 0px #14554f;
}
.btnBlueGreen.btnPush:hover {
  box-shadow: 0px 0px 0px 0px #14554f;
}

.btn-center {
  left: 0%
}

.like-neoby {
  left: 47.3% !important;
}
</style>