<template>
  <div class="page-cinema">
    <img class="backMain back-cinema" src="@/assets/mainback/mainback00.jpg" alt="">
    <div class="map-area">
      <div class="searchbox">
        <div>
          <br>
          <p type="submit" @click="searchPlace" class="button btnPush btnBlueGreen btn-align btn-cinema"> 영화관 찾기 </p>
          </div>
          <br>          <br>          <br>
        <div class="results">
          <div class="place" v-for="rs in search.results"
          :key="rs.id"
          @click="showPlace(rs)">
            <h4>{{ rs.place_name }}</h4>
            <div class="addr">{{ rs.address_name }}</div>
          </div>
      </div>
    </div>
      <KakaoMap class="kmap" :options="mapOption"/>
    </div>
  </div>
</template>

<script>
import KakaoMap from '@/components/KakaoMap'
export default {
  name: 'CinemaLocation',
  components: {
    KakaoMap,
  },
  data() {
    return {
      mapOption: {
        center: {
          lat: 33.450701,
          lng: 126.570667,
        },
        level: 8
      },
      search: {
        keyword: null,
        pgn: null,
        results: [],
      },
    }
  },
  methods: {
    searchPlace() {
      const keyword = "영화관"
      const ps = new window.kakao.maps.services.Places()
      ps.keywordSearch(keyword, (data, status, pagination) => {
        console.log(status)
        this.search.keyword = keyword
        this.search.pgn = pagination
        this.search.results = data
      })
    },
    showPlace(place) {
      console.log(place)
      this.mapOption.center = {
        lat: place.y,
        lng: place.x,
      }
    },
    geoFind() {
      if(!("geolocation" in navigator)) {
        return
        }
        // get position
        navigator.geolocation.getCurrentPosition((pos) => {
        this.mapOption.center.lat = pos.coords.latitude
        this.mapOption.center.lng = pos.coords.longitude
        }, (err) => {
        console.log(err)
        })
    }
  },
  created() {
    this.geoFind()
  }
}
</script>

<style lang="scss">
.map-area {
  display: flex;
  position: relative;
  .searchbox {
    position: absolute;
    top: 0;
    left: 0;
    height: 600px;
    z-index: 10000;
    background-color: #ffffffaa;
    width: 300px;
    display: flex;
    flex-direction: column;
    .results {
      flex: 1 1 auto;
      overflow-y: auto;
      .place{
        padding: 8px;
        cursor: pointer;

        &:hover {
          background-color: rgba(240, 248, 255, 0.657)
        }
        h4: {
          margin: 0;
        }
      }
    }
  }
  .kmap {
    flex: 1 1 auto;
    height: 600px;
  }
}
.btn-cinema {
  width: 60% !important;
  left: 20% !important;
}
// .back-cinema {
//   height: 110% !important;
// }

</style>