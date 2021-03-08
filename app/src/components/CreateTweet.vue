<template>
  <div class="create_tweet">
    <form
      class="new_tweet_form"
      @submit.prevent="CreateNewTweet"
      :class="{ exceeded: newTweetCharCount > 80 }"
    >
      <label for="new tweet">
        <strong>new tweet</strong>
        ({{ newTweetCharCount }})
      </label>
      <textarea
        name=""
        id="new tweet"
        cols="30"
        rows="4"
        v-model="newtweetdata"
      ></textarea>

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
  </div>
</template>

<script>
export default {
  name: "CreateTweet",
  data() {
    return {
      newtweetdata: "",
      newtweettype: "instant",
      tweetTypes: [
        { value: "draft", name: "Draft" },
        { value: "instant", name: "Instant Tweet" },
        { value: "timed", name: "timed tweet" },
      ],
    };
  },
  computed: {
    newTweetCharCount() {
      return this.newtweetdata.length;
    },
  },
  methods: {
    CreateNewTweet() {
      if (this.newtweetdata == "") {
        alert("There is nothing to tweet.");
      }
      if (this.newtweetdata && this.newtweettype != "draft") {
        // this.user.tweets.push({
        //   id: this.user.tweets.length + 1,
        //   content: this.newtweetdata,
        // });
        this.$emit('create-tweet', this.newtweetdata)
        this.newtweetdata = "";
      }
    },
  },
};
</script>

<style lang="scss" scoped>
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
    color: blueviolet;
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
