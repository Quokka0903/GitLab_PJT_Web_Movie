<template>
  <div>
    <h1>영화관 찾기</h1>
    <div>
      <button @click='geofind'>위치찾기</button>
      <p> {{textContent}} </p>
    </div>
    <div id="map" style="width:500px;height:400px;">

    </div>
  </div>
</template>

<script>
export default {
  name: 'CinemaLocation',
  data () {
    return {
      map: null,
      markers: [],
      latitude: '',
      longitude: '',
      textContent: ''
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
    // getMap() {
      
    //   const container = document.getElementById('map')
    //   const options = {
    //     center: new kakao.maps.LatLng(this.latitude, this.longitude),
    //     level: 3,
    //   }
    //   const map = new kakao.maps.Map(container, options)
    // }
    // ,
    loadScript() {
      const script = document.createElement("script")
      script.type = "text/javascript"
      script.src = "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=45abd58f07d2a9ef8f42f8799ce67fda"
      script.onload = () => window.kakao.maps.load(this.loadMap)
      document.head.appendChild(script)
    },
    loadMap() {
      var container = document.getElementById("map")
      var options = {
        center: new window.kakao.maps.LatLng(this.latitude, this.longitude), 
        level: 3,
      }
      this.map = new window.kakao.maps.Map(container, options)
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