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

    <form class="new_tweet_form" @submit.prevent="CreateNewTweet">
      <label for="new tweet"><strong>new tweet</strong></label>
      <textarea name="" id="new tweet" cols="30" rows="4" v-model="newtweetdata"></textarea>

      <div class="tweet_type">
        <label for="newTweetType"><strong>create tweet type.</strong></label>
        <select name="" id="newTweetType" v-model="newtweettype">
          <option
            :value="option.value"
            v-for="(option, index) in tweetTypes"
            :key="index"
          >
            {{ option.name }}
          </option>
        </select>
      </div>
      <button type="submit">Tweet out.</button>
    </form>

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
      newtweetdata: '',
      newtweettype: 'instant',
      tweetTypes: [
        {value: 'draft', name: 'Draft'},
        {value: 'instant', name: 'Instant Tweet'},
        {value: 'timed', name: 'timed tweet'}
      ],
      followers: 0,
      user: {
        id: 1,
        username: "nova_sangeeth",
        firstName: "Nova",
        lastName: "Sangeeth",
        email: "novasangeeth@gg.com",
        isAdmin: false,
        tweets: [
          // { id: 1, content: "twitter is great.." },
          // { id: 2, content: "testing this application's components.." },
          // { id: 3, content: "reddit is great." },
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
    CreateNewTweet() {
      if (this.newtweetdata == '' ){
        alert('There is nothing to tweet.')
      }
      if (this.newtweetdata && this.newtweettype != 'draft') {
        this.user.tweets.push({
            id: this.user.tweets.length + 1,
            content: this.newtweetdata
        })
        this.newtweetdata = ""
      }
      // else {
      //   alert('this is a draft item')
      // }
    }
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

<style>
.new_tweet_form {
  display: flex;
  border-top: 2px;
  padding: 10px;
  flex-direction: column;
  margin: 10px;
}
.tweet_type {
  margin: 10px
}
</style>
