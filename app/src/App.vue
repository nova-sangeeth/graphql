<template>
  <div id="app">
    <p>{{ user.username }}</p>
  </div>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      followers: 0,
      user: {
        id: 1,
        username: "nova",
        firstName: "Nova",
        lastName: "Sangeeth",
        email: "novasangeeth@gg.com",
        isAdmin: false,
      },
    };
  },
  computed: {
    fullName() {
      return `${this.user.firstName} ${this.user.lastName}`;
    },
  },
  methods: {
    followUser() {
      this.followers = this.followers + 1
    }
  },
  mounted() {
    this.followUser();
    console.log("this function is mounted right now and the follow is appended by 1.")
  },
  watch: {
    followers(newfollowerCount, old_followerCount) {
      if (old_followerCount < newfollowerCount) {
        console.log(this.user.username + " has gained a follower")
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
