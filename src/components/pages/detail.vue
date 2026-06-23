<template>
  <section class="detail-section">
    <div class="container detail-container">
      <div v-if="loading" class="state-container">
        <div class="spinner"></div>
        <p>Loading project data...</p>
      </div>
      <div v-else-if="error" class="state-container error">
        <i class="bi bi-exclamation-circle" style="font-size: 2rem; margin-bottom: 8px;"></i>
        <p>{{ error }}</p>
      </div>
      <div v-else-if="project" class="detail-grid">
        <!-- Left Column: Visuals & Info -->
        <div class="main-content">
          <div class="media-frame">
            <iframe
              v-if="youtubeEmbedUrl"
              width="100%"
              height="100%"
              :src="youtubeEmbedUrl"
              title="YouTube video player"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen
              class="project-video"></iframe>
            <img
              v-else-if="project.image"
              :src="project.image"
              :alt="project.title"
              class="project-image" />
            <div v-else class="no-video">
              <i class="bi bi-image text-muted" style="font-size: 2rem;"></i>
              <p>No preview available for this project.</p>
            </div>
          </div>
          
          <div class="project-info">
            <h1 class="project-title">{{ project.title }}</h1>
            <p class="project-desc">{{ project.desc }}</p>
          </div>
        </div>

        <!-- Right Column: Meta & Links -->
        <div class="sidebar-content">
          <div class="meta-card">
            <h4 class="card-title">Project Details</h4>
            
            <div class="meta-item">
              <span class="meta-label">Admin</span>
              <span class="meta-value" style="display: flex; align-items: center; gap: 8px;">
                <div class="admin-avatar">
                  {{ project.adminName ? project.adminName.charAt(0).toUpperCase() : 'U' }}
                </div>
                {{ project.adminName || 'Unknown' }}
              </span>
            </div>
            
            <div class="meta-item">
              <span class="meta-label">Created</span>
              <span class="meta-value">{{ formattedDate }}</span>
            </div>
            
            <div class="meta-item">
              <span class="meta-label">Categories</span>
              <div class="tags-container">
                <span v-for="(tag, index) in project.tags" :key="index" class="custom-tag">
                  {{ tag.trim() }}
                </span>
              </div>
            </div>
          </div>

          <div class="meta-card">
            <h4 class="card-title">Project Links</h4>
            <div class="links-grid">
              <a
                v-if="project.openProject"
                :href="project.openProject"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link primary-link">
                <i class="bi bi-box-arrow-up-right"></i> Open Project
              </a>
              <a
                v-if="project.liveLink"
                :href="project.liveLink"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link"
                :class="youtubeEmbedUrl ? 'youtube-link' : 'live-link'">
                <i :class="youtubeEmbedUrl ? 'bi bi-youtube' : 'bi bi-play-circle'"></i>
                {{ youtubeEmbedUrl ? "Watch Video" : "Live Preview" }}
              </a>
              <a
                v-if="project.githubLink"
                :href="project.githubLink"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link github-link">
                <i class="bi bi-github"></i> Source Code
              </a>
            </div>
          </div>
          
          <div class="note-card">
            <i class="bi bi-info-circle info-icon"></i>
            <p>
              To manage cloud hosting costs, some of my live project servers may
              be inactive. For any project that is currently offline, I have
              provided a complete video demonstration and the GitHub repository.
            </p>
          </div>
        </div>
      </div>
      <div v-else class="state-container">
        <p>No project selected.</p>
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

const formattedDate = computed(() => {
  if (!project.value || !project.value.createdAt) return "N/A";
  try {
    const date = new Date(project.value.createdAt);
    if (isNaN(date.getTime())) return project.value.createdAt.split('T')[0];
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric"
    });
  } catch (e) {
    return project.value.createdAt.split('T')[0];
  }
});

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

<style scoped>
.detail-section {
  padding: 100px 20px 60px;
  background-color: #f8fafc;
  min-height: 100vh;
}

.detail-container {
  max-width: 1100px;
  margin: 0 auto;
}

.detail-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 32px;
  align-items: start;
}

.main-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.media-frame {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 16px;
  overflow: hidden;
  background: #e2e8f0;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-video,
.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.no-video {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: #64748b;
}

.project-info {
  background: #fff;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  border: 1px solid #f1f5f9;
}

.project-title {
  font-size: 28px;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 16px;
  letter-spacing: -0.5px;
}

.project-desc {
  font-size: 16px;
  line-height: 1.7;
  color: #475569;
  margin: 0;
  white-space: pre-wrap;
}

.sidebar-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.meta-card {
  background: #fff;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  border: 1px solid #f1f5f9;
}

.card-title {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f1f5f9;
}

.meta-item {
  margin-bottom: 16px;
}
.meta-item:last-child {
  margin-bottom: 0;
}

.meta-label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}

.meta-value {
  font-size: 15px;
  font-weight: 500;
  color: #334155;
}

.admin-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #eef2ff;
  color: #6366f1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.custom-tag {
  padding: 6px 12px;
  background: #eef2ff;
  color: #6366f1;
  font-size: 13px;
  font-weight: 600;
  border-radius: 8px;
  border: 1px solid #e0e7ff;
}

.links-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.project-link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.primary-link {
  background: #6366f1;
  color: #fff;
}
.primary-link:hover {
  background: #4f46e5;
  color: #fff;
  transform: translateY(-2px);
}

.youtube-link {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}
.youtube-link:hover {
  background: #fee2e2;
  color: #b91c1c;
}

.live-link {
  background: #f0fdf4;
  color: #16a34a;
  border: 1px solid #bbf7d0;
}
.live-link:hover {
  background: #dcfce7;
  color: #15803d;
}

.github-link {
  background: #f8fafc;
  color: #0f172a;
  border: 1px solid #e2e8f0;
}
.github-link:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
}

.note-card {
  background: #fff8f1;
  border: 1px solid #ffedd5;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.note-card .info-icon {
  font-size: 20px;
  color: #f97316;
  margin-top: 2px;
}
.note-card p {
  margin: 0;
  font-size: 14px;
  color: #9a3412;
  line-height: 1.6;
}

.state-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  color: #64748b;
  font-size: 16px;
}
.state-container.error {
  color: #ef4444;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e2e8f0;
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 992px) {
  .detail-grid {
    grid-template-columns: 1fr;
  }
}
</style>

