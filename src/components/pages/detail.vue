<template>
  <section class="detail-section">
    <div class="container">
      <div class="row">
        <div class="col-6">
          <div class="media-frame rounded pt-4">
            <img
              v-if="project?.image"
              :src="project.image"
              :alt="project.title"
              class="project-image" />
            <div v-else class="no-video">
              No preview available for this project.
            </div>
          </div>
          <div class="card-body">
            <div class="title">
              <h3 class="card-title py-3">
                {{
                  project ? project.title : loading ? "Loading..." : "Project"
                }}
              </h3>
              <p class="card-desc">{{ project ? project.desc : "" }}</p>
            </div>
          </div>
        </div>
        <div class="col-6">
          <div class="content border bg-white mt-4 py-3 rounded p-4">
            <h4 class="content-title text-center mb-3">Project details</h4>
            <p v-if="loading" class="card-text">Loading project data...</p>
            <p v-else-if="error" class="card-text text-danger">{{ error }}</p>
            <p class="card-text">
              {{
                project
                  ? project.desc
                  : "Select a project to see the full API response."
              }}
            </p>
            <div v-if="project" class="project-meta mt-3">
              <p><strong>Admin:</strong> {{ project.adminName }}</p>
              <p><strong>Categories:</strong> {{ project.tags.join(", ") }}</p>
              <p><strong>Created:</strong> {{ project.createdAt }}</p>
            </div>
            <span class="fw-bold d-block mt-3">
              Thank you for your interest in my portfolio and for taking the
              time to review my work!
            </span>
          </div>
          <div
            class="description-project border bg-white mt-4 py-3 rounded p-4">
            <h4 class="content-title">Links</h4>
            <div v-if="project" class="link-stack">
              <a
                v-if="project.liveLink"
                :href="project.liveLink"
                target="_blank"
                rel="noopener noreferrer"
                >Open project</a
              >
              <a
                v-if="project.githubLink"
                :href="project.githubLink"
                target="_blank"
                rel="noopener noreferrer"
                >GitHub</a
              >
            </div>
            <p v-else class="card-text">No project selected.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { computed, defineProps, onMounted, ref, watch } from "vue";
import { fetchProjects } from "@/data/projectsApi.js";

const props = defineProps({
  id: {
    type: [String, Number],
    required: true,
  },
});

const projects = ref([]);
const loading = ref(true);
const error = ref("");

const project = computed(() =>
  projects.value.find((item) => String(item.id) === String(props.id)),
);

async function loadProjects() {
  loading.value = true;
  error.value = "";

  try {
    projects.value = await fetchProjects();
  } catch (fetchError) {
    error.value =
      fetchError instanceof Error
        ? fetchError.message
        : "Failed to load project.";
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  loadProjects();
});

watch(
  () => props.id,
  () => {
    if (projects.value.length) {
      return;
    }

    loadProjects();
  },
);
</script>

<style scope>
.detail-section {
  margin-top: 65px;
  background-color: #f8f9fa;
  min-height: 100vh;
}

.media-frame {
  min-height: 415px;
  background: #fff;
}

.project-image {
  width: 100%;
  max-height: 415px;
  object-fit: cover;
  border-radius: 0.5rem;
}

.link-stack {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>
