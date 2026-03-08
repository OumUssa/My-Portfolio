<template>
  <section id="projects" class="projects">
    <div class="container">
      <div class="section-header">
        <span class="label">My Work</span>
        <h2 class="section-title">Recent Projects</h2>
        <div class="title-line"></div>
      </div>

      <!-- Filter Tabs -->
      <div class="filter-tabs">
        <button
          v-for="tab in tabs"
          :key="tab"
          class="filter-btn"
          :class="{ active: activeTab === tab }"
          @click="activeTab = tab">
          {{ tab }}
        </button>
      </div>

      <!-- Projects Grid -->
      <div class="projects-grid">
        <transition-group name="project">
          <div
            v-for="project in filteredProjects"
            :key="project.title"
            class="project-card">
            <div class="project-thumb" :style="{ background: project.color }">
              <div class="thumb-overlay">
                <a href="#" class="thumb-btn"><i class="bi bi-eye"></i></a>
                <a href="#" class="thumb-btn"><i class="bi bi-github"></i></a>
              </div>
              <i :class="project.icon" class="thumb-icon"></i>
            </div>
            <div class="project-info">
              <div class="project-tags">
                <span v-for="tag in project.tags" :key="tag" class="tag">{{
                  tag
                }}</span>
              </div>
              <h3>{{ project.title }}</h3>
              <p>{{ project.desc }}</p>
            </div>
          </div>
        </transition-group>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from "vue";

const tabs = ["All", "Web App", "Landing Page", "Dashboard"];
const activeTab = ref("All");

const projects = [
  {
    title: "E-Commerce Platform",
    desc: "A full-stack online store with cart, checkout, and payment integration.",
    tags: ["Vue.js", "Node.js", "MongoDB"],
    category: "Web App",
    icon: "bi bi-cart3",
    color: "#6366f1",
  },
  {
    title: "Portfolio Website",
    desc: "A clean, responsive personal portfolio with smooth animations.",
    tags: ["Vue.js", "CSS3"],
    category: "Landing Page",
    icon: "bi bi-person-badge",
    color: "#ec4899",
  },
  {
    title: "Task Management App",
    desc: "A productivity tool with drag-and-drop, real-time updates, and team collaboration.",
    tags: ["Vue.js", "Firebase"],
    category: "Web App",
    icon: "bi bi-kanban",
    color: "#0ea5e9",
  },
  {
    title: "Analytics Dashboard",
    desc: "A data visualization dashboard with charts, filters, and export features.",
    tags: ["Vue.js", "Chart.js"],
    category: "Dashboard",
    icon: "bi bi-bar-chart-line",
    color: "#10b981",
  },
  {
    title: "Restaurant Landing Page",
    desc: "A beautiful restaurant site with menu, reservations, and gallery.",
    tags: ["HTML", "CSS", "JavaScript"],
    category: "Landing Page",
    icon: "bi bi-shop",
    color: "#f43f5e",
  },
  {
    title: "Admin Panel",
    desc: "A feature-rich admin dashboard with user management and analytics.",
    tags: ["Vue.js", "Tailwind"],
    category: "Dashboard",
    icon: "bi bi-speedometer2",
    color: "#a78bfa",
  },
];

const filteredProjects = computed(() => {
  if (activeTab.value === "All") return projects;
  return projects.filter((p) => p.category === activeTab.value);
});
</script>

<style scoped>
.projects {
  padding: 6rem 2rem;
  background: #fff;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #6366f1;
  display: block;
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 1rem;
}

.title-line {
  width: 60px;
  height: 4px;
  background: #6366f1;
  border-radius: 2px;
  margin: 0 auto;
}

/* ── Filter Tabs ── */
.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 3rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.5rem 1.4rem;
  border: 1.5px solid #e2e8f0;
  border-radius: 50px;
  background: transparent;
  color: #64748b;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn:hover {
  border-color: #c7d2fe;
  color: #6366f1;
}

.filter-btn.active {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
}

/* ── Projects Grid ── */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.project-card {
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.35s ease;
  background: #fff;
}

.project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.08);
  border-color: #c7d2fe;
}

.project-thumb {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.thumb-icon {
  font-size: 3rem;
  color: rgba(255, 255, 255, 0.4);
  transition: all 0.35s ease;
}

.project-card:hover .thumb-icon {
  transform: scale(1.2);
  color: rgba(255, 255, 255, 0.2);
}

.thumb-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  opacity: 0;
  transition: opacity 0.35s ease;
}

.project-card:hover .thumb-overlay {
  opacity: 1;
}

.thumb-btn {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 50%;
  color: #1e293b;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  text-decoration: none;
  transform: translateY(10px);
}

.project-card:hover .thumb-btn {
  transform: translateY(0);
}

.thumb-btn:hover {
  background: #6366f1;
  color: #fff;
}

.project-info {
  padding: 1.2rem 1.5rem 1.5rem;
}

.project-tags {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin-bottom: 0.6rem;
}

.tag {
  font-size: 0.7rem;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.08);
  padding: 0.2rem 0.6rem;
  border-radius: 50px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.project-info h3 {
  font-size: 1.05rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.4rem;
}

.project-info p {
  font-size: 0.85rem;
  color: #64748b;
  line-height: 1.5;
  margin: 0;
}

/* ── Transition ── */
.project-enter-active {
  transition: all 0.4s ease;
}

.project-leave-active {
  transition: all 0.3s ease;
  position: absolute;
}

.project-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.project-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* ── Responsive ── */
@media (max-width: 992px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .projects {
    padding: 4rem 1.5rem;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 2rem;
  }

  .project-thumb {
    height: 160px;
  }
}
</style>
