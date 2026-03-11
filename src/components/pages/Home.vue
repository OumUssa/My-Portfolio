<template>
  <div class="page">
    <BannerSection />
    <ProjectsSection />
    <ServicesSection />
    <ContactSection />
    <Footer />
  </div>
</template>

<script setup>
import BannerSection from "../Bases/BannerSection.vue";
import ProjectsSection from "../Bases/ProjectsSection.vue";
import ServicesSection from "../Bases/ServicesSection.vue";
import ContactSection from "../Bases/ContactSection.vue";
import Footer from "../layouts/footer.vue";
</script>

<style scoped>
.page {
  overflow-x: hidden;
}
</style>
