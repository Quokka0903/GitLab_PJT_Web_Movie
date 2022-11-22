<template>
  <div>
    <p>리뷰리스트</p>
    <ReviewDetail
    v-for="(id, index) in review_ids"
    :review_id="id.id"
    :key="`review-${index}`"
    @change_review="ChangeReview"
    />
    <ModalTemplate @close="closeModal" v-if="modal">
    <h3>리뷰 수정</h3>
    <b-input @keyup.enter="doSend" v-model="title" placeholder="리뷰 제목"></b-input>
    <b-textarea
    @keyup.enter="doSend"
    placeholder="당신만의 한 줄을 남겨주세요"
    v-model="content"
    ></b-textarea>
    <template slot="footer">
      <button @click="doSend">제출</button>
    </template>
  </ModalTemplate>
  </div>
</template>
<script>
import ModalTemplate from '@/components/ModalTemplate'
import ReviewDetail from '@/components/ReviewDetail'
import axios from 'axios'

export default {
  name: 'ReviewListView',
  data() {
    return {
      review_ids: [],
      modal: false,
      title: '',
      content: '',
      review_id: null,
    }
  },
  components: {
    ReviewDetail,
    ModalTemplate
  },
  methods: {
    
    getReviewids() {
      const movie_id = this.$route.params.movie_id
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/pages/movies/reviews/${movie_id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.review_ids = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    ChangeReview(review_id) {
      this.modal = true
      this.review_id = review_id
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
            this.getReviewids()
          })
        this.closeModal()
        this.title = ""
        this.content = ""
        this.review_id = null
      }
    },
  },
  created() {
    this.getReviewids()
  }
}
</script>

<style>

</style>