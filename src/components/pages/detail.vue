<template>
  <section class="detail-section">
    <div class="container">
      <div class="row">
        <div class="col-6">
          <div class="media-frame rounded pt-4">
            <iframe
              v-if="youtubeEmbedUrl"
              width="100%"
              height="415"
              :src="youtubeEmbedUrl"
              title="YouTube video player"
              frameborder="0"
              allow="
                accelerometer;
                autoplay;
                clipboard-write;
                encrypted-media;
                gyroscope;
                picture-in-picture;
                web-share;
              "
              referrerpolicy="strict-origin-when-cross-origin"
              allowfullscreen
              class="project-video"></iframe>
            <img
              v-else-if="project?.image"
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
            <h4 class="content-title text-center mb-3">
              A quick note on live demos:
            </h4>
            <p v-if="loading" class="card-text">Loading project data...</p>
            <p v-else-if="error" class="card-text text-danger">{{ error }}</p>
            <p class="card-text">
              To manage cloud hosting costs, some of my live project servers may
              be inactive. For any project that is currently offline, I have
              provided a complete YouTube video demonstration and the GitHub
              repository so you can still review the UI, features, and code.
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
            <div
              v-if="project"
              class="link-stack d-flex flex-column gap-3 mt-3">
              <a
                v-if="project.openProject"
                :href="project.openProject"
                target="_blank"
                rel="noopener noreferrer"
                class="d-flex align-items-center gap-2 text-decoration-none">
                <i class="bi bi-box-arrow-up-right text-primary"></i> Open
                project
              </a>
              <a
                v-if="project.liveLink"
                :href="project.liveLink"
                target="_blank"
                rel="noopener noreferrer"
                class="d-flex align-items-center gap-2 text-decoration-none">
                <i
                  :class="
                    youtubeEmbedUrl
                      ? 'bi bi-youtube text-danger'
                      : 'bi bi-play-circle text-info'
                  "></i>
                {{ youtubeEmbedUrl ? "Watch on YouTube" : "Live Preview" }}
              </a>
              <a
                v-if="project.githubLink"
                :href="project.githubLink"
                target="_blank"
                rel="noopener noreferrer"
                class="d-flex align-items-center gap-2 text-decoration-none">
                <i class="bi bi-github text-dark"></i> GitHub
              </a>
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

const youtubeEmbedUrl = computed(() => {
  if (!project.value?.liveLink) return null;
  const url = project.value.liveLink;

  if (url.includes("youtube.com/watch")) {
    try {
      const urlObj = new URL(url);
      const videoId = urlObj.searchParams.get("v");
      if (videoId) return `https://www.youtube.com/embed/${videoId}`;
    } catch (e) {
      return null;
    }
  } else if (url.includes("youtu.be/")) {
    const videoId = url.split("youtu.be/")[1]?.split("?")[0];
    if (videoId) return `https://www.youtube.com/embed/${videoId}`;
  }

  return null;
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

.project-video {
  width: 100%;
  border-radius: 0.5rem;
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
