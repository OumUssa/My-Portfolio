<template>
  <section class="panel-layout">
    <div class="panel">
      <div class="panel-head">
        <div>
          <p class="eyebrow">Tech Stacks</p>
          <h3>Tech stack list</h3>
        </div>
        <div class="panel-actions">
          <input
            v-model="categorySearch"
            class="search"
            type="search"
            placeholder="Search tech stacks" />
          <button
            class="primary"
            type="button"
            @click="openAddCategoryModal">
            <i class="bi bi-plus-lg"></i>
            Add tech stack
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
          </div>
          <div class="row-actions">
            <span class="item-tag">{{ category.items }} items</span>
            <button
              class="icon-btn"
              type="button"
              title="Edit tech stack"
              @click.stop="editCategory(category)">
              <i class="bi bi-pencil-square"></i>
            </button>
            <button
              class="icon-btn danger-icon"
              type="button"
              title="Delete tech stack"
              @click.stop="handleDeleteCategory(category.id)">
              <i class="bi bi-trash3"></i>
            </button>
          </div>
        </button>
      </div>
    </div>

    <teleport to="body">
      <transition name="fade">
        <div v-if="isModalOpen" class="modal-backdrop" @click.self="closeModal">
          <div class="modal-card">
            <div class="modal-head">
              <div>
                <p class="eyebrow">Tech Stacks</p>
                <h3>{{ editingCategoryId ? "Edit tech stack" : "Add new tech stack" }}</h3>
              </div>
              <button class="modal-close" type="button" @click="closeModal">
                ×
              </button>
            </div>

            <p v-if="loadError" class="error-banner">{{ loadError }}</p>

            <div class="modal-form">
              <div class="form-grid modal-grid">
                <input
                  v-model="categoryForm.name"
                  type="text"
                  placeholder="Tech stack name" />
              </div>

              <div class="form-actions modal-actions">
                <button class="primary" @click="saveCategory">
                  {{ editingCategoryId ? "Update tech stack" : "Add tech stack" }}
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
import { createCategory, updateCategory as updateCategoryRequest, deleteCategory as deleteCategoryRequest } from "@/data/categoriesApi.js";
import { buildCategoryList } from "@/data/adminContent.js";

const props = defineProps({
  categories: {
    type: Array,
    required: true,
  },
  projects: {
    type: Array,
    required: true,
  },
  token: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(["update:categories", "update:projects"]);

const categorySearch = ref("");
const selectedCategory = ref(null);
const isModalOpen = ref(false);
const editingCategoryId = ref(null);
const loadError = ref("");

const categoryForm = ref({
  name: "",
});

watch(() => props.categories, (newCategories) => {
  if (!selectedCategory.value || !newCategories.find(c => c.id === selectedCategory.value.id)) {
    selectedCategory.value = newCategories[0] || null;
  } else {
    selectedCategory.value = newCategories.find(c => c.id === selectedCategory.value.id);
  }
}, { immediate: true });

const filteredCategories = computed(() => {
  const keyword = categorySearch.value.trim().toLowerCase();
  if (!keyword) return props.categories;
  return props.categories.filter((category) =>
    [category.name].join(" ").toLowerCase().includes(keyword),
  );
});

function normalizeCategoryName(value) {
  return String(value || "General Stack").trim() || "General Stack";
}

function resetCategoryForm() {
  editingCategoryId.value = null;
  categoryForm.value = { name: "" };
  loadError.value = "";
}

function openAddCategoryModal() {
  resetCategoryForm();
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
}

function selectCategory(category) {
  selectedCategory.value = category;
}

function editCategory(category) {
  editingCategoryId.value = category.id;
  categoryForm.value = { name: category.name };
  isModalOpen.value = true;
}

async function saveCategory() {
  loadError.value = "";
  try {
    const nextName = normalizeCategoryName(categoryForm.value.name);
    const existingCategory = props.categories.find(c => c.id === editingCategoryId.value);
    
    const nextCategories = editingCategoryId.value
      ? props.categories.map((c) => (c.id === editingCategoryId.value ? null : c)).filter(Boolean)
      : [...props.categories];

    const payload = {
      id: editingCategoryId.value || Date.now(),
      name: nextName,
      items: existingCategory?.items || 0,
      createdAt: existingCategory?.createdAt || new Date().toISOString().slice(0, 10),
    };

    if (!props.token) {
      loadError.value = "Missing admin token. Please login again.";
      return;
    }

    let nextProjects = [...props.projects];

    if (editingCategoryId.value) {
      const updatedCategory = await updateCategoryRequest(editingCategoryId.value, {
        name: nextName,
        token: props.token,
      });
      const previousName = existingCategory?.name || nextName;
      payload.id = updatedCategory.id || payload.id;
      payload.name = updatedCategory.name || payload.name;
      payload.createdAt = updatedCategory.createdAt || payload.createdAt;

      nextProjects = props.projects.map((project) =>
        project.category === previousName
          ? {
              ...project,
              category: payload.name,
              categories: [payload.name],
              tags: project.tags?.length ? project.tags : [payload.name],
            }
          : project,
      );

      nextCategories.push(payload);
    } else {
      const createdCategory = await createCategory({
        name: nextName,
        token: props.token,
      });
      payload.id = createdCategory.id || payload.id;
      payload.createdAt = createdCategory.createdAt || payload.createdAt;
      nextCategories.unshift(payload);
    }

    const builtCategories = buildCategoryList(nextProjects, [], nextCategories);
    
    emit("update:projects", nextProjects);
    emit("update:categories", builtCategories);

    selectedCategory.value = payload;
    closeModal();
  } catch (error) {
    loadError.value = error instanceof Error ? error.message : "Failed to save tech stack.";
  }
}

async function handleDeleteCategory(categoryId) {
  if (!confirm("Are you sure you want to delete this tech stack?")) return;
  
  loadError.value = "";
  const categoryToDelete = props.categories.find((c) => c.id === categoryId);
  if (!categoryToDelete) return;

  try {
    if (!props.token) {
      alert("Missing admin token. Please login again.");
      return;
    }

    await deleteCategoryRequest(categoryId, props.token);

    const nextProjects = props.projects.map((project) =>
      project.category === categoryToDelete.name
        ? {
            ...project,
            category: "",
            categories: [],
            tags: [],
          }
        : project,
    );

    const nextCategories = props.categories.filter((c) => c.id !== categoryId);
    const builtCategories = buildCategoryList(nextProjects, [], nextCategories);

    emit("update:projects", nextProjects);
    emit("update:categories", builtCategories);
  } catch (error) {
    alert(error instanceof Error ? error.message : "Failed to delete tech stack.");
  }
}
</script>

<style scoped>
/* Inherit common panel styles */
.panel-layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
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

.search, .form-grid input {
  width: 100%;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background: #fff;
  color: #0f172a;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
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
  width: min(500px, 100%);
  padding: 32px;
  border-radius: 24px;
  background: #fff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
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
  font-size: 20px;
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
  cursor: pointer;
}

.modal-form {
  display: grid;
  gap: 16px;
}

.modal-actions {
  display: flex;
  gap: 10px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.18s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
