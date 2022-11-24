<template>
<div>
  <img class="backMainReview" src="@/assets/mainback/mainback00.jpg" alt="">
  <br>
  <h1>내가 남긴 리뷰</h1>
  <div id="justify-content" class="container">
    <div class="row justify-content-left">
      <hr>
      <MyReviewItem
      v-for="review in my_reviews"
      :key="`my-review-${review.title}`"
      :review="review"
      @change_review="ChangeReview"
      class="mb-4"/>
    </div>
  </div>
  <ModalTemplate @close="closeModal" v-if="modal">
    <h3>리뷰 수정</h3>
    <b-input 
    @keyup.enter="doSend"
    v-model="title" placeholder="리뷰 제목">
    </b-input>
    <b-textarea
    @keyup.enter="doSend"
    placeholder="나만의 한 줄을 남겨주세요"
    v-model="content"
    ></b-textarea>
    <p>{{content.length}}/50</p>
    <template slot="footer">
      <button @click="doSend" class="custom-btn btn-heart btn-center">완료</button>
    </template>
  </ModalTemplate>
</div>
</template>

<script>
import MyReviewItem from '@/components/MyReviewItem'
import ModalTemplate from '@/components/ModalTemplate'
import axios from 'axios'

export default {
  name: 'MyReviewView',
    data() {
    return {
      my_reviews: [],
      modal: false,
      title: '',
      content: '',
      review_id: null,
    }
  },
  components: {
    MyReviewItem,
    ModalTemplate,
  },
  computed: {
    userId() {
      return this.$route.params.user_id
    }
  },
  methods: {
    getReviews() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/infos/profile/${this.userId}`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.my_reviews = res.data.my_reviews
          this.my_reviews.title = res.data.my_reviews.title
        })
    },
    closeModal() {
      this.modal = false
    },
    doSend() {
      if (this.title.length === 0) {
        alert('제목을 입력해주세요!')
      } else if (this.content.length === 0) {
        alert('내용을 입력해주세요!')
      } else {
        const API_URL = 'http://127.0.0.1:8000'
        axios({
          method: 'put',
          url: `${API_URL}/pages/reviews/${this.review_id}/`,
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
          },
          data: {
            title: this.title,
            content: this.content
          }
        })
          .then((res) => {
            console.log(res)
            this.getReviews()
          })
        this.closeModal()
        this.title = ""
        this.content = ""
        this.review_id = null
      }
    },
    ChangeReview(review_id) {
      this.modal = true
      this.review_id = review_id
    }
  },
  created() {
    this.getReviews()
  }
}
</script>

<style>
.reviewcard{
  transition: all 0.2s linear;
  box-shadow: 0px 3px 8px rgba(0,0,0,0.25);
}
.reviewcard:hover{
  transform: scale(1.05);
  z-index: 1;
}
.reviewtitle{
  font-size: 18px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding-top: 5px; 
}

.reviewitem {
  padding-top: 50px;
  justify-content: center;
}

button + button {
  margin-left: 10px;
}

.backMainReview {
  height: 1500% !important;
  width: 100%;
  content: "";
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 30%;
  top: 0;
  left: 0;
  z-index: -1;
  position: absolute;

}
</style>