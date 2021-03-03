<template>
  <div>
    <strong> Username: {{ user.username }}, Full Name: {{ fullName }} </strong>

    <div v-if="user.isAdmin">
      <p>admin</p>
    </div>
    <!-- <div v-else>
      <p>Not Admin</p>
    </div> -->

    <p>Email:{{ user.email }}</p>
    <p>Admin Status:{{ user.isAdmin }}</p>
    <strong>
      Followers:
      {{ followers }}
    </strong>
    <button @click="followUser">follow</button>
    <tweets
      v-for="tweet in user.tweets"
      :key="tweet.id"
      :username="user.username"
      :tweet="tweet"
      @favourite="toggleFavourite"
    />
  </div>
</template>

<script>
import tweets from "./Tweet.vue";
export default {
  name: "UserProfile",
  components: { tweets },
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
        tweets: [
          { id: 1, content: "twitter is great.." },
          { id: 2, content: "testing this application's components.." },
          { id: 3, content: "reddit is great." },
        ],
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
      this.followers = this.followers + 1;
    },
    toggleFavourite(id) {
      console.log(`fav-ed tweet ${id}`);
    },
  },
  mounted() {
    this.followUser();
    console.log(
      "this function is mounted right now and the follow is appended by 1."
    );
  },
  watch: {
    followers(newfollowerCount, old_followerCount) {
      if (old_followerCount < newfollowerCount) {
        console.log(this.user.username + " has gained a follower");
      }
    },
  },
};
</script>
