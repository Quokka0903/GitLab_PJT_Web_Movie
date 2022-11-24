<template>
  <div ref="map"></div>
</template>

<script>
let kakao = window.kakao
export default {
  props: ['options'],
  data() {
    return {
      mapInstance: null,
      markers: [],
      mylat: null,
      mylng: null,
    }
  },
  mounted() {
    kakao = kakao || window.kakao
    var container = this.$refs.map
    kakao.maps.load(() => {
      const {center, level} = this.options
      this.mylat = center.lat
      this.mylng = center.lng
      this.mapInstance = new kakao.maps.Map(container, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level: level
      })
      this.displayMarker([[this.mylat, this.mylng]])
    })

  },
  watch: {
    "options.center"(cur) {
      this.mapInstance.setCenter(
        new kakao.maps.LatLng(cur.lat, cur.lng))
      this.displayMarker([[cur.lat, cur.lng], [this.mylat, this.mylng]])
    }
  },
  methods: {
    displayMarker(markerPositions) {
      if (this.markers.length > 0) {
        this.markers.forEach((marker) => marker.setMap(null))
      }

      const positions = markerPositions.map(
        (position) => new kakao.maps.LatLng(...position)
      );

      if (positions.length > 0) {
        this.markers = positions.map(
          (position) =>
            new kakao.maps.Marker({
              map: this.mapInstance,
              position,
            })
        );

        const bounds = positions.reduce(
          (bounds, latlng) => bounds.extend(latlng),
          new kakao.maps.LatLngBounds()
        );

        this.mapInstance.setBounds(bounds);
      }
    }
  }
}
</script>

<style>
.kmap {
  width: 100%;
  height: 600px;
}
</style>