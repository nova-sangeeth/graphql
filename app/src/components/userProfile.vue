<template>
  <div class="user_profile">
    <div class="user_profile_panel">
      <strong>
        Username: {{ user.username }}
        <br />
        Full Name: {{ fullName }}
      </strong>

      <div v-if="user.isAdmin">
        <p class="user_profile_admin_badge">admin</p>
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
    </div>

    
    <button @click="followUser">follow</button>
    <div>
      <CreateTweet
      @create-tweet="CreateNewTweet"
      />
    </div>
    
    <tweets
      v-for="tweet in user.tweets"
      :key="tweet.id"
      :username="user.username"
      :tweet="tweet"
      @favourite="toggleFavourite"
      class="tweet_wraper"
    />
  </div>
</template>

<script>
import tweets from "./Tweet.vue";
import CreateTweet from "./CreateTweet.vue";
export default {
  name: "UserProfile",
  components: { tweets, CreateTweet },
  data() {
    return {
      // newtweetdata: "",
      // newtweettype: "instant",
      // tweetTypes: [
      //   { value: "draft", name: "Draft" },
      //   { value: "instant", name: "Instant Tweet" },
      //   { value: "timed", name: "timed tweet" },
      // ],
      followers: 0,
      user: {
        id: 1,
        username: "nova_sangeeth",
        firstName: "Nova",
        lastName: "Sangeeth",
        email: "novasangeeth@gg.com",
        isAdmin: true,
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
    newTweetCharCount() {
      return this.newtweetdata.length;
    }
  },
  methods: {
    followUser() {
      this.followers = this.followers + 1;
    },
    toggleFavourite(id) {
      console.log(`fav-ed tweet ${id}`);
    },
    CreateNewTweet(tweet) {
      this.user.tweets.push({id: this.user.tweets.length + 1, content: tweet });
        // this.newtweetdata = ""; 
      }
      // else {
      //   alert('this is a draft item')
      // }
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

<style lang="scss">
.user_profile {
  display: grid;
  grid-template-columns: 1fr, 3fr;
  grid-gap: 15px;
  padding: 50px 5%;
}
.user_profile_panel {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: white;
  border-radius: 5px;
  border: 1px solid black;

  h1 {
    margin: 0px;
  }
  .user_profile_admin_badge {
    background: palegreen;
    color: black;
    border-radius: 10px;
    margin-right: auto;
    padding: 10px;
  }
}

.create_tweet {
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  
  .exceeded {
    border-color: red;
    background: pink;
  }
  .instant-color {
    color: green;
    background: yellow;
  }

  .tweet_wraper {
    display: grid;
    grid-gap: 10px;
  }
  .tweet_type {
    margin: 10px;
    color: blueviolet
  }
  .new_tweet_form {
    display: flex;
    border-top: 2px;
    padding: 10px;
    flex-direction: column;
    margin: 10px;
  }
}
</style>
