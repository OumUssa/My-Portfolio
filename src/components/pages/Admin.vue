<template>
  <div class="admin-shell">
    <aside class="sidebar">
      <div class="sidebar-top">
        <div class="brand">
          <div class="brand-mark">A</div>
          <router-link to="/" class="brand-name">
            <div>
              <h1>Admin</h1>
              <p>Portfolio</p>
            </div>
          </router-link>
        </div>

        <nav class="menu">
          <button
            v-for="item in menuItems"
            :key="item.key"
            class="menu-item"
            :class="{ active: activeSection === item.key }"
            @click="activeSection = item.key">
            <span>{{ item.label }}</span>
          </button>
        </nav>
      </div>

      <div class="sidebar-footer">
        <button class="logout-btn" @click="logout">Log out</button>
      </div>
    </aside>

    <main class="workspace">
      <section class="hero-panel">
        <div>
          <p class="eyebrow">Portfolio Control</p>
          <h2>Welcome back, {{ user?.name || "Admin" }}</h2>
          <p class="subtitle">
            Manage your live portfolio content. Updates persist instantly and sync with your public views.
          </p>
        </div>

        <div class="hero-stat">
          <span class="stat-label">Dashboard</span>
          <strong>{{ projects.length }} Projects</strong>
          <small>{{ categories.length }} Tech Stacks</small>
        </div>
      </section>

      <p v-if="loadError" class="error-banner">{{ loadError }}</p>

      <Dashboard
        v-if="activeSection === 'dashboard'"
        :projects="projects"
        :categories="categories"
      />

      <CreateProject
        v-if="activeSection === 'projects'"
        :projects="projects"
        :categories="categories"
        :token="token"
        @update:projects="projects = $event"
      />

      <CreateTechStack
        v-if="activeSection === 'categories'"
        :categories="categories"
        :projects="projects"
        :token="token"
        @update:categories="categories = $event"
        @update:projects="projects = $event"
      />
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { fetchProjects } from "@/data/projectsApi.js";
import { fetchCategories } from "@/data/categoriesApi.js";
import { buildCategoryList, toAdminProject } from "@/data/adminContent.js";

import Dashboard from "@/components/pages/Admin/Dashboard.vue";
import CreateProject from "@/components/pages/Admin/CreateProject.vue";
import CreateTechStack from "@/components/pages/Admin/CreateTechStack.vue";

const router = useRouter();
const auth = useAuthStore();
const { user, token } = storeToRefs(auth);

const menuItems = [
  { key: "dashboard", label: "Dashboard" },
  { key: "projects", label: "Projects" },
  { key: "categories", label: "Tech Stacks" },
];

const activeSection = ref("dashboard");
const projects = ref([]);
const categories = ref([]);
const loading = ref(true);
const loadError = ref("");

async function loadDashboardData() {
  loading.value = true;
  loadError.value = "";

  try {
    const [apiProjects, apiCategories] = await Promise.all([
      fetchProjects(),
      fetchCategories(),
    ]);

    projects.value = apiProjects.map(toAdminProject);
    categories.value = buildCategoryList(
      projects.value,
      apiCategories || [],
      [],
    );
  } catch (error) {
    loadError.value =
      error instanceof Error ? error.message : "Failed to load dashboard data.";
  } finally {
    loading.value = false;
  }
}

function logout() {
  auth.logout();
  router.push({ path: "/login" });
}

onMounted(loadDashboardData);
</script>

<style scoped>
.admin-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr);
  background: #f1f5f9; /* Slate 100 for better contrast */
  color: #1e293b;
  font-family: inherit;
}

.sidebar {
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  background: #0f172a;
  color: #f8fafc;
  box-shadow: 4px 0 24px rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  height: 100vh;
}

.sidebar-top {
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-mark {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
}

.brand h1 {
  margin: 0;
  font-size: 18px;
  font-weight: 800;
  color: #f8fafc;
}

.brand p {
  margin: 2px 0 0;
  color: #94a3b8;
  font-size: 11px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.menu {
  display: grid;
  gap: 6px;
}

.menu-item {
  width: 100%;
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid transparent;
  background: transparent;
  color: #94a3b8;
  text-align: left;
  font-size: 14px;
  font-weight: 600;
  transition:
    background 0.2s ease,
    transform 0.2s ease,
    color 0.2s ease;
  cursor: pointer;
}

.menu-item:hover,
.menu-item.active {
  background: #1e293b;
  color: #fff;
  border-color: #334155;
  transform: translateX(3px);
}

.menu-item.active {
  border-left: 3px solid #6366f1;
  border-radius: 10px;
}

.sidebar-footer {
  display: grid;
  margin-top: auto; /* Pushes the footer to the bottom */
  padding-top: 20px;
}

.logout-btn {
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid #334155;
  background: transparent;
  color: #cbd5e1;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.2s ease;
  cursor: pointer;
}

.logout-btn:hover {
  background: #7f1d1d;
  color: #fecaca;
  border-color: #991b1b;
}

.workspace {
  padding: 24px;
  display: grid;
  gap: 20px;
  align-content: start;
}

.hero-panel {
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  border-radius: 16px;
  background: #fff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}

.eyebrow {
  margin: 0 0 6px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-size: 10px;
  color: #6366f1;
  font-weight: 700;
}

.hero-panel h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 800;
  color: #1e293b;
  letter-spacing: -0.5px;
}

.subtitle {
  margin: 6px 0 0;
  max-width: 600px;
  font-size: 14px;
  color: #64748b;
  line-height: 1.5;
}

.hero-stat {
  min-width: 150px;
  padding: 16px;
  border-radius: 14px;
  background: linear-gradient(135deg, #f8fafc, #f1f5f9);
  border: 1px solid #e2e8f0;
}

.stat-label {
  display: block;
  margin-bottom: 4px;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6366f1;
  font-weight: 700;
}

.hero-stat strong {
  display: block;
  font-size: 24px;
  font-weight: 800;
  color: #1e293b;
}

.hero-stat small {
  font-size: 12px;
  color: #64748b;
  font-weight: 500;
}

.error-banner {
  margin: 1rem 0;
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid #fca5a5;
  background: #fef2f2;
  color: #991b1b;
  font-size: 14px;
  font-weight: 600;
}

@media (max-width: 1100px) {
  .admin-shell {
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    height: auto;
    position: static;
    gap: 16px;
    padding: 16px;
  }

  .sidebar-top {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }

  .menu {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    flex: 1;
    justify-content: flex-end;
  }

  .menu-item {
    width: auto;
    padding: 8px 12px;
  }

  .menu-item:hover,
  .menu-item.active {
    transform: translateY(-2px) translateX(0);
  }

  .menu-item.active {
    border-left: none;
    border-bottom: 3px solid #6366f1;
  }

  .sidebar-footer {
    margin-top: 0;
    padding-top: 0;
  }
}

@media (max-width: 900px) {
  .hero-panel {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
