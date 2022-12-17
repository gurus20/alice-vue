<template>
  <div>
    <header class="p-3 border-bottom">
      <div class="container d-flex justify-content-between">
        <a
          href="#"
          class="
            col-3
            d-flex
            align-items-center
            text-decoration-none text-secondary
          "
        >
          <img
            src="../../assets/images/cattie.png"
            alt="logo"
            width="35"
            class="me-3"
            style="border-radius: 50%"
          />
          Alice Coffee House
        </a>
        <div class="col-5">
          <nav class="gs-design">
            <ul class="nav">
              <li class="nav-item me-2">
                <router-link to="/" class="nav-link">Home</router-link>
              </li>
              <li class="nav-item me-2">
                <router-link to="/about" class="nav-link">About</router-link>
              </li>
              <li class="nav-item me-2">
                <router-link to="/order" class="nav-link">Order</router-link>
              </li>
              <li class="nav-item me-2">
                <router-link to="/help" class="nav-link">Help</router-link>
              </li>
            </ul>
          </nav>
        </div>
        <div class="col-4 d-flex align-items-center gs-design">
          <input
            type="text"
            class="form-control me-3"
            name="search"
            id="search"
            placeholder="Search coffee or tea..."
          />
          <img
            src="../../assets/images/dodo.png"
            alt="profile"
            width="35"
            style="border-radius: 50%"
          />
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: "HeaderComp",
};
</script>
<style>
.gs-design input {
  border-radius: 100px;
  padding: 7px 20px;
}

.gs-design .nav-link {
  color: #141d29;
}

.gs-design .nav-item:hover {
  background: #e7e9eb;
  border-radius: 10px;
}
</style>