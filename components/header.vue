<template>
  <nav class="header link-spacing">

    <div class="header-btn-right link-spacing">
      <a href="" class="link-spacing">Home</a>
      <a href="" class="link-spacing">login</a>
      <a href="" class="link-spacing">sign-up</a>
      <a href="" class="link-spacing">contact</a>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style>
.header-btn-right {
  float: right;
}
.header-logo-left {
  float: left;
}
.header {
  display: flex;
  flex-basis: auto;
  background-color: #d4d4d4;
  border-radius: 10px;
  flex-grow: 1;
  -ms-flex-align: center;
  align-items: center;
  height: 100%;
}
.link-spacing {
  margin: 10px;
}
</style>
