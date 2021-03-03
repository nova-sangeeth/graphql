<template>
  <div class="tweet-box" @click="favouriteTweet(tweet.id)">
    <div class="tweet-user-box">{{ username }}</div>
    <div>
      {{ tweet.id }}
    </div>
    <div>
      {{ tweet.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: "tweets",
  props: {
    username: {
      type: String,
      required: true,
    },
    tweet: {
      type: Object,
      required: false,
    },
  },
  methods: {
    favouriteTweet(id) {
        this.$emit('favourite', id)
    }
  }
};
</script>

<style>
.tweet-box {
    padding: 3px;
    color: rgb(0, 4, 255);
    background-color: rgb(202, 214, 214);
    border-radius: 3px;
    margin: 10px;
    box-sizing: border-box;
    
}
.tweet-user-box {
    padding: 10px;
    color: rgb(0, 0, 0);
    /* background-color: rgb(120, 161, 52); */
    margin: 10px;
    width: auto;
    border-radius: 5px;
}
</style>