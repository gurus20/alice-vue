<template>
  <div>
    <p class="h5 my-3 text-center" style="#553939">Get Started</p>
    <div class="container b-light rounded-3 p-4">
      <form action="#">
        <div class="d-flex gs-design w-50 m-auto">
          <input
            type="text"
            class="form-control me-3"
            name="search"
            id="search"
            placeholder="Search coffee or tea..."
          />
          <input
            type="submit"
            class="btn btn-success btn-sm"
            value="Login/Signup"
          />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "GetStarted",
};
</script>

<style>
</style>