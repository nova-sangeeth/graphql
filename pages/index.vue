<template>
<header></header>
  <!-- <todo/> -->
</template>

<script>
import todo from './todo.vue';
export default {
  components: { todo },};
</script>


<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
}

body {
  background: rgb(238, 174, 202);
  background: radial-gradient(
    circle,
    rgba(238, 174, 202, 1) 0%,
    rgba(148, 187, 233, 1) 100%
  );
}
a {
  text-decoration: none;
}
p {
  margin-bottom: 15px;
}
p:lost-of-type {
  margin-bottom: 0px;
}
</style>