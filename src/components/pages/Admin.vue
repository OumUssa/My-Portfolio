<template>
  <div class="admin-shell mt-5 pt-3">
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-mark">A</div>
        <div>
          <h1>Admin</h1>
          <p>Portfolio dashboard</p>
        </div>
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
            Manage projects and categories with static data first, then connect
            the API later.
          </p>
        </div>

        <div class="hero-stat">
          <span class="stat-label">Dashboard</span>
          <strong>{{ projectCount }} Projects</strong>
          <small>{{ categoryCount }} Categories</small>
        </div>
      </section>

      <section v-if="activeSection === 'dashboard'" class="overview-grid">
        <article class="overview-card">
          <p class="card-label">Projects</p>
          <h3>{{ projectCount }}</h3>
          <p>Search, add, edit, view details, and delete.</p>
        </article>

        <article class="overview-card">
          <p class="card-label">Categories</p>
          <h3>{{ categoryCount }}</h3>
          <p>CRUD categories for organizing your portfolio content.</p>
        </article>

        <article class="overview-card">
          <p class="card-label">Status</p>
          <h3>Static UI</h3>
          <p>Ready for API integration when you want it.</p>
        </article>
      </section>

      <section v-if="activeSection === 'projects'" class="panel-layout">
        <div class="panel">
          <div class="panel-head">
            <div>
              <p class="eyebrow">Projects</p>
              <h3>Project list</h3>
            </div>
            <div class="panel-actions">
              <input
                v-model="projectSearch"
                class="search"
                type="search"
                placeholder="Search projects" />
              <button
                class="primary"
                type="button"
                @click="openAddProjectModal">
                Add project
              </button>
            </div>
          </div>

          <div class="list-stack">
            <button
              v-for="project in filteredProjects"
              :key="project.id"
              class="list-item"
              :class="{ selected: selectedProject?.id === project.id }"
              @click="selectProject(project)">
              <div>
                <strong>{{ project.title }}</strong>
                <small>{{ project.category }} • {{ project.tech }}</small>
              </div>
              <span class="item-tag">{{ project.status }}</span>
            </button>
          </div>
        </div>

        <div class="panel detail-panel">
          <p class="eyebrow">Details</p>
          <h3>{{ selectedProject?.title || "Select a project" }}</h3>
          <p class="muted">
            {{
              selectedProject?.description ||
              "Click a project to view more details."
            }}
          </p>

          <div v-if="selectedProject" class="detail-box">
            <p><strong>Category:</strong> {{ selectedProject.category }}</p>
            <p><strong>Tech:</strong> {{ selectedProject.tech }}</p>
            <p><strong>Status:</strong> {{ selectedProject.status }}</p>
            <p><strong>Link:</strong> {{ selectedProject.link }}</p>
          </div>

          <div class="detail-actions" v-if="selectedProject">
            <button class="secondary" @click="editProject(selectedProject)">
              Edit
            </button>
            <button class="danger" @click="deleteProject(selectedProject.id)">
              Delete
            </button>
          </div>
        </div>
      </section>

      <section v-if="activeSection === 'categories'" class="panel-layout">
        <div class="panel">
          <div class="panel-head">
            <div>
              <p class="eyebrow">Categories</p>
              <h3>Category CRUD</h3>
            </div>
            <div class="panel-actions">
              <input
                v-model="categorySearch"
                class="search"
                type="search"
                placeholder="Search categories" />
              <button
                class="primary"
                type="button"
                @click="openAddCategoryModal">
                Add category
              </button>
            </div>
          </div>

          <div class="list-stack categories">
            <button
              v-for="category in filteredCategories"
              :key="category.id"
              class="list-item"
              :class="{ selected: selectedCategory?.id === category.id }"
              @click="selectCategory(category)">
              <div>
                <strong>{{ category.name }}</strong>
                <small>{{ category.note }}</small>
              </div>
              <span class="item-tag">{{ category.items }} items</span>
            </button>
          </div>
        </div>

        <div class="panel detail-panel">
          <p class="eyebrow">Details</p>
          <h3>{{ selectedCategory?.name || "Select a category" }}</h3>
          <p class="muted">
            {{
              selectedCategory?.note || "Click a category to view more details."
            }}
          </p>

          <div v-if="selectedCategory" class="detail-box">
            <p><strong>Items:</strong> {{ selectedCategory.items }}</p>
            <p><strong>Created:</strong> {{ selectedCategory.createdAt }}</p>
          </div>

          <div class="detail-actions" v-if="selectedCategory">
            <button class="secondary" @click="editCategory(selectedCategory)">
              Edit
            </button>
            <button class="danger" @click="deleteCategory(selectedCategory.id)">
              Delete
            </button>
          </div>
        </div>
      </section>
    </main>

    <teleport to="body">
      <transition name="fade">
        <div v-if="modalType" class="modal-backdrop" @click.self="closeModal">
          <div class="modal-card">
            <div class="modal-head">
              <div>
                <p class="eyebrow">
                  {{ modalType === "project" ? "Projects" : "Categories" }}
                </p>
                <h3>{{ modalTitle }}</h3>
              </div>
              <button class="modal-close" type="button" @click="closeModal">
                ×
              </button>
            </div>

            <div v-if="modalType === 'project'" class="modal-form">
              <div class="form-grid modal-grid">
                <input
                  v-model="projectForm.title"
                  type="text"
                  placeholder="Project title" />
                <input
                  v-model="projectForm.category"
                  type="text"
                  placeholder="Category" />
                <input
                  v-model="projectForm.tech"
                  type="text"
                  placeholder="Tech stack" />
                <input
                  v-model="projectForm.link"
                  type="text"
                  placeholder="Project link" />
                <select v-model="projectForm.status">
                  <option value="Draft">Draft</option>
                  <option value="Live">Live</option>
                  <option value="Archived">Archived</option>
                </select>
                <textarea
                  v-model="projectForm.description"
                  rows="4"
                  placeholder="Short description"></textarea>
              </div>

              <div class="form-actions modal-actions">
                <button class="primary" @click="saveProject">
                  {{ editingProjectId ? "Update project" : "Add project" }}
                </button>
                <button class="secondary" type="button" @click="closeModal">
                  Cancel
                </button>
              </div>
            </div>

            <div v-else class="modal-form">
              <div class="form-grid modal-grid">
                <input
                  v-model="categoryForm.name"
                  type="text"
                  placeholder="Category name" />
                <textarea
                  v-model="categoryForm.note"
                  rows="4"
                  placeholder="Short note"></textarea>
              </div>

              <div class="form-actions modal-actions">
                <button class="primary" @click="saveCategory">
                  {{ editingCategoryId ? "Update category" : "Add category" }}
                </button>
                <button class="secondary" type="button" @click="closeModal">
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </teleport>
  </div>
</template>

<script setup>
import { computed, ref } from "vue";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const auth = useAuthStore();
const { user } = storeToRefs(auth);
const userInitial = computed(
  () => user.value?.name?.slice(0, 1)?.toUpperCase() || "A",
);

const menuItems = [
  { key: "dashboard", label: "Dashboard" },
  { key: "projects", label: "Projects" },
  { key: "categories", label: "Categories" },
];

const activeSection = ref("dashboard");
const modalType = ref(null);

const projects = ref([
  {
    id: 1,
    title: "Portfolio Landing Page",
    category: "Web Design",
    tech: "Vue, CSS, Vite",
    link: "https://example.com",
    status: "Live",
    description:
      "A clean hero-focused portfolio landing page with animated sections.",
  },
  {
    id: 2,
    title: "Dashboard Admin UI",
    category: "Dashboard",
    tech: "Vue, Pinia",
    link: "https://example.com/dashboard",
    status: "Draft",
    description: "Admin dashboard UI for project and category management.",
  },
  {
    id: 3,
    title: "Client Showcase",
    category: "Showcase",
    tech: "Vue, API",
    link: "https://example.com/showcase",
    status: "Live",
    description:
      "A client project showcase with detail cards and responsive layout.",
  },
]);

const categories = ref([
  {
    id: 1,
    name: "Web Design",
    note: "Landing pages and visual design",
    items: 4,
    createdAt: "2026-05-01",
  },
  {
    id: 2,
    name: "Dashboard",
    note: "Admin and control panels",
    items: 2,
    createdAt: "2026-05-07",
  },
  {
    id: 3,
    name: "Showcase",
    note: "Portfolio and client presentation",
    items: 3,
    createdAt: "2026-05-12",
  },
]);

const projectSearch = ref("");
const categorySearch = ref("");
const selectedProject = ref(projects.value[0]);
const selectedCategory = ref(categories.value[0]);
const editingProjectId = ref(null);
const editingCategoryId = ref(null);

const projectForm = ref({
  title: "",
  category: "",
  tech: "",
  link: "",
  description: "",
  status: "Draft",
});

const categoryForm = ref({
  name: "",
  note: "",
});

const modalTitle = computed(() => {
  if (modalType.value === "project") {
    return editingProjectId.value ? "Edit project" : "Add new project";
  }
  if (modalType.value === "category") {
    return editingCategoryId.value ? "Edit category" : "Add new category";
  }
  return "";
});

const projectCount = computed(() => projects.value.length);
const categoryCount = computed(() => categories.value.length);

const filteredProjects = computed(() => {
  const keyword = projectSearch.value.trim().toLowerCase();
  if (!keyword) return projects.value;
  return projects.value.filter((project) =>
    [project.title, project.category, project.tech, project.status]
      .join(" ")
      .toLowerCase()
      .includes(keyword),
  );
});

const filteredCategories = computed(() => {
  const keyword = categorySearch.value.trim().toLowerCase();
  if (!keyword) return categories.value;
  return categories.value.filter((category) =>
    [category.name, category.note].join(" ").toLowerCase().includes(keyword),
  );
});

function resetProjectForm() {
  editingProjectId.value = null;
  projectForm.value = {
    title: "",
    category: "",
    tech: "",
    link: "",
    description: "",
    status: "Draft",
  };
}

function resetCategoryForm() {
  editingCategoryId.value = null;
  categoryForm.value = { name: "", note: "" };
}

function openAddProjectModal() {
  resetProjectForm();
  modalType.value = "project";
}

function openAddCategoryModal() {
  resetCategoryForm();
  modalType.value = "category";
}

function closeModal() {
  modalType.value = null;
}

function selectProject(project) {
  selectedProject.value = project;
}

function selectCategory(category) {
  selectedCategory.value = category;
}

function saveProject() {
  const payload = {
    id: editingProjectId.value || Date.now(),
    title: projectForm.value.title,
    category: projectForm.value.category,
    tech: projectForm.value.tech,
    link: projectForm.value.link,
    status: projectForm.value.status || "Draft",
    description: projectForm.value.description,
  };

  if (editingProjectId.value) {
    projects.value = projects.value.map((project) =>
      project.id === editingProjectId.value ? payload : project,
    );
  } else {
    projects.value.unshift(payload);
  }

  selectedProject.value = payload;
  resetProjectForm();
  closeModal();
}

function editProject(project) {
  editingProjectId.value = project.id;
  projectForm.value = { ...project };
  activeSection.value = "projects";
  modalType.value = "project";
}

function deleteProject(projectId) {
  projects.value = projects.value.filter((project) => project.id !== projectId);
  if (selectedProject.value?.id === projectId) {
    selectedProject.value = projects.value[0] || null;
  }
}

function saveCategory() {
  const payload = {
    id: editingCategoryId.value || Date.now(),
    name: categoryForm.value.name,
    note: categoryForm.value.note,
    items: editingCategoryId.value ? selectedCategory.value?.items || 0 : 0,
    createdAt: editingCategoryId.value
      ? selectedCategory.value?.createdAt ||
        new Date().toISOString().slice(0, 10)
      : new Date().toISOString().slice(0, 10),
  };

  if (editingCategoryId.value) {
    categories.value = categories.value.map((category) =>
      category.id === editingCategoryId.value ? payload : category,
    );
  } else {
    categories.value.unshift(payload);
  }

  selectedCategory.value = payload;
  resetCategoryForm();
  closeModal();
}

function editCategory(category) {
  editingCategoryId.value = category.id;
  categoryForm.value = {
    name: category.name,
    note: category.note,
  };
  activeSection.value = "categories";
  modalType.value = "category";
}

function deleteCategory(categoryId) {
  categories.value = categories.value.filter(
    (category) => category.id !== categoryId,
  );
  if (selectedCategory.value?.id === categoryId) {
    selectedCategory.value = categories.value[0] || null;
  }
}

function logout() {
  auth.logout();
  router.push({ path: "/login" });
}
</script>

<style scoped>
.admin-shell {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  background:
    radial-gradient(
      circle at top left,
      rgba(6, 182, 212, 0.12),
      transparent 28%
    ),
    radial-gradient(
      circle at bottom right,
      rgba(59, 130, 246, 0.12),
      transparent 28%
    ),
    linear-gradient(135deg, #f7fbff 0%, #edf4ff 100%);
  color: #0f172a;
}

.sidebar {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 28px 20px;
  background: linear-gradient(180deg, #102748 0%, #0a1a31 100%);
  color: #dbeafe;
  box-shadow: 20px 0 40px rgba(15, 23, 42, 0.12);
}

.brand {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 32px;
}

.brand-mark {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  font-size: 22px;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(135deg, #3b82f6, #06b6d4);
  box-shadow: 0 14px 28px rgba(6, 182, 212, 0.22);
}

.brand h1 {
  margin: 0;
  font-size: 22px;
}

.brand p {
  margin: 4px 0 0;
  color: #93c5fd;
  font-size: 13px;
}

.menu {
  display: grid;
  gap: 10px;
}

.menu-item {
  width: 100%;
  padding: 14px 16px;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.04);
  color: #dbeafe;
  text-align: left;
  transition:
    background 0.2s ease,
    transform 0.2s ease,
    border-color 0.2s ease;
}

.menu-item:hover,
.menu-item.active {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(125, 211, 252, 0.28);
  transform: translateX(2px);
}

.sidebar-footer {
  display: grid;
  gap: 16px;
}

.mini-user {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.avatar {
  width: 46px;
  height: 46px;
  border-radius: 14px;
  display: grid;
  place-items: center;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(135deg, #3b82f6, #06b6d4);
  flex-shrink: 0;
}

.mini-user strong {
  display: block;
  margin-bottom: 2px;
}

.mini-user small {
  color: #93c5fd;
}

.logout-btn {
  padding: 14px 16px;
  border-radius: 14px;
  border: 1px solid rgba(248, 113, 113, 0.25);
  background: rgba(239, 68, 68, 0.08);
  color: #fee2e2;
}

.workspace {
  padding: 28px;
  display: grid;
  gap: 20px;
}

.hero-panel,
.overview-card,
.panel {
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(148, 163, 184, 0.16);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.hero-panel {
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.eyebrow {
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 12px;
  color: #2563eb;
}

.hero-panel h2,
.panel h3 {
  margin: 0;
  font-size: 30px;
  color: #0f172a;
}

.subtitle {
  margin: 10px 0 0;
  max-width: 700px;
  color: #475569;
}

.hero-stat {
  min-width: 180px;
  padding: 18px;
  border-radius: 18px;
  background: linear-gradient(135deg, #eff6ff, #e0f2fe);
  border: 1px solid rgba(59, 130, 246, 0.12);
}

.stat-label,
.card-label {
  display: block;
  margin-bottom: 6px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2563eb;
}

.hero-stat strong {
  display: block;
  font-size: 26px;
  color: #0f172a;
}

.hero-stat small {
  color: #475569;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.overview-card {
  padding: 20px;
}

.overview-card h3 {
  margin: 0 0 8px;
  font-size: 28px;
  color: #0f172a;
}

.overview-card p {
  margin: 0;
  color: #475569;
}

.panel-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(280px, 0.75fr);
  gap: 16px;
}

.panel {
  padding: 20px;
}

.panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.panel-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search,
.form-grid input,
.form-grid textarea,
.form-grid select {
  width: 100%;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #0f172a;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.form-grid textarea {
  grid-column: 1 / -1;
  resize: vertical;
}

.category-grid textarea {
  grid-column: 1 / -1;
}

.modal-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.form-actions,
.detail-actions {
  display: flex;
  gap: 10px;
  margin-top: 14px;
}

.primary,
.secondary,
.danger {
  padding: 11px 14px;
  border-radius: 12px;
  font-weight: 600;
}

.primary {
  background: linear-gradient(135deg, #2563eb, #06b6d4);
  color: #fff;
}

.secondary {
  background: #fff;
  color: #0f172a;
  border: 1px solid rgba(148, 163, 184, 0.24);
}

.danger {
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fecaca;
}

.list-stack {
  display: grid;
  gap: 10px;
  margin-top: 16px;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 16px;
  border: 1px solid rgba(148, 163, 184, 0.18);
  background: #fff;
  text-align: left;
}

.list-item.selected {
  border-color: rgba(37, 99, 235, 0.35);
  background: linear-gradient(135deg, #eff6ff, #f8fbff);
}

.list-item strong {
  display: block;
  margin-bottom: 4px;
  color: #0f172a;
}

.list-item small,
.muted {
  color: #64748b;
}

.item-tag {
  padding: 7px 10px;
  border-radius: 999px;
  font-size: 12px;
  background: #e0f2fe;
  color: #0369a1;
  white-space: nowrap;
}

.detail-panel {
  align-self: start;
}

.detail-box {
  margin-top: 16px;
  padding: 16px;
  border-radius: 16px;
  background: #f8fbff;
  border: 1px solid rgba(148, 163, 184, 0.18);
}

.detail-box p {
  margin: 0 0 10px;
  color: #334155;
}

.detail-box p:last-child {
  margin-bottom: 0;
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 20px;
  background: rgba(15, 23, 42, 0.55);
  backdrop-filter: blur(10px);
  z-index: 50;
}

.modal-card {
  width: min(760px, 100%);
  padding: 24px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.96);
  border: 1px solid rgba(148, 163, 184, 0.18);
  box-shadow: 0 30px 80px rgba(15, 23, 42, 0.24);
}

.modal-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 18px;
}

.modal-head h3 {
  margin: 0;
  font-size: 28px;
}

.modal-close {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #0f172a;
  font-size: 22px;
  line-height: 1;
}

.modal-form {
  display: grid;
  gap: 16px;
}

.modal-actions {
  margin-top: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.18s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1100px) {
  .admin-shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    gap: 20px;
  }
}

@media (max-width: 900px) {
  .overview-grid,
  .panel-layout {
    grid-template-columns: 1fr;
  }

  .hero-panel,
  .panel-head,
  .form-grid,
  .form-actions,
  .detail-actions {
    flex-direction: column;
  }

  .panel-head {
    align-items: stretch;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .panel-actions,
  .modal-grid {
    grid-template-columns: 1fr;
  }

  .panel-actions {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
