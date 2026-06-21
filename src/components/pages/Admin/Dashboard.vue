<template>
  <section class="overview-grid">
    <article class="overview-card">
      <p class="card-label">Projects</p>
      <h3>{{ projectCount }}</h3>
      <p>Search, add, edit, view details, and delete.</p>
    </article>

    <article class="overview-card">
      <p class="card-label">Tech Stacks</p>
      <h3>{{ categoryCount }}</h3>
      <p>Create and manage your tech stacks.</p>
    </article>

    <article class="overview-card">
      <p class="card-label">Status</p>
      <h3>Connected</h3>
      <p>Project and tech stack changes are saved and searchable.</p>
    </article>

    <article class="overview-card chart-card">
      <p class="card-label">Projects by Tech Stack</p>
      <div class="custom-chart-container" v-if="projectCount > 0">
        <div class="chart-bars">
          <div 
            v-for="item in chartData" 
            :key="item.label" 
            class="chart-bar-group"
          >
            <div class="chart-bar-wrapper">
              <div 
                class="chart-bar" 
                :style="{ height: item.percentage + '%' }"
                :title="item.label + ': ' + item.count + ' projects'"
              >
                <span class="bar-value">{{ item.count }}</span>
              </div>
            </div>
            <div class="chart-label">{{ item.label }}</div>
          </div>
        </div>
      </div>
      <div v-else class="no-data">No projects to display in chart.</div>
    </article>
  </section>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  projects: {
    type: Array,
    required: true,
  },
  categories: {
    type: Array,
    required: true,
  },
});

const projectCount = computed(() => props.projects.length);
const categoryCount = computed(() => props.categories.length);

const chartData = computed(() => {
  const categoryCounts = {};
  props.projects.forEach((p) => {
    const cat = p.category || "Uncategorized";
    categoryCounts[cat] = (categoryCounts[cat] || 0) + 1;
  });

  const labels = Object.keys(categoryCounts);
  if (labels.length === 0) return [];

  const maxCount = Math.max(...Object.values(categoryCounts));

  return labels.map(label => ({
    label,
    count: categoryCounts[label],
    percentage: maxCount > 0 ? (categoryCounts[label] / maxCount) * 100 : 0
  }));
});
</script>

<style scoped>
.overview-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.overview-card {
  padding: 24px;
  border-radius: 22px;
  background: #fff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.04);
}

.chart-card {
  grid-column: 1 / -1;
  height: 400px;
  display: flex;
  flex-direction: column;
}

.custom-chart-container {
  flex: 1;
  margin-top: 24px;
  display: flex;
  align-items: flex-end;
  padding-bottom: 10px;
  overflow-x: auto;
}

.chart-bars {
  display: flex;
  align-items: flex-end;
  gap: 32px;
  height: 100%;
  width: 100%;
  padding: 0 20px;
}

.chart-bar-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  height: 100%;
  min-width: 60px;
}

.chart-bar-wrapper {
  flex: 1;
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  background: #f8fafc;
  border-radius: 8px 8px 0 0;
  border-bottom: 1px solid #e2e8f0;
}

.chart-bar {
  width: 100%;
  max-width: 60px;
  background: linear-gradient(to top, #6366f1, #8b5cf6);
  border-radius: 6px 6px 0 0;
  position: relative;
  display: flex;
  justify-content: center;
  transition: height 0.5s ease-out;
}

.chart-bar:hover {
  background: linear-gradient(to top, #4f46e5, #7c3aed);
}

.bar-value {
  position: absolute;
  top: -24px;
  font-size: 13px;
  font-weight: 700;
  color: #1e293b;
}

.chart-label {
  margin-top: 12px;
  font-size: 12px;
  font-weight: 600;
  color: #64748b;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100px;
}

.no-data {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #64748b;
  font-style: italic;
}

.overview-card h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 800;
  color: #1e293b;
}

.overview-card p {
  margin: 0;
  color: #475569;
}

.card-label {
  display: block;
  margin-bottom: 6px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #6366f1;
  font-weight: 700;
}

@media (max-width: 900px) {
  .overview-grid {
    grid-template-columns: 1fr;
  }
}
</style>
