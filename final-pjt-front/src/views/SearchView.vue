<template>
  <div id="justify-content" class="container">
    <img class="backMain" src="@/assets/mainback/mainback00.jpg" alt="">
    <div class="row justify-content-around">
      <div class="search-box">
        <input
        class="inputsearch" 
        type="text" 
        placeholder="영화 제목을 입력하세요!"
        @input="search"
        />
      </div>
    </div>
  <div v-if="results.length" class="row justify-content-start">
    <div class="row g-3">
    <h4 class="go">"{{ this.title_search  }}" 검색 결과가 {{ searchcount }}개 있습니다.</h4>
    <hr>
    <SearchItem
      v-for="result in results"
      :key="result.id"
      :result="result"
      class="col-3"
      />
    </div>
  </div>
  <div v-else>
    <h5 class="go">검색된 결과가 없습니다.</h5>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import SearchItem from '@/components/SearchItem'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'SearchView',
  data(){
    return {
      results: [],
      // title_info: null,
      title_search : null,
    }
  },
  components: {
    SearchItem,
  },
  methods:{
    search(event) {
      const search_input = event.target.value.trim()
      if (!search_input) {
        // alert('검색어를 입력해주세요!')
        return
      }
      this.title_search = search_input
      axios({
        method : 'get',
        url: `http://127.0.0.1:8000/pages/search/`,
        params:{
          "search" : search_input, 
        },
      })
        .then((response) => {
          console.log(response)
          this.results = response.data
          // this.title_search = this.search_input
          // this.title_info = null
        }) 
        .catch((error)=> {
          console.log(error)
        })
    }
  },
  computed:{
    searchcount() {
      return this.results.length
    }
  }
}
</script>

<style>
.card {
  margin-top: auto;
  margin-bottom: auto;
  background-size: cover;

}
.card-title{
  font-size: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  padding-top: 5px; 
}
.go {
  margin-top: 10px;
}
.search {
    position: relative;
    text-align: center;
    width: 400px;
    margin: 0 auto;
}
.inputsearch {
    width: 50%;
    border-radius: 20px;
    border: 2px solid #bbb;
    margin: 10px 0;
    padding: 10px 12px;
}
</style>