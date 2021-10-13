<template>
  <div class="main-bg">
    <div class="login-container content">
      <form action="" method="post">
        <input
          class="input"
          type="text"
          name="Username"
          placeholder="Username"
          id=""
        />
        <input
          class="input"
          type="password"
          name="Password"
          placeholder="Password"
          id=""
        />
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.login-container {
  background-color: rgb(127, 187, 255);
  height: auto;
  width: auto;
  border-radius: 20px;
  /* border: 1px solid rgb(85, 85, 85); */
  display: grid;
  place-items: center;
}
.content {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.input {
  margin: 10px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid white;
}
.submit-button {
  align-content: center;
}
form {
  padding: 10px;
  margin: 10px;
}
.main-bg {
  background: rgb(2, 0, 36);
  background: linear-gradient(
    90deg,
    rgba(2, 0, 36, 1) 0%,
    rgba(228, 130, 255, 1) 61%,
    rgba(0, 212, 255, 1) 100%
  );
}

</style>