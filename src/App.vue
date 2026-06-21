<script setup>
import Header from "@/components/layouts/Header.vue";
import { useRoute } from "vue-router";
const route = useRoute();
</script>

<template>
  <div id="app">
    <Header v-if="route.name !== 'Admin' && route.name !== 'Login'" />
    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<style>

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

body {
  font-family:
    "Inter",
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Helvetica,
    Arial,
    sans-serif;
  color: #1e293b;
  background: #fff;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  text-decoration: none;
}

img {
  max-width: 100%;
  display: block;
}
</style>
