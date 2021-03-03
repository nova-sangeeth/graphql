<template>
  <div id="app">
    <user-profile/>
    <!-- <tweets/> -->
  </div>
</template>

<script>
// import tweets from './components/Tweet.vue'
import UserProfile from './components/userProfile.vue'
export default {
  name: "App",
  components: {
    // tweets, 
    UserProfile,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: None;
  text-align: justify;
  color: #4d2c50;
  margin-top: 60px;
  padding: 25px;
}
</style>
