<template>
  <section id="projects" class="projects">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">My Work</span>
        <h2 class="section-title">Recent Projects</h2>
      </div>

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

      <div class="grid">
        <transition-group name="fade">
          <div
            v-for="project in filteredProjects"
            :key="project.title"
            class="card">
            <div
              class="card-thumb"
              :style="{
                backgroundImage: project.image
                  ? 'url(' + project.image + ')'
                  : 'linear-gradient(135deg, ' + project.color + ', ' + project.color + ')',
              }">
              <div class="card-overlay">
                <a :href="project.liveLink" target="_blank" rel="noopener noreferrer" class="card-action">
                  <i class="bi bi-eye"></i>
                </a>
                <a :href="project.githubLink" target="_blank" rel="noopener noreferrer" class="card-action">
                  <i class="bi bi-github"></i>
                </a>
              </div>
            </div>
            <div class="card-body">
              <div class="card-tags">
                <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
              <h3 class="card-title">{{ project.title }}</h3>
              <p class="card-desc">{{ project.desc }}</p>
            </div>
          </div>
        </transition-group>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from "vue";
import worksyncImage from "@/assets/Worksync.png";
import E_examImage from "@/assets/image.png";

const tabs = ["All", "Web App", "Landing Page", "Dashboard"];
const activeTab = ref("All");

const projects = [
  {
    title: "WorkSync",
    desc: "A freelance marketplace for seamless collaboration between clients and freelancers.",
    tags: ["Vue.js", "HTML5", "CSS3", "API", "JavaScript"],
    category: "Web App",
    color: "#6366f1",
    image: worksyncImage,
    liveLink: "https://worksync-eta.vercel.app/",
    githubLink: "https://github.com/horsenghab/freelancer-ant-g2",
  },
  {
    title: "Portfolio Website",
    desc: "A clean, responsive personal portfolio with smooth animations.",
    tags: ["Vue.js", "CSS3"],
    category: "Landing Page",
    color: "#ec4899",
    image: E_examImage,
    liveLink: "https://curious-rabanadas-de9ea1.netlify.app/",
    githubLink: "https://github.com/V-Sopanha/G13-ANT-e-ExamCam",
  },
  {
    title: "Task Management App",
    desc: "A productivity tool with drag-and-drop, real-time updates, and team collaboration.",
    tags: ["Vue.js", "Firebase"],
    category: "Web App",
    color: "#0ea5e9",
    image: "https://via.placeholder.com/400x300?text=Task+App",
    liveLink: "https://task-management-app.com/",
    githubLink: "https://github.com/yourname/task-app",
  },
  {
    title: "Analytics Dashboard",
    desc: "A data visualization dashboard with charts, filters, and export features.",
    tags: ["Vue.js", "Chart.js"],
    category: "Dashboard",
    color: "#10b981",
    image: "https://via.placeholder.com/400x300?text=Analytics",
    liveLink: "https://analytics-dashboard.com/",
    githubLink: "https://github.com/yourname/analytics-dashboard",
  },
  {
    title: "Restaurant Landing Page",
    desc: "A beautiful restaurant site with menu, reservations, and gallery.",
    tags: ["HTML", "CSS", "JavaScript"],
    category: "Landing Page",
    color: "#f43f5e",
    image: "https://via.placeholder.com/400x300?text=Restaurant",
    liveLink: "https://restaurant-landing.com/",
    githubLink: "https://github.com/yourname/restaurant-site",
  },
  {
    title: "Admin Panel",
    desc: "A feature-rich admin dashboard with user management and analytics.",
    tags: ["Vue.js", "Tailwind"],
    category: "Dashboard",
    color: "#a78bfa",
    image: "https://via.placeholder.com/400x300?text=Admin+Panel",
    liveLink: "https://admin-panel-demo.com/",
    githubLink: "https://github.com/yourname/admin-panel",
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

.fade-enter-active { transition: all 0.3s ease; }
.fade-leave-active { transition: all 0.2s ease; position: absolute; }
.fade-enter-from { opacity: 0; transform: translateY(12px); }
.fade-leave-to { opacity: 0; }

@media (max-width: 992px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
  .projects { padding: 4rem 1.5rem; }
  .grid { grid-template-columns: 1fr; }
  .section-title { font-size: 1.8rem; }
}
</style>
