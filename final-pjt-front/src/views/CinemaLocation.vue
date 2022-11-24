<template>
  <div>
    <h1>영화관 찾기</h1>
    <div>
      <button @click='geofind'>위치찾기</button>
      <p> {{textContent}} </p>
    </div>
    <div id="map" style="width:500px;height:400px;">
    </div>
    <div class="results">
      <div class="place" v-for="rs in search.results"
      :key=rs.id>
      <h4>{{rs.place_name}}</h4>
      <p>{{rs.address_name}}</p>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: 'CinemaLocation',
  data () {
    return {
      map: null,
      markers: [],
      latitude: '',
      longitude: '',
      textContent: '',
      infowindow: null,
      search: {
        keyword: null,
        pgn: null,
        result: null
      }
    }
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.loadMap()
    } else {
      this.loadScript()
    }
  },
  methods:{
    geofind () {
      if(!("geolocation" in navigator)) {
        this.textContent = 'Geolocation is not available.'
        return
        }
        this.textContent = 'Locating...'
        
        // get position
        navigator.geolocation.getCurrentPosition((pos) => {
        this.latitude = pos.coords.latitude
        this.longitude = pos.coords.longitude
        this.textContent = 'Your location data is ' + this.latitude + ', ' + this.longitude
        }, (err) => {
        this.textContent = err.message;
        })
    },
    loadScript() {
      const script = document.createElement("script")
      script.type = "text/javascript"
      script.src = "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=45abd58f07d2a9ef8f42f8799ce67fda&libraries=services"
      script.onload = () => window.kakao.maps.load(this.loadMap)
      document.head.appendChild(script)
    },
    loadMap() {
      var container = document.getElementById("map")
      var options = {
        center: new window.kakao.maps.LatLng(this.latitude, this.longitude), 
        level: 5,
      }
      this.map = new window.kakao.maps.Map(container, options)
      this.displayMarker([[this.latitude, this.longitude]])
      this.searchPlace()
    },
    displayMarker(markerPositions) {
      if (this.markers.length > 0) {
        this.markers.forEach((marker) => marker.setMap(null))
      }

      const positions = markerPositions.map(
        (position) => new window.kakao.maps.LatLng(...position)
      );

      if (positions.length > 0) {
        this.markers = positions.map(
          (position) =>
            new window.kakao.maps.Marker({
              map: this.map,
              position,
            })
        );

        const bounds = positions.reduce(
          (bounds, latlng) => bounds.extend(latlng),
          new window.kakao.maps.LatLngBounds()
        );

        this.map.setBounds(bounds);
      }
    },
    searchPlace() {
      const keyword = '영화관'
      const ps = new window.kakao.maps.services.Places(this.map)
      const searchOption = {
        location: location,
        radius: 1000,
        size: 5
      }
      ps.keywordSearch(keyword, (data, status, pgn) => {
        console.log(data)
        console.log(pgn)
        console.log(status)
      }, searchOption)

    },
  },
  created() {
    this.geofind()
  }
}
</script>

<style scoped>
#map {
  width: 400px;
  height: 400px;
}
</style>