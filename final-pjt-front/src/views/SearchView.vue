<template>
<div>
  <div class="input-group mb-3 search" @submit.prevent>
    <input 
    type="text" 
    v-model.trim="title_info" 
    placeholder="영화 제목을 입력하세요!"
    @keyup.enter="search"/>
  </div>
  <br>
  <br>
  <div v-if="results.length" class="row justify-content-start">
    <SearchItem
    v-for="result in results"
    :key="result.id"
    :result="result"
    class="col-3"
    />
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
.container-1 {
  width: 300px;
  vertical-align: middle;
  white-space: nowrap;
  position:relative;
}

.search {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
}

</style>