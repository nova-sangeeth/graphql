<template>
  <header>
    <nav>
      <div class="logo">
        <a href="">
          <h1>HEllo There...</h1>
        </a>
      </div>
      <div class="button-right-side">
        <a href="">home</a>
        <a href="">about</a>
        <a href="">login</a>
        <a href="">signup</a>
      </div>
    </nav>
  </header>
</template>

<script>
export default {};
</script>

<style>
nav {
  margin: 15px;
  padding: 15px;
}
header {
  border-block: 1px;
  background-color: aqua;
  border-block-color: gray;
}
.logo {
  float: left;
}
.button-right-side {
  float: right;
  margin: 25px;
}
a {
  text-decoration: none;
  margin: 15px;
  padding: 10px;
}
</style>