<template>
  <section class="detail-section">
    <div class="container ">
      <div class="row">
        <div class="col-6">
          <div class="video-fram  rounded pt-4">
            <iframe
              width="100%"
              height="415"
              :src="videoSrc"
              :title="project ? project.title : 'Project video'"
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
              v-if="videoSrc"></iframe>
            <div v-else class="no-video">
              No video available for this project.
            </div>
          </div>
          <div class="card-body">
            <div class="title">
              <h3 class="card-title py-3  ">
                {{ project ? project.title : "Project" }}
              </h3>
              <p class="card-desc">{{ project ? project.desc : "" }}</p>
            </div>
          </div>
        </div>
        <div class="col-6">
          <div class="content border bg-white mt-4 py-3 rounded p-4">
            <h4 class="content-title text-center mb-3   ">Why show this detail ?</h4>
            <p class="card-text">
              This section is included to ensure transparency regarding the API's expiration. If the API expires, the website's functionality may be temporarily unavailable for testing. In that case, please refer to the YouTube video linked below to see how the project works.
            </p>
            <span class="fw-bold d-block mt-3">
                 Thank you for your interest in my portfolio and for taking the time to review my work!
            </span>
          </div>
          <div class="description-project border bg-white mt-4 py-3 rounded p-4">
              <h4 class="content-title"></h4>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
import { defineProps, onMounted, computed } from "vue";
import projects from "@/data/projects.js";

const props = defineProps({
  id: {
    type: [String, Number],
    required: true,
  },
});

const project = computed(() => {
  return projects.find((p) => String(p.id) === String(props.id));
});

const videoSrc = computed(() => {
  if (!project.value) return "";
  if (project.value.videoId) {
    return `https://www.youtube.com/embed/${project.value.videoId}`;
  }
  return project.value.liveLink || "";
});

onMounted(() => {
  console.log("detail id:", props.id);
});
</script>

<style scope>
.detail-section {
  margin-top: 65px;
  background-color: #f8f9fa;
  min-height: 100vh;
}
</style>
