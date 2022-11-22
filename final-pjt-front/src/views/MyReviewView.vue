<template>
<div>
  <br>
  <h1>내가 남긴 리뷰</h1>
  <hr>
  <br>
  <div class="row justify-content-around">
    <MyReviewItem
    v-for="review in my_reviews"
    :key="`my-review-${review.title}`"
    :review="review"
    @change_review="ChangeReview"
    />
  </div>
  <ModalTemplate @close="closeModal" v-if="modal">
    <h3>리뷰 수정</h3>
    <div>제목: <input @keyup.enter="doSend" v-model="title"></div>
    <div>내용: <input @keyup.enter="doSend" v-model="content"></div>
    <template slot="footer">
      <button @click="doSend">제출</button>
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

</style>