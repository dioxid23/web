<template>
  <div class="home">
    <Home_page/>
  </div>
</template>

<script>
// @ is an alias to /src
import Home_page from "../components/Home_page.vue"

export default {
  name: 'Home',
  components: {
    Home_page
  }
}
</script>

