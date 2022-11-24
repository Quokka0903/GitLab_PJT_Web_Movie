<template>
  <div class="background">
    <p v-if="!background" class="loading">
    <hr>
    <div>
    <p @click="MoveBack()" class="button btnPush btnBlueGreen back-neobi1">영화로 돌아가기</p> 
    <!-- <p @click="MoveBack()" class="button btnPush btnBlueGreen neo3.5%>새 리뷰 남기기</p> -->
    </div>
    <!-- <br>    <br>    <br> -->
    <br>    <br>    <br>
    <h2> {{movie_title}}의 리뷰리스트</h2>
    <hr class="hr-dotted">
    <ReviewDetail
    v-for="(id, index) in review_ids"
    :review_id="id.id"
    :key="`review-${index}`"
    @change_review="ChangeReview"
    :ischanged="ischanged"
    @resetid="ResetId"
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
          <button @click="doSend" class="custom-btn btn-heart btn-center RLV-center">완료</button>
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
      movie_title: null,
      ischanged: null,
    }
  },
  components: {
    ReviewDetail,
    ModalTemplate
  },
  methods: {
    
    getReviewids() {
      console.log('working')
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
          console.log(this.review_ids)
        })
        .then(() => {
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/pages/movies/${movie_id}/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              this.movie_title = res.data.title
            })
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
            console.log('res',res)
            this.ischanged = res.data.id 
          })
        this.closeModal()
        this.title = ""
        this.content = ""
        this.review_id = null
      }
    },
    MoveBack() {
      this.$router.go(-1)
    },
    ResetId() {
      this.ischanged = null
    }
  },
  created() {
    this.getReviewids()
  }
}
</script>

<style>
.hr-dotted {
border : 0px;
border-top: 2px dotted #8866aa;
width: 50%;
margin-left: 25%;
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
.btnFade.btnBlueGreen {
  width: 85px;
  font-size: 100%;
}
.btnFade.btnBlueGreen:hover {
  background: #14554f;
}
.back-neobi1 {
  left: 43.4% !important;
  width: 13rem !important;
}
.RLV-center {
  left: 0% !important;
}
/* .neobi2 {
  left: 50% !important;
  width: 13rem !important;
} */
</style>