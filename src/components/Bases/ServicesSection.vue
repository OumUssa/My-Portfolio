<template>
  <section id="services" class="services">
    <div class="container">
      <div class="section-header">
        <span class="label">What I Do</span>
        <h2 class="section-title">My Services</h2>
        <div class="title-line"></div>
      </div>

      <div class="services-grid">
        <div
          v-for="service in services"
          :key="service.title"
          class="service-card">
          <div class="service-icon">
            <i :class="service.icon"></i>
          </div>
          <h3>{{ service.title }}</h3>
          <p>{{ service.desc }}</p>
          <div class="card-accent"></div>
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
  background: #fff;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #6366f1;
  display: block;
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 1rem;
}

.title-line {
  width: 60px;
  height: 4px;
  background: #6366f1;
  border-radius: 2px;
  margin: 0 auto;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.service-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 2rem;
  position: relative;
  overflow: hidden;
  transition: all 0.35s ease;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.1);
  border-color: #c7d2fe;
}

.service-card:hover .card-accent {
  transform: scaleX(1);
}

.service-icon {
  width: 50px;
  height: 50px;
  background: #6366f1;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.2rem;
}

.service-icon i {
  font-size: 1.3rem;
  color: #fff;
}

.service-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.6rem;
}

.service-card p {
  font-size: 0.88rem;
  color: #64748b;
  line-height: 1.65;
  margin: 0;
}

.card-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #6366f1;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.35s ease;
}

@media (max-width: 992px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .services {
    padding: 4rem 1.5rem;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 2rem;
  }
}
</style>
