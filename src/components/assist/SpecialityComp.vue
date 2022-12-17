<template>
  <div class="b-light">
    <div class="container py-4">

      <p class="h5 my-3 text-center" style="#553939">Our Offerings at Best</p>

      <div class="mt-3 d-flex justify-content-between">
        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/Bestseller.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Bestseller</p>
          </div>
        </a>

        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/Drinks.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Drinks</p>
          </div>
        </a>

        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/ReadyToEat.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Ready To Eat</p>
          </div>
        </a>

        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/Food.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Food</p>
          </div>
        </a>
        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/Merchandise.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Merchandise</p>
          </div>
        </a>
        <a href="#" class="a-hover-bg rounded-4 text-secondary">
          <div class="p-4 text-center">
            <img
              src="../../assets/images/CoffeeAtHome.jpg"
              alt="Bestseller"
              class="image-round border border-3 shadow img-fluid"
              width="100"
            />
            <p class="mb-0 mt-3">Coffee At Home</p>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SepecialiltyComp",
};
</script>

<style>
.image-round {
  border-radius: 50%;
}

.b-light {
  background: #eeeeee;
}

a {
  text-decoration: none;
}

.a-hover-bg:hover {
  background: #553939;
  color: white !important;
}

</style>