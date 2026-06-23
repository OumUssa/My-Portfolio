<template>
  <section id="projects" class="projects">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">My Work</span>
        <h2 class="section-title">Recent Projects</h2>
      </div>

      <div v-if="loading" class="state-copy">Loading projects...</div>
      <div v-else-if="error" class="state-copy state-error">
        {{ error }}
      </div>

      <div v-else class="filter-bar">
        <button
          v-for="tab in tabs"
          :key="tab"
          class="filter-btn"
          :class="{ active: activeTab === tab }"
          @click="activeTab = tab">
          {{ tab }}
        </button>
      </div>

      <div class="grid">
        <transition-group
          v-if="!loading && !error && filteredProjects.length"
          name="fade">
          <div
            v-for="project in filteredProjects"
            :key="project.id"
            class="card">
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

        <div v-else-if="!loading && !error" class="state-copy state-empty">
          No projects found.
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { fetchProjects } from "@/data/projectsApi.js";

const projects = ref([]);
const loading = ref(true);
const error = ref("");
const activeTab = ref("All");

const tabs = computed(() => {
  const categories = new Set();

  projects.value.forEach((project) => {
    project.categories.forEach((category) => categories.add(category));
  });

  return ["All", ...categories];
});

const filteredProjects = computed(() => {
  if (activeTab.value === "All") {
    return projects.value;
  }

  return projects.value.filter((project) =>
    project.categories.includes(activeTab.value),
  );
});

async function loadProjects() {
  loading.value = true;
  error.value = "";

  try {
    projects.value = await fetchProjects();
  } catch (fetchError) {
    error.value =
      fetchError instanceof Error
        ? fetchError.message
        : "Failed to load projects.";
  } finally {
    loading.value = false;
  }
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

.filter-bar {
  display: flex;
  justify-content: center;
  gap: 0.4rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.state-copy {
  text-align: center;
  color: #64748b;
  margin-bottom: 2rem;
}

.state-error {
  color: #b91c1c;
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
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
  border-color: #e2e8f0;
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
