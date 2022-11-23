<template>
  <div>
    {{moviename}}
  </div>
</template>

<script>
export default {
  name: 'MovieOstView',
  data() {
    return {
      moviename: this.$route.params.moviename
    }
  },
  methods: {

  }
}
</script>

<style>

</style>