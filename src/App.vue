<script setup>
import Header from "@/components/layouts/Header.vue";
import { useRoute } from "vue-router";
import { useThemeStore } from "@/stores/theme";
import { onMounted } from "vue";

const route = useRoute();
const themeStore = useThemeStore();

onMounted(() => {
  themeStore.initTheme();
});
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

:root {
  --bg-color: #fff;
  --text-color: #1e293b;
}

[data-bs-theme="dark"] {
  --bg-color: #0f172a;
  --text-color: #f8fafc;
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
  color: var(--text-color);
  background: var(--bg-color);
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

/* Global Dark Mode Overrides for Portfolio Components */
[data-bs-theme="dark"] .hero,
[data-bs-theme="dark"] .projects,
[data-bs-theme="dark"] .services,
[data-bs-theme="dark"] .contact,
[data-bs-theme="dark"] .about-hero,
[data-bs-theme="dark"] .skills,
[data-bs-theme="dark"] .timeline-section,
[data-bs-theme="dark"] .detail-page {
  background: var(--bg-color) !important;
}

[data-bs-theme="dark"] .services,
[data-bs-theme="dark"] .contact,
[data-bs-theme="dark"] .profile {
  background: #0f172a !important; 
}

[data-bs-theme="dark"] .card,
[data-bs-theme="dark"] .code-card,
[data-bs-theme="dark"] .float-card,
[data-bs-theme="dark"] .bg-white,
[data-bs-theme="dark"] .info-card,
[data-bs-theme="dark"] .contact-form,
[data-bs-theme="dark"] .project-detail,
[data-bs-theme="dark"] .profile-card,
[data-bs-theme="dark"] .skill-item,
[data-bs-theme="dark"] .skill-icon,
[data-bs-theme="dark"] .timeline-col {
  background: #1e293b !important;
  border-color: #334155 !important;
}

[data-bs-theme="dark"] .hero-name,
[data-bs-theme="dark"] .section-title,
[data-bs-theme="dark"] .card-title,
[data-bs-theme="dark"] .card h3,
[data-bs-theme="dark"] .text-dark,
[data-bs-theme="dark"] h1,
[data-bs-theme="dark"] h2,
[data-bs-theme="dark"] h3,
[data-bs-theme="dark"] .info-item h4,
[data-bs-theme="dark"] .about-heading,
[data-bs-theme="dark"] .info-val,
[data-bs-theme="dark"] .skill-name,
[data-bs-theme="dark"] .timeline-title,
[data-bs-theme="dark"] .timeline-content h4 {
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .hero-role,
[data-bs-theme="dark"] .hero-desc,
[data-bs-theme="dark"] .card-desc,
[data-bs-theme="dark"] .section-desc,
[data-bs-theme="dark"] .card p,
[data-bs-theme="dark"] p,
[data-bs-theme="dark"] .info-item p,
[data-bs-theme="dark"] .about-sub,
[data-bs-theme="dark"] .bio,
[data-bs-theme="dark"] .info-label,
[data-bs-theme="dark"] .timeline-desc {
  color: #94a3b8 !important;
}

[data-bs-theme="dark"] .hero-badge,
[data-bs-theme="dark"] .btn-outline,
[data-bs-theme="dark"] .filter-btn {
  background: #1e293b !important;
  color: #cbd5e1 !important;
  border-color: #334155 !important;
}

[data-bs-theme="dark"] .stack-tag {
  background: #1e293b !important;
  border-color: #334155 !important;
}

[data-bs-theme="dark"] .form-group input,
[data-bs-theme="dark"] .form-group textarea {
  background: #0f172a !important;
  border-color: #334155 !important;
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .form-group input:focus,
[data-bs-theme="dark"] .form-group textarea:focus {
  border-color: #6366f1 !important;
}

[data-bs-theme="dark"] .filter-btn.active {
  background: #6366f1 !important;
  color: #fff !important;
  border-color: transparent !important;
}

[data-bs-theme="dark"] .card-action {
  background: #1e293b !important;
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .card-action:hover {
  background: #6366f1 !important;
  color: #fff !important;
}

[data-bs-theme="dark"] .footer {
  background: #0b1120 !important;
  border-top-color: #1e293b !important;
}

[data-bs-theme="dark"] .info-item:hover {
  background: #334155 !important;
}

[data-bs-theme="dark"] .skill-item:hover {
  border-color: #6366f1 !important;
}

[data-bs-theme="dark"] .timeline-wrap {
  border-left-color: #334155 !important;
}

[data-bs-theme="dark"] .timeline-dot {
  border-color: #1e293b !important;
}
</style>
