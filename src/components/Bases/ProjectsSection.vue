<template>
  <section id="projects" class="projects">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">My Work</span>
        <h2 class="section-title">Recent Projects</h2>
        <p v-if="isFallback && !loading" class="fallback-note">
          <i class="bi bi-cloud-slash"></i> Showing example projects — live data is temporarily unavailable.
        </p>
      </div>

      <div v-if="!loading" class="controls-bar" v-reveal>
        <div class="filter-bar">
          <button
            v-for="tab in tabs"
            :key="tab"
            class="filter-btn"
            :class="{ active: activeTab === tab }"
            @click="activeTab = tab">
            {{ tab }}
          </button>
        </div>

        <div class="search-field">
          <i class="bi bi-search"></i>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search projects..."
            aria-label="Search projects" />
          <button
            v-if="searchQuery"
            type="button"
            class="search-clear"
            aria-label="Clear search"
            @click="searchQuery = ''">
            <i class="bi bi-x"></i>
          </button>
        </div>
      </div>

      <div class="grid">
        <template v-if="loading">
          <div v-for="n in 6" :key="`skeleton-${n}`" class="card skeleton-card">
            <div class="card-thumb skeleton-block"></div>
            <div class="card-body">
              <div class="card-tags">
                <span class="skeleton-block skeleton-tag"></span>
                <span class="skeleton-block skeleton-tag"></span>
              </div>
              <div class="skeleton-block skeleton-line skeleton-title"></div>
              <div class="skeleton-block skeleton-line"></div>
              <div class="skeleton-block skeleton-line short"></div>
              <div class="card-footer-action">
                <span class="skeleton-block skeleton-btn"></span>
              </div>
            </div>
          </div>
        </template>

        <transition-group v-else-if="filteredProjects.length" name="fade">
          <div
            v-for="(project, index) in filteredProjects"
            :key="project.id"
            class="card"
            v-reveal
            :style="{ transitionDelay: (index % 3) * 90 + 'ms' }">
            <div
              class="card-thumb"
              :style="{
                backgroundImage: project.image
                  ? `url('${project.image}')`
                  : `linear-gradient(135deg, ${project.color || '#e2e8f0'}, ${project.color || '#cbd5e1'})`,
              }">
              <div class="card-overlay">
                <router-link :to="`/detail/${project.id}`" class="card-action">
                  <i class="bi bi-eye"></i>
                </router-link>
                <a
                  v-if="project.githubLink"
                  :href="project.githubLink"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="card-action">
                  <i class="bi bi-github"></i>
                </a>
              </div>
            </div>
            <div class="card-body">
              <div class="card-tags">
                <span v-for="tag in project.tags" :key="tag" class="tag">{{
                  tag
                }}</span>
              </div>
              <h3 class="card-title">{{ project.title }}</h3>
              <p class="card-desc">{{ project.desc }}</p>
              <div class="card-footer-action">
                <router-link :to="`/detail/${project.id}`" class="card-btn">
                  View Project <i class="bi bi-arrow-right"></i>
                </router-link>
              </div>
            </div>
          </div>
        </transition-group>

        <div v-else class="state-copy state-empty">
          {{
            searchQuery
              ? `No projects match "${searchQuery}".`
              : "No projects found."
          }}
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { fetchProjectsSafe } from "@/data/projectsApi.js";

const projects = ref([]);
const loading = ref(true);
const isFallback = ref(false);
const activeTab = ref("All");
const searchQuery = ref("");

const tabs = computed(() => {
  const categories = new Set();

  projects.value.forEach((project) => {
    project.categories.forEach((category) => categories.add(category));
  });

  return ["All", ...categories];
});

const filteredProjects = computed(() => {
  let result = projects.value;

  if (activeTab.value !== "All") {
    result = result.filter((project) =>
      project.categories.includes(activeTab.value),
    );
  }

  const query = searchQuery.value.trim().toLowerCase();
  if (query) {
    result = result.filter(
      (project) =>
        project.title.toLowerCase().includes(query) ||
        project.desc.toLowerCase().includes(query) ||
        project.tags.some((tag) => tag.toLowerCase().includes(query)),
    );
  }

  return result;
});

async function loadProjects() {
  loading.value = true;

  const { projects: data, isFallback: fallback } = await fetchProjectsSafe();
  projects.value = data;
  isFallback.value = fallback;
  loading.value = false;
}

onMounted(loadProjects);
</script>

<style scoped>
.projects {
  padding: 6rem 2rem;
  background: #fff;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-head {
  text-align: center;
  margin-bottom: 2.5rem;
}

.section-tag {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #6366f1;
}

.section-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #1e293b;
  margin-top: 0.35rem;
}

.controls-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.filter-bar {
  display: flex;
  justify-content: center;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.search-field {
  position: relative;
  display: flex;
  align-items: center;
  width: 240px;
}

.search-field i.bi-search {
  position: absolute;
  left: 0.85rem;
  font-size: 0.85rem;
  color: #94a3b8;
  pointer-events: none;
}

.search-field input {
  width: 100%;
  padding: 0.5rem 2rem 0.5rem 2.1rem;
  border: 1px solid #e2e8f0;
  border-radius: 100px;
  font-size: 0.82rem;
  color: #1e293b;
  background: #f8fafc;
  outline: none;
  transition: all 0.2s ease;
}

.search-field input::placeholder {
  color: #94a3b8;
}

.search-field input:focus {
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.08);
}

.search-clear {
  position: absolute;
  right: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border: none;
  border-radius: 50%;
  background: transparent;
  color: #94a3b8;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.search-clear:hover {
  background: #e2e8f0;
  color: #475569;
}

.state-copy {
  text-align: center;
  color: #64748b;
  margin-bottom: 2rem;
}

.state-error {
  color: #b91c1c;
}

.skeleton-card {
  pointer-events: none;
}

.skeleton-card:hover {
  transform: none;
  box-shadow: none;
  border-color: #f1f5f9;
}

.skeleton-block {
  position: relative;
  overflow: hidden;
  background: #eef2f7;
  border-radius: 4px;
}

.skeleton-block::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.65),
    transparent
  );
  animation: skeleton-shimmer 1.4s infinite;
}

@keyframes skeleton-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.skeleton-card .card-thumb {
  border-radius: 0;
}

.skeleton-tag {
  width: 56px;
  height: 18px;
  border-radius: 4px;
}

.skeleton-line {
  height: 12px;
  margin-bottom: 0.6rem;
}

.skeleton-title {
  height: 18px;
  width: 70%;
  margin-bottom: 0.85rem;
}

.skeleton-line.short {
  width: 55%;
  margin-bottom: 0;
}

.skeleton-btn {
  width: 130px;
  height: 34px;
  border-radius: 6px;
  display: inline-block;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton-block::after {
    animation: none;
  }
}

.fallback-note {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.75rem;
  padding: 0.35rem 0.85rem;
  font-size: 0.78rem;
  font-weight: 500;
  color: #92400e;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 100px;
}

.state-empty {
  grid-column: 1 / -1;
  padding: 2rem 1rem;
}

.filter-btn {
  padding: 0.45rem 1.1rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  background: transparent;
  color: #64748b;
  font-size: 0.82rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  border-color: #c7d2fe;
  color: #6366f1;
}

.filter-btn.active {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.card {
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(99, 102, 241, 0.12);
  border-color: #c7d2fe;
}

.card-thumb {
  height: 190px;
  position: relative;
  overflow: hidden;
  background-size: cover;
  background-position: center;
}

.card-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  opacity: 0;
  transition: opacity 0.25s ease;
}

.card:hover .card-overlay {
  opacity: 1;
}

.card-action {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 50%;
  color: #1e293b;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.card-action:hover {
  background: #6366f1;
  color: #fff;
}

.card-body {
  padding: 1.15rem 1.25rem 1.35rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.card-tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.tag {
  font-size: 0.65rem;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.06);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.card-title {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.35rem;
}

.card-desc {
  font-size: 0.83rem;
  color: #64748b;
  line-height: 1.5;
  margin: 0;
}

.card-footer-action {
  margin-top: auto;
  padding-top: 1.25rem;
}

.card-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 1rem;
  background: rgba(99, 102, 241, 0.08);
  color: #6366f1;
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: 6px;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 1px solid rgba(99, 102, 241, 0.15);
}

.card-btn:hover {
  background: rgba(99, 102, 241, 0.15);
  transform: translateY(-1px);
}

/* Limit description to 3 lines with an ellipsis */
.card-desc {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.fade-enter-active {
  transition: all 0.3s ease;
}
.fade-leave-active {
  transition: all 0.2s ease;
  position: absolute;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(12px);
}
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 992px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .projects {
    padding: 4rem 1.5rem;
  }
  .grid {
    grid-template-columns: 1fr;
  }
  .section-title {
    font-size: 1.8rem;
  }
}
</style>
