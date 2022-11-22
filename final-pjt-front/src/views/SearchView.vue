<template>
<div id="justify-content" class="container">
  <div class="row justify-content-around" @submit.prevent>
    <input 
    type="text" 
    v-model.trim="title_info" 
    placeholder="영화 제목을 입력하세요!"
    @keyup.enter="search"/>
  </div>
  <hr>
  <div v-if="results.length" class="row justify-content-start">
    <div class="row g-4">
      <SearchItem
      v-for="result in results"
      :key="result.id"
      :result="result"
      class="col-3"
      />
    </div>
  </div>
  <div v-else>
    <p>검색된 결과가 없습니다.</p>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import SearchItem from '@/components/SearchItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'SearchView',
  data(){
    return {
      results: [],
      title_info: null,
    }
  },
  components: {
    SearchItem,
  },
  methods:{
    search() {
      axios({
        method : 'get',
        url: `${API_URL}/pages/search/`,
        params:{
          "search" : this.title_info,    
        },
      })
        .then((response) => {
          this.results = response.data
          console.log(response.data)
          this.title_info = null
        }) 
        .catch((error)=> {
          console.log(error)
        })
    }
  },
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

</style>