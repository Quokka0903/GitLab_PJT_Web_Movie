<template>
  <div>
    <img class="backimg1" :src="require(`@/assets/back/cinema${num}.jpg`)" alt="">
      <div class="holder1">
        <form @submit.prevent="Change">
          <!-- <label for="original">Origin Password : </label>
            <input type="text" id="original" v-model="original"><br> -->
            <h1>Change Password</h1>
            <div>
              <label class="inputText" for="newpassword"> New Password</label><br>
              <input class="input inputLogin" type="password" id="newpassword" v-model="newpassword"><br>
              <label class="inputText" for="newpassword2"> New Password Confirmation</label>
              <input class="input inputLogin" type="password" id="newpassword2" v-model="newpassword2"><br>
              <input class="buttonprofile1" type="submit" value="Change">
            </div>
        </form>
    </div>
  </div>

</template>

<script>
import _ from 'lodash'
export default {
  name: 'ChangeView',
  data() {
    return {
      // original: null,
      newpassword: null,
      newpassword2: null,
      num: null,
    }
  },
  methods: {
    getBack() {
      this.num = _.sample(_.range(1, 28))
    },
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
  },
  created() {
    this.getBack()
  }
}
</script>

<style>
.holder1{
  background: rgba(255, 255, 255, 0.7);
  padding: 20px;
  width: 450px;
  margin: 0 auto;
  position: relative;
  top: 25rem;
  transform: translateY(-65%);
  box-shadow: 0px 3px 8px rgba(0,0,0,0.5);
  border-radius: 20px;
}

.backimg1 {
  height: 100%;
  width: 100%;
  content: "";
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  top: 0;
  left: 0;
  z-index: -1;
  position: absolute;
}

.buttonprofile1 {
  font-weight: bolder;
  font-size: 25px;
  font-family: 'YarpHanna';
  background: rgba(255, 255, 255, 0.9);
  margin : 20px auto;
  padding: 8px;
  width : 200px;
  height : 50px;
  overflow: hidden;
  text-align : center;
  cursor : pointer;
  border-radius: 15px;
  box-shadow: 0px 1px 2px rgba(0,0,0,3);
  transition: all 0.2s linear;
}

.buttonprofile1:hover {
  transform: scale(1.1);
  z-index: 1;
}
</style>