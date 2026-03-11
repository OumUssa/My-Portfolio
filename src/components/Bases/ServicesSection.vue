<template>
  <section id="services" class="services">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">What I Do</span>
        <h2 class="section-title">My Services</h2>
      </div>

      <div class="grid">
        <div v-for="service in services" :key="service.title" class="card">
          <div class="card-icon">
            <i :class="service.icon"></i>
          </div>
          <h3>{{ service.title }}</h3>
          <p>{{ service.desc }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  {
    icon: "bi bi-laptop",
    title: "Web Development",
    desc: "Building responsive, fast, and modern websites using the latest technologies and best practices.",
  },
  {
    icon: "bi bi-phone",
    title: "Responsive Design",
    desc: "Creating beautiful layouts that adapt perfectly to any device — desktop, tablet, or mobile.",
  },
  {
    icon: "bi bi-palette",
    title: "UI/UX Design",
    desc: "Designing intuitive and visually appealing interfaces that prioritize user experience.",
  },
  {
    icon: "bi bi-gear",
    title: "Backend Development",
    desc: "Building secure and scalable server-side applications with robust APIs and databases.",
  },
  {
    icon: "bi bi-speedometer2",
    title: "Performance",
    desc: "Optimizing websites for speed, accessibility, and search engine visibility.",
  },
  {
    icon: "bi bi-shield-check",
    title: "Maintenance & Support",
    desc: "Providing ongoing support, bug fixes, and feature updates to keep your project running smoothly.",
  },
];
</script>

<style scoped>
.services {
  padding: 6rem 2rem;
  background: #f8fafc;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-head {
  text-align: center;
  margin-bottom: 3rem;
}

.section-tag {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #6366f1;
}

.section-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #1e293b;
  margin-top: 0.35rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.card {
  background: #fff;
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  padding: 1.75rem;
  transition: all 0.25s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  border-color: #e2e8f0;
}

.card-icon {
  width: 44px;
  height: 44px;
  background: rgba(99, 102, 241, 0.08);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.card-icon i {
  font-size: 1.15rem;
  color: #6366f1;
}

.card h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 0.85rem;
  color: #64748b;
  line-height: 1.6;
  margin: 0;
}

@media (max-width: 992px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
  .services { padding: 4rem 1.5rem; }
  .grid { grid-template-columns: 1fr; }
  .section-title { font-size: 1.8rem; }
}
</style>
