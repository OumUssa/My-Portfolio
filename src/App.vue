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
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" :key="route.fullPath" />
        </transition>
      </router-view>
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

/* Route-switch transition */
.page-enter-active,
.page-leave-active {
  transition:
    opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1),
    transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.page-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}

@media (prefers-reduced-motion: reduce) {
  .page-enter-active,
  .page-leave-active {
    transition: none;
  }
}

/* Scroll-reveal animation (see src/directives/reveal.js) */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition:
    opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
    transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-visible {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }
}

/* Shared section-tag / section-title accent, used across every page section */
.section-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
}

.section-tag::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.12);
}

.section-head .section-title::after {
  content: "";
  display: block;
  width: 44px;
  height: 4px;
  margin: 0.85rem auto 0;
  border-radius: 4px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
}

/* Global Dark Mode Overrides for Portfolio Components */
[data-bs-theme="dark"] .hero,
[data-bs-theme="dark"] .projects,
[data-bs-theme="dark"] .services,
[data-bs-theme="dark"] .achievements,
[data-bs-theme="dark"] .certificates,
[data-bs-theme="dark"] .contact,
[data-bs-theme="dark"] .about-hero,
[data-bs-theme="dark"] .skills,
[data-bs-theme="dark"] .timeline-section,
[data-bs-theme="dark"] .detail-page,
[data-bs-theme="dark"] .detail-section {
  background: var(--bg-color) !important;
}

[data-bs-theme="dark"] .services,
[data-bs-theme="dark"] .contact,
[data-bs-theme="dark"] .profile {
  background: #0f172a !important; 
}

[data-bs-theme="dark"] .card,
[data-bs-theme="dark"] .course-card,
[data-bs-theme="dark"] .scholarship-meta,
[data-bs-theme="dark"] .code-card,
[data-bs-theme="dark"] .float-card,
[data-bs-theme="dark"] .bg-white,
[data-bs-theme="dark"] .info-card,
[data-bs-theme="dark"] .contact-form,
[data-bs-theme="dark"] .project-detail,
[data-bs-theme="dark"] .profile-card,
[data-bs-theme="dark"] .skill-item,
[data-bs-theme="dark"] .skill-icon,
[data-bs-theme="dark"] .timeline-col,
[data-bs-theme="dark"] .project-info,
[data-bs-theme="dark"] .meta-card,
[data-bs-theme="dark"] .media-frame {
  background: #1e293b !important;
  border-color: #334155 !important;
}

[data-bs-theme="dark"] .hero-name,
[data-bs-theme="dark"] .section-title,
[data-bs-theme="dark"] .card-title,
[data-bs-theme="dark"] .card h3,
[data-bs-theme="dark"] .course-card h4,
[data-bs-theme="dark"] .text-dark,
[data-bs-theme="dark"] h1,
[data-bs-theme="dark"] h2,
[data-bs-theme="dark"] h3,
[data-bs-theme="dark"] .info-item h4,
[data-bs-theme="dark"] .about-heading,
[data-bs-theme="dark"] .info-val,
[data-bs-theme="dark"] .skill-name,
[data-bs-theme="dark"] .timeline-title,
[data-bs-theme="dark"] .timeline-content h4,
[data-bs-theme="dark"] .project-title,
[data-bs-theme="dark"] .meta-value {
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
[data-bs-theme="dark"] .timeline-desc,
[data-bs-theme="dark"] .project-desc,
[data-bs-theme="dark"] .meta-label,
[data-bs-theme="dark"] .meta-item {
  color: #94a3b8 !important;
}

[data-bs-theme="dark"] .hero-badge,
[data-bs-theme="dark"] .btn-outline,
[data-bs-theme="dark"] .filter-btn,
[data-bs-theme="dark"] .github-link {
  background: #1e293b !important;
  color: #cbd5e1 !important;
  border-color: #334155 !important;
}

[data-bs-theme="dark"] .github-link:hover {
  background: #334155 !important;
  border-color: #475569 !important;
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .stack-tag,
[data-bs-theme="dark"] .custom-tag,
[data-bs-theme="dark"] .admin-avatar {
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

[data-bs-theme="dark"] .search-field input {
  background: #1e293b !important;
  border-color: #334155 !important;
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .search-field input::placeholder {
  color: #64748b !important;
}

[data-bs-theme="dark"] .search-clear:hover {
  background: #334155 !important;
  color: #f8fafc !important;
}

[data-bs-theme="dark"] .skeleton-block {
  background: #334155 !important;
}

[data-bs-theme="dark"] .skeleton-block::after {
  background: linear-gradient(
    90deg,
    transparent,
    rgba(148, 163, 184, 0.25),
    transparent
  ) !important;
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

[data-bs-theme="dark"] .note-card {
  background: rgba(249, 115, 22, 0.1) !important;
  border-color: rgba(249, 115, 22, 0.2) !important;
}

[data-bs-theme="dark"] .note-card p {
  color: #fdba74 !important;
}

/* Header dark-mode overrides (moved here from Header.vue's scoped style,
   which couldn't express :global(sel) + descendant reliably) */
[data-bs-theme="dark"] .navbar {
  background: transparent;
  border-bottom-color: transparent;
}
[data-bs-theme="dark"] .navbar.scrolled {
  background: rgba(15, 23, 42, 0.95);
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(255, 255, 255, 0.08);
}
[data-bs-theme="dark"] .logo {
  color: #f8fafc;
}
[data-bs-theme="dark"] .nav-link {
  color: #94a3b8;
}
[data-bs-theme="dark"] .nav-link:hover {
  color: #f8fafc;
  background: rgba(99, 102, 241, 0.15);
}
[data-bs-theme="dark"] .nav-link.active {
  background: rgba(99, 102, 241, 0.2);
}
[data-bs-theme="dark"] .menu-toggle span {
  background: #f8fafc;
}
@media (max-width: 768px) {
  [data-bs-theme="dark"] .nav-links {
    background: #0f172a;
    box-shadow: -10px 0 30px rgba(0, 0, 0, 0.5);
  }
}
</style>
