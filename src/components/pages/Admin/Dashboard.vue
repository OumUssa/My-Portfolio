<template>
  <div class="dash">
    <!-- KPI cards -->
    <section class="kpi-grid">
      <article v-for="k in kpis" :key="k.label" class="kpi" :style="{ '--tone': k.tone, '--tone-soft': k.soft }">
        <div class="kpi-icon"><i :class="k.icon"></i></div>
        <div>
          <div class="kpi-label">{{ k.label }}</div>
          <div class="kpi-value">{{ k.value }}</div>
          <div class="kpi-hint">{{ k.hint }}</div>
        </div>
      </article>
    </section>

    <section class="chart-grid">
      <!-- Bar chart -->
      <article class="dx-card">
        <header class="card-head">
          <div>
            <div class="t">Projects by Tech Stack</div>
            <div class="s">How many projects use each tech stack</div>
          </div>
        </header>

        <div v-if="chartData.length" class="bars">
          <div class="y-grid">
            <div v-for="t in ticks" :key="t" class="y-line" :style="{ bottom: (t / maxValue) * 100 + '%' }">
              <span>{{ t }}</span>
            </div>
          </div>
          <div class="bar-row">
            <div v-for="item in chartData" :key="item.label" class="bar-col">
              <div class="bar-track">
                <div
                  class="bar"
                  :style="{ height: item.percentage + '%', background: item.color }"
                  :title="item.label + ': ' + item.count">
                  <span class="bar-value">{{ item.count }}</span>
                </div>
              </div>
              <span class="bar-label" :title="item.label">{{ item.label }}</span>
            </div>
          </div>
        </div>
        <div v-else class="empty">
          <i class="bi bi-bar-chart-line"></i>
          <div>No projects to display yet.</div>
        </div>
      </article>

      <!-- Donut chart -->
      <article class="dx-card">
        <header class="card-head">
          <div>
            <div class="t">Distribution</div>
            <div class="s">Share of projects per stack</div>
          </div>
        </header>

        <div v-if="chartData.length" class="donut-wrap">
          <svg viewBox="0 0 120 120" class="donut" role="img" aria-label="Projects distribution">
            <circle cx="60" cy="60" r="44" fill="none" stroke="var(--d-line)" stroke-width="16" />
            <circle
              v-for="seg in segments"
              :key="seg.label"
              cx="60" cy="60" r="44"
              fill="none"
              :stroke="seg.color"
              stroke-width="16"
              :stroke-dasharray="seg.dash"
              :stroke-dashoffset="seg.offset"
              transform="rotate(-90 60 60)"
              class="seg">
              <title>{{ seg.label }}: {{ seg.count }} ({{ seg.pct }}%)</title>
            </circle>
            <text x="60" y="57" text-anchor="middle" class="donut-num">{{ projectCount }}</text>
            <text x="60" y="72" text-anchor="middle" class="donut-sub">projects</text>
          </svg>

          <ul class="legend">
            <li v-for="seg in segments" :key="seg.label">
              <span class="dot" :style="{ background: seg.color }"></span>
              <span class="legend-name">{{ seg.label }}</span>
              <strong>{{ seg.pct }}%</strong>
            </li>
          </ul>
        </div>
        <div v-else class="empty">
          <i class="bi bi-pie-chart"></i>
          <div>No data yet.</div>
        </div>
      </article>
    </section>

    <!-- Recent projects -->
    <article class="dx-card">
      <header class="card-head">
        <div>
          <div class="t">Recent Projects</div>
          <div class="s">Your latest additions</div>
        </div>
      </header>

      <ul v-if="recent.length" class="recent">
        <li v-for="p in recent" :key="p.id">
          <div class="thumb">
            <img v-if="p.image" :src="p.image" :alt="p.title" loading="lazy" />
            <i v-else class="bi bi-folder2-open"></i>
          </div>
          <div class="recent-info">
            <strong>{{ p.title }}</strong>
            <span>{{ p.category || "General Stack" }}</span>
          </div>
          <span class="recent-date">{{ formatDate(p.createdAt) }}</span>
        </li>
      </ul>
      <div v-else class="empty">
        <i class="bi bi-folder-x"></i>
        <div>No projects yet. Add your first one from the Projects tab.</div>
      </div>
    </article>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  projects: { type: Array, required: true },
  categories: { type: Array, required: true },
});

const PALETTE = ["#6366f1", "#06b6d4", "#f59e0b", "#10b981", "#ec4899", "#8b5cf6", "#f97316", "#14b8a6"];

const projectCount = computed(() => props.projects.length);
const categoryCount = computed(() => props.categories.length);

const publishedCount = computed(
  () => props.projects.filter((p) => String(p.status || "").toLowerCase() === "published").length,
);

const kpis = computed(() => [
  {
    label: "Projects",
    value: projectCount.value,
    hint: "Total in portfolio",
    icon: "bi bi-folder-fill",
    tone: "#6366f1",
    soft: "#eef2ff",
  },
  {
    label: "Tech Stacks",
    value: categoryCount.value,
    hint: "Categories available",
    icon: "bi bi-layers-fill",
    tone: "#06b6d4",
    soft: "#ecfeff",
  },
  {
    label: "Published",
    value: publishedCount.value,
    hint: `${projectCount.value - publishedCount.value} draft / other`,
    icon: "bi bi-rocket-takeoff-fill",
    tone: "#10b981",
    soft: "#ecfdf5",
  },
  {
    label: "Status",
    value: "Online",
    hint: "API connected",
    icon: "bi bi-activity",
    tone: "#f59e0b",
    soft: "#fffbeb",
  },
]);

const chartData = computed(() => {
  const counts = {};
  props.projects.forEach((p) => {
    const cat = p.category || "Uncategorized";
    counts[cat] = (counts[cat] || 0) + 1;
  });

  const labels = Object.keys(counts);
  if (!labels.length) return [];
  const max = Math.max(...Object.values(counts));

  return labels.map((label, i) => ({
    label,
    count: counts[label],
    percentage: (counts[label] / max) * 100,
    color: PALETTE[i % PALETTE.length],
  }));
});

const maxValue = computed(() => Math.max(1, ...chartData.value.map((d) => d.count)));

const ticks = computed(() => {
  const max = maxValue.value;
  const step = Math.max(1, Math.ceil(max / 4));
  const list = [];
  for (let v = step; v <= max; v += step) list.push(v);
  return list;
});

const CIRC = 2 * Math.PI * 44;

const segments = computed(() => {
  const total = projectCount.value || 1;
  let acc = 0;
  return chartData.value.map((d) => {
    const frac = d.count / total;
    const len = frac * CIRC;
    const seg = {
      label: d.label,
      count: d.count,
      color: d.color,
      pct: Math.round(frac * 100),
      dash: `${Math.max(len - 2, 0)} ${CIRC - Math.max(len - 2, 0)}`,
      offset: -acc,
    };
    acc += len;
    return seg;
  });
});

const recent = computed(() =>
  [...props.projects]
    .sort((a, b) => String(b.createdAt).localeCompare(String(a.createdAt)))
    .slice(0, 5),
);

function formatDate(value) {
  if (!value) return "—";
  const d = new Date(value);
  return Number.isNaN(d.getTime())
    ? String(value)
    : d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}
</script>

<style scoped>
.dash {
  --d-text: #0f172a; --d-muted: #64748b; --d-faint: #94a3b8;
  --d-card: #ffffff; --d-border: #e8edf3; --d-line: #eef2f7; --d-icon-bg: #eef2ff;
  display: grid; gap: 20px;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}

.kpi {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  border-radius: 18px;
  background: var(--d-card);
  border: 1px solid var(--d-border);
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.kpi:hover { transform: translateY(-3px); box-shadow: 0 16px 36px rgba(15, 23, 42, 0.08); }

.kpi-icon {
  width: 52px;
  height: 52px;
  flex-shrink: 0;
  display: grid;
  place-items: center;
  border-radius: 14px;
  font-size: 22px;
  color: var(--tone);
  background: color-mix(in srgb, var(--tone) 14%, transparent);
}

.kpi-label {
  margin: 0;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--d-muted);
}

.kpi-value { margin: 2px 0; font-size: 28px; font-weight: 800; color: var(--d-text); line-height: 1.1; }
.kpi-hint { margin: 0; font-size: 12px; color: var(--d-faint); }

.chart-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr);
  gap: 16px;
}

.dx-card {
  padding: 22px;
  border-radius: 18px;
  background: var(--d-card);
  border: 1px solid var(--d-border);
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
}

.card-head { margin-bottom: 18px; }
.card-head .t { margin: 0; font-size: 16px; font-weight: 700; color: var(--d-text); }
.card-head .s { margin: 2px 0 0; font-size: 13px; color: var(--d-faint); }

/* Bar chart */
.bars { position: relative; height: 280px; padding-left: 28px; }
.y-grid { position: absolute; inset: 0 0 34px 28px; }
.y-line { position: absolute; left: 0; right: 0; border-top: 1px dashed var(--d-line); }
.y-line span { position: absolute; left: -28px; top: -8px; width: 22px; text-align: right; font-size: 11px; color: var(--d-faint); }

.bar-row {
  position: relative;
  height: 100%;
  display: flex;
  gap: 18px;
  align-items: stretch;
  overflow-x: auto;
}

.bar-col { flex: 1; min-width: 56px; display: flex; flex-direction: column; align-items: center; }
.bar-track { flex: 1; width: 100%; display: flex; align-items: flex-end; justify-content: center; padding-top: 22px; }

.bar {
  position: relative;
  width: 100%;
  max-width: 54px;
  min-height: 6px;
  border-radius: 10px 10px 4px 4px;
  transition: height 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.2s;
  animation: grow 0.7s cubic-bezier(0.2, 0.8, 0.2, 1);
  transform-origin: bottom;
}

.bar:hover { filter: brightness(1.08); }

@keyframes grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }

.bar-value { position: absolute; top: -22px; left: 0; right: 0; text-align: center; font-size: 12px; font-weight: 700; color: var(--d-text); }

.bar-label {
  height: 34px;
  padding-top: 10px;
  max-width: 90px;
  font-size: 12px;
  font-weight: 600;
  color: var(--d-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Donut */
.donut-wrap { display: grid; justify-items: center; gap: 18px; }
.donut { width: 190px; height: 190px; }
.seg { transition: stroke-width 0.2s; }
.seg:hover { stroke-width: 19; }
.donut-num { font-size: 22px; font-weight: 800; fill: var(--d-text); }
.donut-sub { font-size: 8px; fill: var(--d-faint); letter-spacing: 0.08em; text-transform: uppercase; }

.legend { list-style: none; margin: 0; padding: 0; width: 100%; display: grid; gap: 8px; }
.legend li { display: flex; align-items: center; gap: 10px; font-size: 13px; color: var(--d-muted); }
.legend-name { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.legend strong { color: var(--d-text); }
.dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }

/* Recent */
.recent { list-style: none; margin: 0; padding: 0; display: grid; }
.recent li {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 4px;
  border-bottom: 1px solid var(--d-line);
}
.recent li:last-child { border-bottom: 0; }

.thumb {
  width: 46px;
  height: 46px;
  flex-shrink: 0;
  border-radius: 12px;
  overflow: hidden;
  display: grid;
  place-items: center;
  background: var(--d-icon-bg);
  color: #6366f1;
  font-size: 20px;
}
.thumb img { width: 100%; height: 100%; object-fit: cover; }

.recent-info { flex: 1; min-width: 0; display: grid; }
.recent-info strong { font-size: 14px; color: var(--d-text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.recent-info span { font-size: 12px; color: var(--d-faint); }
.recent-date { font-size: 12px; color: var(--d-muted); white-space: nowrap; }

.empty { text-align: center; display: grid; justify-items: center; gap: 6px; padding: 40px 0; color: var(--d-faint); }
.empty i { font-size: 34px; color: var(--d-faint); }
.empty p { margin: 0; font-size: 14px; }

@media (max-width: 1100px) {
  .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .chart-grid { grid-template-columns: 1fr; }
}

@media (max-width: 560px) {
  .kpi-grid { grid-template-columns: 1fr; }
  .recent-date { display: none; }
}
</style>
