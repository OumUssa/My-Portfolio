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
          <div class="row-actions">
            <span class="item-tag">{{ project.status }}</span>
            <button
              class="icon-btn"
              type="button"
              title="Edit project"
              @click.stop="editProject(project)">
              <i class="bi bi-pencil-square"></i>
            </button>
            <button
              class="icon-btn danger-icon"
              type="button"
              title="Delete project"
              @click.stop="handleDeleteProject(project.id)">
              <i class="bi bi-trash3"></i>
            </button>
          </div>
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

      <div v-if="selectedProject" class="detail-box project-card-preview">
        <div class="project-preview-media">
          <img
            v-if="selectedProject.image"
            :src="selectedProject.image"
            :alt="selectedProject.title"
            class="project-preview-image" />
          <div v-else class="project-preview-empty">No image</div>
        </div>

        <div class="project-card-head">
          <strong>{{ selectedProject.title }}</strong>
          <span class="item-tag">{{ selectedProject.status }}</span>
        </div>

        <p class="project-card-desc">
          {{ selectedProject.description || "No description available." }}
        </p>

        <div class="project-meta-grid">
          <div class="meta-chip">
            <small>Tech Stack</small>
            <strong>{{ selectedProject.category || "-" }}</strong>
          </div>
          <div class="meta-chip">
            <small>Tech Details</small>
            <strong>{{ selectedProject.tech || "-" }}</strong>
          </div>
        </div>

        <div class="project-links-row" style="display: flex; gap: 8px; flex-wrap: wrap;">
          <a
            v-if="selectedProject.openProject"
            class="project-link"
            :href="selectedProject.openProject"
            target="_blank"
            rel="noopener noreferrer">
            <i class="bi bi-box-arrow-up-right"></i>
            Open project
          </a>
          <a
            v-if="selectedProject.link"
            class="project-link"
            :href="selectedProject.link"
            target="_blank"
            rel="noopener noreferrer">
            <i class="bi bi-play-circle"></i>
            Preview
          </a>
          <a
            v-if="selectedProject.githubLink"
            class="project-link"
            :href="selectedProject.githubLink"
            target="_blank"
            rel="noopener noreferrer">
            <i class="bi bi-github"></i>
            GitHub
          </a>
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
  transition: border-color 0.2s, box-shadow 0.2s;
  cursor: pointer;
}

.list-item.selected {
  border-color: #6366f1;
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1);
}

.list-item:hover {
  border-color: #94a3b8;
}

.list-item strong {
  display: block;
  margin-bottom: 4px;
  color: #0f172a;
}

.list-item small, .muted {
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

.row-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

.icon-btn {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #0f172a;
  transition: all 0.2s ease;
}

.icon-btn:hover {
  transform: translateY(-2px);
  border-color: #c7d2fe;
  color: #6366f1;
}

.danger-icon {
  color: #b91c1c;
  border-color: #fecaca;
  background: #fff5f5;
}

.danger-icon:hover {
  color: #991b1b;
  border-color: #fca5a5;
  background: #fff1f2;
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

.project-card-preview {
  display: grid;
  gap: 14px;
}

.project-preview-media {
  width: 100%;
  height: 170px;
  border-radius: 14px;
  overflow: hidden;
  background: #e2e8f0;
}

.project-preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-preview-empty {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
  font-size: 13px;
  color: #64748b;
}

.project-card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.project-card-head strong {
  font-size: 1rem;
  color: #0f172a;
}

.project-card-desc {
  margin: 0;
  color: #475569;
  line-height: 1.6;
}

.project-meta-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}

.meta-chip {
  padding: 10px 12px;
  border-radius: 12px;
  background: #fff;
  border: 1px solid rgba(148, 163, 184, 0.18);
  display: grid;
  gap: 6px;
}

.meta-chip small {
  text-transform: uppercase;
  font-size: 11px;
  color: #64748b;
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  padding: 9px 12px;
  border-radius: 10px;
  border: 1px solid #c7d2fe;
  background: #fff;
  color: #2563eb;
  font-size: 13px;
  font-weight: 600;
}

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
