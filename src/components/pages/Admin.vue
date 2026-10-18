<template>
  <div class="admin-shell">
    <aside class="sidebar">
      <div class="sidebar-top">
        <div class="brand">
          <div class="brand-mark">A</div>
          <router-link to="/" class="brand-name">
            <div>
              <h1>OumUssa</h1>
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
            <i class="bi" :class="item.icon"></i>
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

      <transition name="section" mode="out-in">
        <div :key="activeSection" class="section-wrap">
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

      <ContactManagement
        v-if="activeSection === 'contact'"
        :token="token"
      />

      <div v-if="activeSection === 'profile'" class="panel" style="padding: 40px; text-align: center; color: #64748b; background: #fff; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <i class="bi bi-person-badge" style="font-size: 48px; margin-bottom: 16px; display: block; color: #cbd5e1;"></i>
        <h3 style="margin: 0 0 8px; color: #1e293b; font-size: 20px;">Admin Profile</h3>
        <p style="margin: 0;">This feature will be available soon.</p>
      </div>
        </div>
      </transition>
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
import { useToastStore } from "@/stores/toast";

import Dashboard from "@/components/pages/Admin/Dashboard.vue";
import CreateProject from "@/components/pages/Admin/CreateProject.vue";
import CreateTechStack from "@/components/pages/Admin/CreateTechStack.vue";
import ContactManagement from "@/components/pages/Admin/ContactManagement.vue";

const router = useRouter();
const auth = useAuthStore();
const toast = useToastStore();
const { user, token } = storeToRefs(auth);

const menuItems = [
  { key: "dashboard", label: "Dashboard", icon: "bi-grid-1x2-fill" },
  { key: "projects", label: "Projects", icon: "bi-folder-fill" },
  { key: "categories", label: "Tech Stacks", icon: "bi-layers-fill" },
  { key: "contact", label: "Contact", icon: "bi-chat-left-dots-fill" },
  { key: "profile", label: "Profile", icon: "bi-person-circle" },
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
    toast.error(loadError.value);
  } finally {
    loading.value = false;
  }
}

function logout() {
  auth.logout();
  toast.success("You have been logged out.");
  router.push({ path: "/login" });
}

onMounted(loadDashboardData);
</script>

<style>
[data-bs-theme="dark"] .admin-shell .dash {
  --d-text: #f1f5f9; --d-muted: #94a3b8; --d-faint: #64748b;
  --d-card: #1e293b; --d-border: #334155; --d-line: #2b3a52; --d-icon-bg: rgba(99, 102, 241, 0.18);
}

/* Admin dark mode — App.vue's global dark rules force colors with !important, so these match that. */
[data-bs-theme="dark"] .admin-shell { background: #0b1220 !important; color: #e2e8f0; }
[data-bs-theme="dark"] .admin-shell .sidebar { background: #060b16; box-shadow: 4px 0 24px rgba(0, 0, 0, 0.4); }

[data-bs-theme="dark"] .admin-shell .panel,
[data-bs-theme="dark"] .admin-shell .modal-card,
[data-bs-theme="dark"] .admin-shell .list-item,
[data-bs-theme="dark"] .admin-shell .hp-card {
  background: #1e293b !important;
  border-color: #334155 !important;
  box-shadow: none;
}

[data-bs-theme="dark"] .admin-shell .search,
[data-bs-theme="dark"] .admin-shell .compact-input,
[data-bs-theme="dark"] .admin-shell .form-grid input,
[data-bs-theme="dark"] .admin-shell .form-grid textarea,
[data-bs-theme="dark"] .admin-shell .form-grid select,
[data-bs-theme="dark"] .admin-shell .modal-close,
[data-bs-theme="dark"] .admin-shell .secondary,
[data-bs-theme="dark"] .admin-shell .action-pill,
[data-bs-theme="dark"] .admin-shell .hp-btn {
  background: #0f172a !important;
  border-color: #334155 !important;
  color: #e2e8f0 !important;
}

[data-bs-theme="dark"] .admin-shell .search:focus,
[data-bs-theme="dark"] .admin-shell .form-grid input:focus,
[data-bs-theme="dark"] .admin-shell .form-grid textarea:focus,
[data-bs-theme="dark"] .admin-shell .form-grid select:focus { border-color: #6366f1 !important; }

[data-bs-theme="dark"] .admin-shell .panel h3,
[data-bs-theme="dark"] .admin-shell .modal-head h3,
[data-bs-theme="dark"] .admin-shell .info-text strong,
[data-bs-theme="dark"] .admin-shell .td-info strong,
[data-bs-theme="dark"] .admin-shell .hp-title { color: #f1f5f9 !important; }

[data-bs-theme="dark"] .admin-shell .panel p,
[data-bs-theme="dark"] .admin-shell .table-header,
[data-bs-theme="dark"] .admin-shell .muted,
[data-bs-theme="dark"] .admin-shell small,
[data-bs-theme="dark"] .admin-shell .hp-desc,
[data-bs-theme="dark"] .admin-shell .detail-empty { color: #94a3b8 !important; }

[data-bs-theme="dark"] .admin-shell .index-badge { background: rgba(99, 102, 241, 0.2) !important; color: #a5b4fc !important; }
[data-bs-theme="dark"] .admin-shell .item-tag,
[data-bs-theme="dark"] .admin-shell .items-tag { background: #0f172a !important; color: #cbd5e1 !important; }

[data-bs-theme="dark"] .admin-shell .action-pill:hover,
[data-bs-theme="dark"] .admin-shell .hp-btn:hover { background: #334155 !important; color: #fff !important; }

[data-bs-theme="dark"] .admin-shell .error-banner {
  background: rgba(239, 68, 68, 0.12) !important;
  border-color: rgba(239, 68, 68, 0.4) !important;
  color: #fca5a5 !important;
}

[data-bs-theme="dark"] .admin-shell .workspace .subtitle { color: #c7d2fe !important; }
[data-bs-theme="dark"] .admin-shell .hero-stat { background: #1e293b; border-color: #334155; }
[data-bs-theme="dark"] .admin-shell .hero-stat strong { color: #f1f5f9 !important; }
[data-bs-theme="dark"] .admin-shell .hero-stat small { color: #94a3b8; }

[data-bs-theme="dark"] .admin-shell .ct-name { color: #f1f5f9 !important; }
[data-bs-theme="dark"] .admin-shell .ct-msg,
[data-bs-theme="dark"] .admin-shell .ct-subject { color: #cbd5e1 !important; }
[data-bs-theme="dark"] .admin-shell .ct-divider { border-color: #334155 !important; }

/* Modals are teleported to <body>, so they sit outside .admin-shell */
[data-bs-theme="dark"] .modal-backdrop { background: rgba(2, 6, 23, 0.65) !important; }
[data-bs-theme="dark"] .modal-card {
  background: #1e293b !important;
  border-color: #334155 !important;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.55) !important;
  color: #e2e8f0;
}
[data-bs-theme="dark"] .modal-card h3,
[data-bs-theme="dark"] .modal-card .chip { color: #f1f5f9 !important; }
[data-bs-theme="dark"] .modal-card p,
[data-bs-theme="dark"] .modal-card .input-label,
[data-bs-theme="dark"] .modal-card small,
[data-bs-theme="dark"] .modal-card .empty-state span { color: #94a3b8 !important; }
[data-bs-theme="dark"] .modal-card .eyebrow { color: #818cf8 !important; }
[data-bs-theme="dark"] .modal-card input,
[data-bs-theme="dark"] .modal-card textarea,
[data-bs-theme="dark"] .modal-card select,
[data-bs-theme="dark"] .modal-card .modal-close,
[data-bs-theme="dark"] .modal-card .secondary {
  background: #0f172a !important;
  border-color: #334155 !important;
  color: #e2e8f0 !important;
}
[data-bs-theme="dark"] .modal-card input::placeholder,
[data-bs-theme="dark"] .modal-card textarea::placeholder { color: #64748b !important; }
[data-bs-theme="dark"] .modal-card input:focus,
[data-bs-theme="dark"] .modal-card textarea:focus { border-color: #6366f1 !important; box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.18); }
[data-bs-theme="dark"] .modal-card .secondary:hover,
[data-bs-theme="dark"] .modal-card .modal-close:hover { background: #334155 !important; color: #fff !important; }
[data-bs-theme="dark"] .modal-card .chip { background: rgba(99, 102, 241, 0.18) !important; border-color: rgba(129, 140, 248, 0.4) !important; }
[data-bs-theme="dark"] .modal-card .upload-box { background: #0f172a !important; border-color: #334155 !important; }
[data-bs-theme="dark"] .modal-card .upload-box:hover { border-color: #6366f1 !important; }
[data-bs-theme="dark"] .modal-card .error-banner {
  background: rgba(239, 68, 68, 0.12) !important;
  border-color: rgba(239, 68, 68, 0.4) !important;
  color: #fca5a5 !important;
}

[data-bs-theme="dark"] .modal-card .used-label { color: #94a3b8 !important; }
[data-bs-theme="dark"] .modal-card .used-label strong { color: #a5b4fc !important; }

/* Section switch + smooth feel */
.section-enter-active { transition: opacity 0.35s ease, transform 0.45s cubic-bezier(0.2, 0.9, 0.3, 1); }
.section-leave-active { transition: opacity 0.12s ease; }
.section-enter-from { opacity: 0; transform: translateY(14px); }
.section-leave-to { opacity: 0; }
@media (prefers-reduced-motion: reduce) {
  .section-enter-active, .section-leave-active { transition: none; }
}
</style>

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
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid transparent;
  background: transparent;
  color: #94a3b8;
  text-align: left;
  font-size: 14px;
  font-weight: 600;
  transition: background 0.25s ease, color 0.25s ease, box-shadow 0.25s ease, transform 0.2s cubic-bezier(0.3, 1.4, 0.5, 1);
  cursor: pointer;
}

.menu-item i {
  font-size: 18px;
  transition: transform 0.25s cubic-bezier(0.3, 1.5, 0.5, 1);
}

.menu-item:hover i { transform: scale(1.18); }
.menu-item:active { transform: scale(0.97); }
.menu-item { animation: menu-in 0.5s cubic-bezier(0.2, 0.9, 0.3, 1) backwards; }
.menu-item:nth-child(2) { animation-delay: 0.05s; }
.menu-item:nth-child(3) { animation-delay: 0.1s; }
.menu-item:nth-child(4) { animation-delay: 0.15s; }
.menu-item:nth-child(5) { animation-delay: 0.2s; }
@keyframes menu-in { from { opacity: 0; transform: translateX(-14px); } to { opacity: 1; transform: none; } }

.hero-panel { animation: hero-in 0.6s cubic-bezier(0.2, 0.9, 0.3, 1) backwards; }
@keyframes hero-in { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: none; } }

@media (prefers-reduced-motion: reduce) {
  .menu-item, .hero-panel { animation: none; }
}

.menu-item:hover {
  background: #1e293b;
  color: #fff;
  transform: translateX(3px);
}

.menu-item.active {
  background: linear-gradient(135deg, #6366f1, #7c3aed);
  color: #fff;
  border-color: transparent;
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
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
  padding: 28px;
  min-width: 0;
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
  border-radius: 20px;
  background: linear-gradient(120deg, #1e1b4b 0%, #4338ca 55%, #7c3aed 100%);
  border: 0;
  box-shadow: 0 18px 40px rgba(79, 70, 229, 0.25);
}

.eyebrow {
  margin: 0 0 6px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-size: 10px;
  color: #f7f7f8;
  font-weight: 700;
}

.hero-panel h2 {
  margin: 0;
  font-size: 24px;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: -0.5px;
}

.subtitle {
  margin: 6px 0 0;
  max-width: 600px;
  font-size: 14px;
  color: #c7d2fe;
  line-height: 1.5;
}

.hero-stat {
  min-width: 150px;
  padding: 16px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.6);
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.18);
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

  .menu-item:hover {
    transform: none;
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
