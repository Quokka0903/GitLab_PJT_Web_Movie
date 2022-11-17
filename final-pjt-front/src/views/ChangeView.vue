<template>
  <div>
    <h1>Change Password</h1>
    <form @submit.prevent="Change">
      <!-- <label for="original">Origin Password : </label>
      <input type="text" id="original" v-model="original"><br> -->

      <label for="newpassword"> New Password : </label>
      <input type="password" id="newpassword" v-model="newpassword"><br>

      <label for="newpassword2"> New Password Confirmation : </label>
      <input type="password" id="newpassword2" v-model="newpassword2"><br>

      <input type="submit" value="Change">
    </form>
  </div>
</template>

<script>
export default {
  name: 'ChangeView',
  data() {
    return {
      // original: null,
      newpassword: null,
      newpassword2: null,
    }
  },
  methods: {
    Change() {
      // const original = this.original
      const newpassword = this.newpassword
      const newpassword2 = this.newpassword2

      const payload = {
        // original,
        newpassword,
        newpassword2,
      }

      this.$store.dispatch('change', payload)
    }
  }
}
</script>

<style>

</style>