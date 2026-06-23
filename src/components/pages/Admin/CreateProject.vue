<template>
  <section class="panel-layout">
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
            <i class="bi bi-plus-lg"></i>
            Add project
          </button>
        </div>
      </div>

      <div class="table-container">
        <div class="table-header">
          <div class="th-id">#</div>
          <div class="th-info">Project Info</div>
          <div class="th-tech">Tech Stack</div>
          <div class="th-status">Status</div>
          <div class="th-actions">Action</div>
        </div>

        <div class="list-stack">
          <button
            v-for="(project, index) in filteredProjects"
            :key="project.id"
            class="list-item"
            :class="{ selected: selectedProject?.id === project.id }"
            @click="selectProject(project)">
            
            <div class="td-id">
              <span class="index-badge">{{ String(index + 1).padStart(3, '0') }}</span>
            </div>

            <div class="td-info">
              <div class="info-text">
                <strong>{{ project.title }}</strong>
                <small>{{ project.category }}</small>
              </div>
            </div>

            <div class="td-tech">
              <small>{{ project.tech }}</small>
            </div>

            <div class="td-status">
              <span class="item-tag" :class="project.status ? project.status.toLowerCase() : 'draft'">
                <span class="status-dot"></span> {{ project.status || 'Draft' }}
              </span>
            </div>

            <div class="td-actions">
              <button
                class="action-pill view-pill"
                type="button"
                title="View project"
                @click.stop="selectProject(project)">
                <i class="bi bi-eye"></i> View
              </button>
              <button
                class="action-pill edit-pill"
                type="button"
                title="Edit project"
                @click.stop="editProject(project)">
                <i class="bi bi-pencil-square"></i> Edit
              </button>
              <button
                class="action-pill delete-pill"
                type="button"
                title="Delete project"
                @click.stop="handleDeleteProject(project.id)">
                <i class="bi bi-trash3"></i> Delete
              </button>
            </div>
          </button>
        </div>
      </div>
    </div>

    <div class="panel detail-panel">
      <p class="eyebrow">Details</p>

      <div v-if="!selectedProject" class="detail-empty">
        <i class="bi bi-collection"></i>
        <p>Click a project row to preview it here.</p>
      </div>

      <div v-else class="hp-card">
        <!-- Thumbnail with hover overlay – mirrors home page card -->
        <div
          class="hp-thumb"
          :style="{
            backgroundImage: selectedProject.image
              ? `url('${selectedProject.image}')`
              : `linear-gradient(135deg, #e0e7ff, #c7d2fe)`,
          }">
          <div class="hp-overlay">
            <a
              v-if="selectedProject.openProject"
              :href="selectedProject.openProject"
              target="_blank" rel="noopener noreferrer"
              class="hp-action" title="Open project">
              <i class="bi bi-box-arrow-up-right"></i>
            </a>
            <a
              v-if="selectedProject.githubLink"
              :href="selectedProject.githubLink"
              target="_blank" rel="noopener noreferrer"
              class="hp-action" title="GitHub">
              <i class="bi bi-github"></i>
            </a>
            <a
              v-if="selectedProject.link"
              :href="selectedProject.link"
              target="_blank" rel="noopener noreferrer"
              class="hp-action" title="Live preview">
              <i class="bi bi-play-circle"></i>
            </a>
          </div>
          <span class="hp-status-badge" :class="selectedProject.status ? selectedProject.status.toLowerCase() : 'draft'">
            <span class="status-dot"></span> {{ selectedProject.status || 'Draft' }}
          </span>
        </div>

        <!-- Card body -->
        <div class="hp-body">
          <div class="hp-tags">
            <span
              v-for="tag in (selectedProject.tags && selectedProject.tags.length
                ? selectedProject.tags
                : (selectedProject.tech ? selectedProject.tech.split(',') : []))"
              :key="tag"
              class="hp-tag">
              {{ tag.trim() }}
            </span>
          </div>
          <h3 class="hp-title">{{ selectedProject.title }}</h3>
          <p class="hp-desc">
            {{ selectedProject.description || selectedProject.desc || 'No description available.' }}
          </p>
          <div class="hp-edit-row">
            <button class="hp-btn hp-edit" type="button" @click="editProject(selectedProject)">
              <i class="bi bi-pencil-square"></i> Edit
            </button>
            <button class="hp-btn hp-delete" type="button" @click="handleDeleteProject(selectedProject.id)">
              <i class="bi bi-trash3"></i> Delete
            </button>
          </div>
        </div>
      </div>
    </div>

    <teleport to="body">
      <transition name="fade">
        <div v-if="isModalOpen" class="modal-backdrop" @click.self="closeModal">
          <div class="modal-card">
            <div class="modal-head">
              <div>
                <p class="eyebrow">Projects</p>
                <h3>{{ editingProjectId ? "Edit project" : "Add new project" }}</h3>
              </div>
              <button class="modal-close" type="button" @click="closeModal">
                ×
              </button>
            </div>

            <p v-if="loadError" class="error-banner">{{ loadError }}</p>

            <div class="modal-form">
              <div class="form-grid modal-grid">
                <input
                  v-model="projectForm.title"
                  type="text"
                  placeholder="Project title" />
                <input
                  v-model="projectForm.tech"
                  type="text"
                  placeholder="Tech details (e.g. Vue, Node)" />
                <input
                  v-model="projectForm.link"
                  type="text"
                  placeholder="Live Project link" />
                <input
                  v-model="projectForm.openProject"
                  type="text"
                  placeholder="Open Project URL" />
                <input
                  v-model="projectForm.githubLink"
                  type="text"
                  placeholder="GitHub URL" />
                <select v-model="projectForm.status">
                  <option value="Draft">Draft</option>
                  <option value="Live">Live</option>
                  <option value="Archived">Archived</option>
                </select>

                <div class="multi-select-container">
                  <label class="input-label">Tech Stacks (Categories)</label>
                  <div class="selected-chips">
                    <span v-for="catId in projectForm.categoryIds" :key="catId" class="chip">
                      {{ getCategoryName(catId) }}
                      <button type="button" @click.prevent="removeCategory(catId)" class="remove-chip">&times;</button>
                    </span>
                  </div>
                  <select @change="addCategory($event)" class="compact-input">
                    <option value="" disabled selected>Add a Tech Stack...</option>
                    <option v-for="cat in availableCategories" :key="cat.id" :value="cat.id">
                      {{ cat.name }}
                    </option>
                  </select>
                </div>
                <div class="image-upload-area">
                  <label class="upload-box" :class="{ 'has-image': !!(localImagePreview || projectForm.image), 'is-uploading': uploadingImage }">
                    <input
                      type="file"
                      accept="image/*"
                      class="hidden-file-input"
                      @change="onFileChange" />
                    
                    <div v-if="localImagePreview || projectForm.image" class="image-preview-wrapper" :style="{ opacity: uploadingImage ? 0.6 : 1 }">
                      <img :src="localImagePreview || projectForm.image" alt="Thumbnail preview" class="preview-img" />
                      <div v-if="uploadingImage" class="change-overlay" style="opacity: 1; flex-direction: column;">
                        <div class="spinner"></div>
                        <span>Uploading...</span>
                      </div>
                      <div v-else class="change-overlay">
                        <i class="bi bi-camera"></i>
                        <span>Change Image</span>
                      </div>
                    </div>
                    <div v-else-if="uploadingImage" class="upload-state">
                      <div class="spinner"></div>
                      <span>Uploading image...</span>
                    </div>
                    <div v-else class="empty-state">
                      <i class="bi bi-cloud-arrow-up"></i>
                      <span>Click to upload thumbnail</span>
                      <small>JPEG, PNG, JPG, WEBP</small>
                    </div>
                  </label>
                </div>
                <textarea
                  v-model="projectForm.description"
                  rows="3"
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
          </div>
        </div>
      </transition>
    </teleport>
  </section>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { createProject, updateProject, deleteProject as deleteProjectRequest, uploadThumbnail } from "@/data/projectsApi.js";

const props = defineProps({
  projects: {
    type: Array,
    required: true,
  },
  categories: {
    type: Array,
    required: true,
  },
  token: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(["update:projects"]);

const projectSearch = ref("");
const selectedProject = ref(null);
const isModalOpen = ref(false);
const editingProjectId = ref(null);
const loadError = ref("");
const uploadingImage = ref(false);
const localImagePreview = ref(null);

const projectForm = ref({
  title: "",
  categoryIds: [],
  tech: "",
  link: "",
  openProject: "",
  githubLink: "",
  image: "",
  description: "",
  status: "Draft",
});

function getInitials(title) {
  if (!title) return "P";
  const words = title.split(" ").filter(w => w);
  if (words.length >= 2) {
    return (words[0][0] + words[1][0]).toUpperCase();
  }
  return title.substring(0, 2).toUpperCase();
}

function getAvatarColor(title) {
  const colors = ["#dbeafe", "#e0e7ff", "#f3e8ff", "#fae8ff", "#ffe4e6", "#ffedd5", "#fef9c3", "#dcfce7"];
  const textColors = ["#1e40af", "#3730a3", "#6b21a8", "#86198f", "#be123c", "#c2410c", "#a16207", "#166534"];
  if (!title) return { bg: colors[0], text: textColors[0] };
  let hash = 0;
  for (let i = 0; i < title.length; i++) {
    hash = title.charCodeAt(i) + ((hash << 5) - hash);
  }
  const index = Math.abs(hash) % colors.length;
  return { bg: colors[index], text: textColors[index] };
}

const availableCategories = computed(() => {
  return props.categories.filter(c => !projectForm.value.categoryIds.includes(c.id));
});

function getCategoryName(id) {
  const cat = props.categories.find(c => c.id === id);
  return cat ? cat.name : "Unknown";
}

function addCategory(event) {
  const id = Number(event.target.value);
  if (id && !projectForm.value.categoryIds.includes(id)) {
    projectForm.value.categoryIds.push(id);
  }
  event.target.value = ""; // Reset select
}

function removeCategory(id) {
  projectForm.value.categoryIds = projectForm.value.categoryIds.filter(catId => catId !== id);
}

async function onFileChange(event) {
  const file = event.target.files[0];
  if (!file) return;

  localImagePreview.value = URL.createObjectURL(file);

  if (!props.token) {
    loadError.value = "Missing admin token. Please login again.";
    return;
  }

  uploadingImage.value = true;
  loadError.value = "";
  try {
    const res = await uploadThumbnail(file, props.token);
    let imageUrl = res.thumbnail || res.url || res.image || res.data?.thumbnail || res.data?.url || res.data?.image || res.path || res.filePath || res.file_path || res.filename || res.file_name || res.fileUrl || res.file;
    
    if (!imageUrl && typeof res === 'object') {
      const vals = Object.values(res);
      imageUrl = vals.find(v => typeof v === 'string' && /\.(jpg|jpeg|png|webp|gif)$/i.test(v)) || vals.find(v => typeof v === 'string' && v.includes('upload')) || "";
    }
    
    if (!imageUrl && typeof res === 'string') {
      imageUrl = res;
    }
    projectForm.value.image = typeof imageUrl === 'string' ? imageUrl : "";
  } catch (err) {
    loadError.value = err instanceof Error ? err.message : "Failed to upload image.";
  } finally {
    uploadingImage.value = false;
    event.target.value = ""; // Reset file input
  }
}

watch(() => props.projects, (newProjects) => {
  if (!selectedProject.value || !newProjects.find(p => p.id === selectedProject.value.id)) {
    selectedProject.value = newProjects[0] || null;
  } else {
    selectedProject.value = newProjects.find(p => p.id === selectedProject.value.id);
  }
}, { immediate: true });

const filteredProjects = computed(() => {
  const keyword = projectSearch.value.trim().toLowerCase();
  if (!keyword) return props.projects;
  return props.projects.filter((project) =>
    [project.title, project.category, project.tech, project.status]
      .join(" ")
      .toLowerCase()
      .includes(keyword),
  );
});

function normalizeCategoryName(value) {
  return String(value || "General Stack").trim() || "General Stack";
}

function splitTech(value) {
  if (Array.isArray(value)) {
    return value.map((item) => String(item || "").trim()).filter(Boolean);
  }
  if (typeof value !== "string") {
    return [];
  }
  return value.split(",").map((item) => item.trim()).filter(Boolean);
}

function toStoredProject(project, existingProject = null) {
  const category = normalizeCategoryName(project.category);
  const techTags = splitTech(project.tech);
  const createdAt = existingProject?.createdAt || project.createdAt || new Date().toISOString().slice(0, 10);
  const previousTags = Array.isArray(existingProject?.tags) ? existingProject.tags : [];
  const tags = techTags.length ? techTags : previousTags.length ? previousTags : [category];

  return {
    id: project.id,
    adminId: existingProject?.adminId || null,
    adminName: existingProject?.adminName || "Admin",
    title: (project.title && typeof project.title === "string" ? project.title.trim() : "") || "Untitled project",
    desc: project.description && typeof project.description === "string" ? project.description.trim() : "",
    image: (project.image && typeof project.image === "string" ? project.image.trim() : "") || existingProject?.image || "",
    liveLink: project.link && typeof project.link === "string" ? project.link.trim() : "",
    githubLink: (project.githubLink && typeof project.githubLink === "string" ? project.githubLink.trim() : "") || existingProject?.githubLink || "",
    openProject: (project.openProject && typeof project.openProject === "string" ? project.openProject.trim() : "") || existingProject?.openProject || "",
    createdAt,
    categories: [category],
    category,
    tags,
    status: project.status || existingProject?.status || "Draft",
    tech: techTags.join(", "),
  };
}

function resetProjectForm() {
  editingProjectId.value = null;
  projectForm.value = {
    title: "",
    categoryIds: [],
    tech: "",
    link: "",
    openProject: "",
    githubLink: "",
    image: "",
    description: "",
    status: "Draft",
  };
  localImagePreview.value = null;
  loadError.value = "";
}

function openAddProjectModal() {
  resetProjectForm();
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
}

function selectProject(project) {
  selectedProject.value = project;
}

function editProject(project) {
  editingProjectId.value = project.id;
  const selectedCatIds = project.categories
    ? project.categories.map(catName => {
        const found = props.categories.find(c => c.name === catName);
        return found ? found.id : null;
      }).filter(Boolean)
    : [];

  projectForm.value = {
    title: project.title,
    categoryIds: selectedCatIds,
    tech: project.tech,
    link: project.link,
    openProject: project.openProject,
    githubLink: project.githubLink,
    image: project.image,
    description: project.description,
    status: project.status || "Draft",
  };
  localImagePreview.value = null;
  isModalOpen.value = true;
}

async function saveProject() {
  loadError.value = "";
  try {
    const existingProject = props.projects.find(p => p.id === editingProjectId.value);
    const payload = toStoredProject(
      {
        id: editingProjectId.value || Date.now(),
        title: projectForm.value.title,
        category: projectForm.value.categoryIds.length > 0 ? getCategoryName(projectForm.value.categoryIds[0]) : "General Stack",
        tech: projectForm.value.tech,
        link: projectForm.value.link,
        openProject: projectForm.value.openProject,
        githubLink: projectForm.value.githubLink,
        image: projectForm.value.image,
        status: projectForm.value.status || "Draft",
        description: projectForm.value.description,
      },
      existingProject || null,
    );
    
    payload.categoryIds = projectForm.value.categoryIds;

    if (!props.token) {
      loadError.value = "Missing admin token. Please login again.";
      return;
    }

    let nextProjects = [...props.projects];
    if (editingProjectId.value) {
      const updated = await updateProject(editingProjectId.value, payload, props.token);
      nextProjects = nextProjects.map((p) => p.id === editingProjectId.value ? updated : p);
      selectedProject.value = updated;
    } else {
      const created = await createProject(payload, props.token);
      nextProjects = [created, ...nextProjects];
      selectedProject.value = created;
    }

    emit("update:projects", nextProjects);
    closeModal();
  } catch (err) {
    loadError.value = err instanceof Error ? err.message : "Failed to save project.";
  }
}

async function handleDeleteProject(projectId) {
  if (!confirm("Are you sure you want to delete this project?")) return;
  try {
    if (!props.token) {
      alert("Missing admin token. Please login again.");
      return;
    }
    await deleteProjectRequest(projectId, props.token);
    const nextProjects = props.projects.filter((project) => project.id !== projectId);
    emit("update:projects", nextProjects);
  } catch (err) {
    alert(err instanceof Error ? err.message : "Failed to delete project.");
  }
}
</script>

<style scoped>
/* Inherit base styles from Admin.vue or duplicate specific ones here */
.panel-layout {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(280px, 0.75fr);
  gap: 16px;
}

.panel {
  padding: 20px;
  border-radius: 22px;
  background: #fff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.04);
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

.search, .compact-input, .form-grid input, .form-grid textarea, .form-grid select {
  width: 100%;
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #f8fafc;
  color: #0f172a;
  font-size: 13px;
}

.search:focus, .compact-input:focus, .form-grid input:focus, .form-grid textarea:focus, .form-grid select:focus {
  outline: none;
  border-color: #6366f1;
  background: #fff;
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

.primary, .secondary, .danger {
  padding: 9px 18px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 13px;
  transition: all 0.25s ease;
  cursor: pointer;
  white-space: nowrap;
}

.primary {
  width: auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #6366f1, #7c3aed);
  color: #fff;
  border: 1px solid transparent;
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
}

.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
}

.secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.secondary:hover {
  color: #6366f1;
  border-color: #c7d2fe;
}

.table-container {
  display: flex;
  flex-direction: column;
  margin-top: 16px;
  overflow-x: auto;
}

.table-header {
  display: flex;
  align-items: center;
  padding: 0 16px 12px;
  font-size: 13px;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  min-width: 700px;
}

.th-id, .td-id { width: 60px; flex-shrink: 0; }
.th-info, .td-info { flex: 2; min-width: 220px; }
.th-tech, .td-tech { flex: 1.5; min-width: 150px; }
.th-status, .td-status { width: 120px; flex-shrink: 0; }
.th-actions, .td-actions { width: 220px; flex-shrink: 0; display: flex; justify-content: flex-end; }

.list-stack {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-width: 700px;
}

.list-item {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 12px 16px;
  border-radius: 16px;
  border: 1px solid rgba(148, 163, 184, 0.18);
  background: #fff;
  text-align: left;
  transition: all 0.2s ease;
  cursor: pointer;
}

.list-item:hover {
  border-color: #94a3b8;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.list-item.selected {
  border-color: #6366f1;
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1);
}

.td-id .index-badge {
  font-weight: 700;
  color: #6366f1;
  font-size: 13px;
  background: #e0e7ff;
  padding: 4px 8px;
  border-radius: 6px;
}

.td-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.td-info .info-text {
  display: flex;
  flex-direction: column;
}

.td-info strong {
  color: #0f172a;
  font-size: 14px;
  margin-bottom: 2px;
}

.td-info small, .td-tech small {
  color: #64748b;
  font-size: 12px;
}

.muted {
  color: #64748b;
}

.item-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  background: #e0f2fe;
  color: #0369a1;
}

.item-tag .status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

.item-tag.draft {
  background: #f1f5f9;
  color: #475569;
}
.item-tag.live {
  background: #dcfce7;
  color: #166534;
}
.item-tag.archived {
  background: #fee2e2;
  color: #991b1b;
}

.td-actions {
  display: flex;
  gap: 6px;
}

.action-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #475569;
  transition: all 0.2s ease;
}

.action-pill:hover {
  background: #f8fafc;
  color: #0f172a;
  border-color: #cbd5e1;
}

.view-pill:hover { color: #2563eb; border-color: #bfdbfe; background: #eff6ff; }
.edit-pill:hover { color: #16a34a; border-color: #bbf7d0; background: #f0fdf4; }
.delete-pill:hover { color: #dc2626; border-color: #fecaca; background: #fef2f2; }

.detail-panel {
  align-self: start;
}

/* ──────────────────────────────────────────────────
   Empty state
────────────────────────────────────────────────── */
.detail-empty {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: #94a3b8;
  text-align: center;
  padding: 40px 20px;
}
.detail-empty i {
  font-size: 40px;
  color: #cbd5e1;
}
.detail-empty p {
  margin: 0;
  font-size: 14px;
}

/* ──────────────────────────────────────────────────
   Home-page card mirror (hp-* classes)
────────────────────────────────────────────────── */
.hp-card {
  margin-top: 12px;
  border: 1px solid #f1f5f9;
  border-radius: 14px;
  overflow: hidden;
  background: #fff;
  transition: all 0.25s ease;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

.hp-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
  border-color: #e2e8f0;
}

/* Thumbnail */
.hp-thumb {
  height: 180px;
  position: relative;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-color: #e0e7ff;
}

/* Hover overlay – same as home page */
.hp-overlay {
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

.hp-card:hover .hp-overlay {
  opacity: 1;
}

.hp-action {
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

.hp-action:hover {
  background: #6366f1;
  color: #fff;
}

/* Status badge pinned top-right of image */
.hp-status-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  backdrop-filter: blur(8px);
  background: rgba(255,255,255,0.92);
  color: #475569;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
.hp-status-badge .status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #94a3b8;
}
.hp-status-badge.live { color: #166534; }
.hp-status-badge.live .status-dot { background: #22c55e; }
.hp-status-badge.draft { color: #475569; }
.hp-status-badge.draft .status-dot { background: #94a3b8; }
.hp-status-badge.archived { color: #991b1b; }
.hp-status-badge.archived .status-dot { background: #ef4444; }

/* Card body */
.hp-body {
  padding: 1rem 1.1rem 1.25rem;
}

.hp-tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.hp-tag {
  font-size: 0.65rem;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.06);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.hp-title {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 0.35rem;
}

.hp-desc {
  font-size: 0.83rem;
  color: #64748b;
  line-height: 1.55;
  margin: 0 0 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.hp-edit-row {
  display: flex;
  gap: 8px;
  padding-top: 0.75rem;
  border-top: 1px solid #f1f5f9;
}

.hp-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #475569;
  cursor: pointer;
  transition: all 0.2s ease;
}
.hp-edit:hover  { color: #16a34a; border-color: #bbf7d0; background: #f0fdf4; }
.hp-delete:hover { color: #dc2626; border-color: #fecaca; background: #fef2f2; }

.error-banner {
  margin: 1rem 0;
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid #fca5a5;
  background: #fef2f2;
  color: #991b1b;
  font-weight: 600;
}

.eyebrow {
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 12px;
  color: #6366f1;
  font-weight: 700;
}

.panel h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 800;
  color: #1e293b;
  letter-spacing: -0.5px;
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 20px;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(12px);
  z-index: 50;
}

.modal-card {
  width: min(580px, 100%);
  padding: 24px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
}

.modal-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
}

.modal-head h3 {
  margin: 0;
  font-size: 20px;
}

.modal-close {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #0f172a;
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
}

.modal-form {
  display: grid;
  gap: 14px;
}

.modal-actions {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

/* Multi-select Tags */
.multi-select-container {
  grid-column: 1 / -1;
  display: flex;
  flex-direction: column;
}
.input-label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}
.selected-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}
.chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 10px;
  background: #f1f5f9;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 600;
  color: #334155;
}
.remove-chip {
  background: none;
  border: none;
  color: #94a3b8;
  font-size: 16px;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}
.remove-chip:hover {
  color: #ef4444;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.18s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.image-upload-area {
  grid-column: 1 / -1;
}

.upload-box {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 160px;
  border: 2px dashed rgba(148, 163, 184, 0.4);
  border-radius: 14px;
  background: #f8fafc;
  cursor: pointer;
  transition: all 0.2s ease;
  overflow: hidden;
}

.upload-box:hover {
  border-color: #6366f1;
  background: #eff6ff;
}

.upload-box.has-image {
  border-style: solid;
  border-color: transparent;
  background: #e2e8f0;
}

.upload-box.is-uploading {
  pointer-events: none;
  opacity: 0.8;
}

.hidden-file-input {
  display: none;
}

.upload-state, .empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: #64748b;
}

.empty-state i {
  font-size: 32px;
  color: #94a3b8;
  margin-bottom: 4px;
}

.empty-state span {
  font-weight: 600;
  color: #334155;
}

.empty-state small {
  font-size: 12px;
}

.image-preview-wrapper {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.preview-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.change-overlay {
  position: absolute;
  inset: 0;
  background: rgba(15, 23, 42, 0.6);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #fff;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.upload-box:hover .change-overlay {
  opacity: 1;
}

.change-overlay i {
  font-size: 24px;
}

.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid rgba(99, 102, 241, 0.2);
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 900px) {
  .panel-layout {
    grid-template-columns: 1fr;
  }
  .panel-head, .form-grid, .modal-grid {
    flex-direction: column;
    grid-template-columns: 1fr;
  }
}
</style>
