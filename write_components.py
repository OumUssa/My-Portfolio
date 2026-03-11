import os

base = r'd:\c++\my-portfolio\my-portfolio\src'

# ============================================================
# ProjectsSection.vue
# ============================================================
projects_vue = r'''<template>
  <section id="projects" class="projects">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">My Work</span>
        <h2 class="section-title">Recent Projects</h2>
      </div>

      <div class="filter-bar">
        <button
          v-for="tab in tabs"
          :key="tab"
          class="filter-btn"
          :class="{ active: activeTab === tab }"
          @click="activeTab = tab">
          {{ tab }}
        </button>
      </div>

      <div class="grid">
        <transition-group name="fade">
          <div
            v-for="project in filteredProjects"
            :key="project.title"
            class="card">
            <div
              class="card-thumb"
              :style="{
                backgroundImage: project.image
                  ? 'url(' + project.image + ')'
                  : 'linear-gradient(135deg, ' + project.color + ', ' + project.color + ')',
              }">
              <div class="card-overlay">
                <a :href="project.liveLink" target="_blank" rel="noopener noreferrer" class="card-action">
                  <i class="bi bi-eye"></i>
                </a>
                <a :href="project.githubLink" target="_blank" rel="noopener noreferrer" class="card-action">
                  <i class="bi bi-github"></i>
                </a>
              </div>
            </div>
            <div class="card-body">
              <div class="card-tags">
                <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
              <h3 class="card-title">{{ project.title }}</h3>
              <p class="card-desc">{{ project.desc }}</p>
            </div>
          </div>
        </transition-group>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from "vue";
import worksyncImage from "@/assets/Worksync.png";

const tabs = ["All", "Web App", "Landing Page", "Dashboard"];
const activeTab = ref("All");

const projects = [
  {
    title: "WorkSync",
    desc: "A freelance marketplace for seamless collaboration between clients and freelancers.",
    tags: ["Vue.js", "HTML5", "CSS3", "API", "JavaScript"],
    category: "Web App",
    color: "#6366f1",
    image: worksyncImage,
    liveLink: "https://worksync-eta.vercel.app/",
    githubLink: "https://github.com/horsenghab/freelancer-ant-g2",
  },
  {
    title: "Portfolio Website",
    desc: "A clean, responsive personal portfolio with smooth animations.",
    tags: ["Vue.js", "CSS3"],
    category: "Landing Page",
    color: "#ec4899",
    image: "https://via.placeholder.com/400x300?text=Portfolio",
    liveLink: "https://your-portfolio.com/",
    githubLink: "https://github.com/yourname/portfolio",
  },
  {
    title: "Task Management App",
    desc: "A productivity tool with drag-and-drop, real-time updates, and team collaboration.",
    tags: ["Vue.js", "Firebase"],
    category: "Web App",
    color: "#0ea5e9",
    image: "https://via.placeholder.com/400x300?text=Task+App",
    liveLink: "https://task-management-app.com/",
    githubLink: "https://github.com/yourname/task-app",
  },
  {
    title: "Analytics Dashboard",
    desc: "A data visualization dashboard with charts, filters, and export features.",
    tags: ["Vue.js", "Chart.js"],
    category: "Dashboard",
    color: "#10b981",
    image: "https://via.placeholder.com/400x300?text=Analytics",
    liveLink: "https://analytics-dashboard.com/",
    githubLink: "https://github.com/yourname/analytics-dashboard",
  },
  {
    title: "Restaurant Landing Page",
    desc: "A beautiful restaurant site with menu, reservations, and gallery.",
    tags: ["HTML", "CSS", "JavaScript"],
    category: "Landing Page",
    color: "#f43f5e",
    image: "https://via.placeholder.com/400x300?text=Restaurant",
    liveLink: "https://restaurant-landing.com/",
    githubLink: "https://github.com/yourname/restaurant-site",
  },
  {
    title: "Admin Panel",
    desc: "A feature-rich admin dashboard with user management and analytics.",
    tags: ["Vue.js", "Tailwind"],
    category: "Dashboard",
    color: "#a78bfa",
    image: "https://via.placeholder.com/400x300?text=Admin+Panel",
    liveLink: "https://admin-panel-demo.com/",
    githubLink: "https://github.com/yourname/admin-panel",
  },
];

const filteredProjects = computed(() => {
  if (activeTab.value === "All") return projects;
  return projects.filter((p) => p.category === activeTab.value);
});
</script>

<style scoped>
.projects {
  padding: 6rem 2rem;
  background: #fff;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.section-head {
  text-align: center;
  margin-bottom: 2.5rem;
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

.filter-bar {
  display: flex;
  justify-content: center;
  gap: 0.4rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.45rem 1.1rem;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  background: transparent;
  color: #64748b;
  font-size: 0.82rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  border-color: #c7d2fe;
  color: #6366f1;
}

.filter-btn.active {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.card {
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
  transition: all 0.25s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.06);
  border-color: #e2e8f0;
}

.card-thumb {
  height: 190px;
  position: relative;
  overflow: hidden;
  background-size: cover;
  background-position: center;
}

.card-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  opacity: 0;
  transition: opacity 0.25s ease;
}

.card:hover .card-overlay {
  opacity: 1;
}

.card-action {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 50%;
  color: #1e293b;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.card-action:hover {
  background: #6366f1;
  color: #fff;
}

.card-body {
  padding: 1.15rem 1.25rem 1.35rem;
}

.card-tags {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}

.tag {
  font-size: 0.65rem;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.06);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.card-title {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.35rem;
}

.card-desc {
  font-size: 0.83rem;
  color: #64748b;
  line-height: 1.5;
  margin: 0;
}

.fade-enter-active { transition: all 0.3s ease; }
.fade-leave-active { transition: all 0.2s ease; position: absolute; }
.fade-enter-from { opacity: 0; transform: translateY(12px); }
.fade-leave-to { opacity: 0; }

@media (max-width: 992px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
  .projects { padding: 4rem 1.5rem; }
  .grid { grid-template-columns: 1fr; }
  .section-title { font-size: 1.8rem; }
}
</style>
'''

# ============================================================
# ServicesSection.vue
# ============================================================
services_vue = r'''<template>
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
'''

# ============================================================
# ContactSection.vue
# ============================================================
contact_vue = r'''<template>
  <section id="contact" class="contact">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Get In Touch</span>
        <h2 class="section-title">Let's Work Together</h2>
        <p class="section-desc">
          Have a project in mind or just want to say hello? I'd love to hear from you.
        </p>
      </div>

      <div class="contact-grid">
        <div class="info-panel">
          <h3>Contact Information</h3>
          <p class="info-desc">Fill up the form and I'll get back to you within 24 hours.</p>

          <div class="info-list">
            <a href="mailto:oumussa719@gmail.com" class="info-item">
              <i class="bi bi-envelope"></i>
              <div>
                <span class="info-label">Email</span>
                <span class="info-value">oumussa719@gmail.com</span>
              </div>
            </a>
            <a href="tel:+1234567890" class="info-item">
              <i class="bi bi-telephone"></i>
              <div>
                <span class="info-label">Phone</span>
                <span class="info-value">+1 234 567 890</span>
              </div>
            </a>
            <div class="info-item">
              <i class="bi bi-geo-alt"></i>
              <div>
                <span class="info-label">Location</span>
                <span class="info-value">Your City, Country</span>
              </div>
            </div>
          </div>

          <div class="social-row">
            <a href="#" aria-label="GitHub"><i class="bi bi-github"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
            <a href="#" aria-label="Twitter"><i class="bi bi-twitter-x"></i></a>
            <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
          </div>
        </div>

        <form class="form-panel" @submit.prevent="sendEmail">
          <Transition name="slide">
            <div v-if="statusMsg" class="status" :class="statusType">
              <i :class="statusType === 'success' ? 'bi bi-check-circle-fill' : 'bi bi-exclamation-circle-fill'"></i>
              {{ statusMsg }}
            </div>
          </Transition>

          <div class="form-row">
            <div class="field">
              <label for="c-name">Your Name</label>
              <input id="c-name" v-model="form.name" type="text" placeholder="John Doe" required />
            </div>
            <div class="field">
              <label for="c-email">Your Email</label>
              <input id="c-email" v-model="form.email" type="email" placeholder="john@email.com" required />
            </div>
          </div>
          <div class="field">
            <label for="c-subject">Subject</label>
            <input id="c-subject" v-model="form.subject" type="text" placeholder="Project Inquiry" required />
          </div>
          <div class="field">
            <label for="c-message">Message</label>
            <textarea id="c-message" v-model="form.message" rows="5" placeholder="Tell me about your project..." required></textarea>
          </div>

          <button type="submit" class="submit-btn" :disabled="loading">
            {{ loading ? "Sending..." : "Send Message" }}
            <i :class="loading ? 'bi bi-arrow-repeat spin' : 'bi bi-arrow-right'"></i>
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from "vue";

const loading = ref(false);
const statusMsg = ref("");
const statusType = ref("");

const form = reactive({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const sendEmail = async () => {
  if (!form.name || !form.email || !form.subject || !form.message) {
    statusMsg.value = "Please fill in all fields.";
    statusType.value = "error";
    return;
  }

  loading.value = true;
  statusMsg.value = "";

  try {
    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        access_key: "YOUR_ACCESS_KEY",
        name: form.name,
        email: form.email,
        subject: form.subject,
        message: form.message,
        to: "oumussa719@gmail.com",
      }),
    });

    const data = await response.json();

    if (data.success) {
      statusMsg.value = "Message sent successfully! I'll get back to you soon.";
      statusType.value = "success";
      form.name = "";
      form.email = "";
      form.subject = "";
      form.message = "";
    } else {
      throw new Error("Failed");
    }
  } catch {
    const mailtoLink = `mailto:oumussa719@gmail.com?subject=${encodeURIComponent(form.subject)}&body=${encodeURIComponent(`Name: ${form.name}\nEmail: ${form.email}\n\n${form.message}`)}`;
    window.open(mailtoLink, "_blank");
    statusMsg.value = "Opening your email client as fallback...";
    statusType.value = "success";
  } finally {
    loading.value = false;
    setTimeout(() => { statusMsg.value = ""; }, 6000);
  }
};
</script>

<style scoped>
.contact {
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
  margin-bottom: 0.5rem;
}

.section-desc {
  font-size: 0.95rem;
  color: #64748b;
  max-width: 460px;
  margin: 0 auto;
  line-height: 1.6;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
  background: #fff;
}

/* Info Panel */
.info-panel {
  background: #0a0a1a;
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
}

.info-panel h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
}

.info-desc {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.45);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: auto;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.75rem;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  text-decoration: none;
  transition: background 0.2s ease;
}

.info-item:hover {
  background: rgba(255, 255, 255, 0.08);
}

.info-item i {
  font-size: 1rem;
  color: #818cf8;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.15);
  border-radius: 8px;
  flex-shrink: 0;
}

.info-label {
  display: block;
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.35);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.info-value {
  display: block;
  font-size: 0.85rem;
  color: #fff;
  font-weight: 500;
}

.social-row {
  display: flex;
  gap: 0.5rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.social-row a {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.social-row a:hover {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

/* Form Panel */
.form-panel {
  padding: 2.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.field {
  margin-bottom: 1.25rem;
}

.field label {
  display: block;
  font-size: 0.75rem;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 0.4rem;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.field input,
.field textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.88rem;
  color: #1e293b;
  background: #f8fafc;
  transition: all 0.2s ease;
  font-family: inherit;
  outline: none;
}

.field input::placeholder,
.field textarea::placeholder {
  color: #cbd5e1;
}

.field input:focus,
.field textarea:focus {
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.06);
}

.field textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6366f1;
  color: #fff;
  font-size: 0.88rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.submit-btn:hover:not(:disabled) {
  background: #4f46e5;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1.25rem;
}

.status.success {
  background: #ecfdf5;
  color: #059669;
  border: 1px solid #a7f3d0;
}

.status.error {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

.slide-enter-active { transition: all 0.3s ease; }
.slide-leave-active { transition: all 0.2s ease; }
.slide-enter-from { opacity: 0; transform: translateY(-8px); }
.slide-leave-to { opacity: 0; }

@media (max-width: 900px) {
  .contact-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  .contact { padding: 4rem 1.5rem; }
  .section-title { font-size: 1.8rem; }
  .form-row { grid-template-columns: 1fr; }
  .form-panel { padding: 2rem 1.5rem; }
  .info-panel { padding: 2rem 1.5rem; }
}
</style>
'''

# ============================================================
# AboutSection.vue
# ============================================================
about_vue = r'''<template>
  <section class="about-hero">
    <div class="about-hero-bg"></div>
    <div class="about-hero-inner">
      <span class="about-tag">About Me</span>
      <h1 class="about-heading">Know Me Better</h1>
    </div>
  </section>

  <section class="profile">
    <div class="container">
      <div class="profile-card">
        <div class="profile-img-wrap">
          <img :src="profileImage" alt="Profile Photo" class="profile-img" />
        </div>
        <div class="profile-info">
          <h2>Hi, I'm <span class="accent">Oum Ussa</span></h2>
          <p class="role">Full-Stack Developer</p>
          <p class="bio">
            I'm a passionate full-stack developer with a love for creating
            beautiful, functional, and user-friendly websites. I specialize in
            building modern web applications with the latest technologies.
          </p>
          <p class="bio">
            With a strong foundation in both front-end and back-end development,
            I bring ideas to life through clean code and thoughtful design decisions.
          </p>
          <div class="info-grid">
            <div class="info-item">
              <i class="bi bi-person"></i>
              <div>
                <span class="info-label">Name</span>
                <span class="info-val">Oum Ussa</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-envelope"></i>
              <div>
                <span class="info-label">Email</span>
                <span class="info-val">oumussa719@gmail.com</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-geo-alt"></i>
              <div>
                <span class="info-label">Location</span>
                <span class="info-val">Your City, Country</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-calendar3"></i>
              <div>
                <span class="info-label">Experience</span>
                <span class="info-val">1+ Years</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="skills">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">My Expertise</span>
        <h2 class="section-title">Skills & Technologies</h2>
      </div>
      <div class="skills-grid">
        <div v-for="skill in skills" :key="skill.name" class="skill-item">
          <div class="skill-icon">
            <i :class="skill.icon"></i>
          </div>
          <span class="skill-name">{{ skill.name }}</span>
          <div class="skill-bar">
            <div class="skill-fill" :style="{ width: skill.level }"></div>
          </div>
          <span class="skill-pct">{{ skill.level }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const profileImage = ref(
  "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=face",
);

const skills = [
  { name: "HTML5", icon: "bi bi-filetype-html", level: "95%" },
  { name: "CSS3", icon: "bi bi-filetype-css", level: "90%" },
  { name: "JavaScript", icon: "bi bi-filetype-js", level: "85%" },
  { name: "Vue.js", icon: "bi bi-braces", level: "80%" },
  { name: "Node.js", icon: "bi bi-hdd-stack", level: "75%" },
  { name: "Git", icon: "bi bi-git", level: "85%" },
];
</script>

<style scoped>
/* Hero */
.about-hero {
  position: relative;
  background: #0a0a1a;
  padding: 9rem 2rem 7rem;
  text-align: center;
  overflow: hidden;
}

.about-hero-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 30% 60%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 70% 30%, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
}

.about-hero-inner {
  position: relative;
  z-index: 1;
}

.about-tag {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: rgba(255, 255, 255, 0.6);
  display: block;
  margin-bottom: 0.75rem;
}

.about-heading {
  font-size: 3rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.5px;
}

/* Profile */
.profile {
  padding: 0 2rem 4rem;
  background: #f8fafc;
  margin-top: -4rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.profile-card {
  background: #fff;
  border-radius: 16px;
  border: 1px solid #f1f5f9;
  padding: 2.5rem;
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 2.5rem;
  align-items: center;
}

.profile-img-wrap {
  display: flex;
  justify-content: center;
}

.profile-img {
  width: 220px;
  height: 220px;
  object-fit: cover;
  border-radius: 14px;
}

.profile-info h2 {
  font-size: 1.6rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.accent {
  color: #6366f1;
}

.role {
  font-size: 0.9rem;
  color: #6366f1;
  font-weight: 500;
  margin-bottom: 1rem;
}

.bio {
  color: #64748b;
  line-height: 1.7;
  margin-bottom: 0.6rem;
  font-size: 0.9rem;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-top: 1.25rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.info-item i {
  font-size: 1rem;
  color: #6366f1;
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.06);
  border-radius: 8px;
  flex-shrink: 0;
}

.info-label {
  display: block;
  font-size: 0.62rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.info-val {
  display: block;
  font-size: 0.85rem;
  color: #1e293b;
  font-weight: 600;
}

/* Skills */
.skills {
  padding: 3rem 2rem 5rem;
  background: #f8fafc;
}

.section-head {
  text-align: center;
  margin-bottom: 2.5rem;
}

.section-tag {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #6366f1;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  margin-top: 0.35rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.skill-item {
  background: #fff;
  padding: 1rem 1.2rem;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  border: 1px solid #f1f5f9;
  transition: all 0.2s ease;
}

.skill-item:hover {
  border-color: #e2e8f0;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.skill-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.06);
  border-radius: 8px;
  flex-shrink: 0;
}

.skill-icon i {
  font-size: 1.1rem;
  color: #6366f1;
}

.skill-name {
  font-weight: 600;
  font-size: 0.85rem;
  color: #334155;
  flex: 1;
}

.skill-bar {
  width: 50px;
  height: 5px;
  background: #e2e8f0;
  border-radius: 3px;
  overflow: hidden;
  flex-shrink: 0;
}

.skill-fill {
  height: 100%;
  background: #6366f1;
  border-radius: 3px;
}

.skill-pct {
  font-size: 0.72rem;
  font-weight: 700;
  color: #6366f1;
  width: 28px;
  text-align: right;
  flex-shrink: 0;
}

@media (max-width: 900px) {
  .about-hero { padding: 7rem 1.5rem 5.5rem; }
  .about-heading { font-size: 2.4rem; }
  .profile-card {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .info-grid { grid-template-columns: 1fr; }
  .info-item { justify-content: center; }
  .skills-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
  .about-hero { padding: 6rem 1.5rem 4.5rem; }
  .about-heading { font-size: 2rem; }
  .profile-card { padding: 2rem 1.5rem; }
  .profile-img { width: 180px; height: 180px; }
  .profile-info h2 { font-size: 1.35rem; }
  .skills-grid { grid-template-columns: 1fr; }
  .skills { padding: 2.5rem 1.5rem 4rem; }
  .section-title { font-size: 1.6rem; }
}
</style>
'''

# ============================================================
# Footer.vue
# ============================================================
footer_vue = r'''<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="/" class="footer-logo">Oum<span class="accent">.</span></a>
          <p>Building modern web experiences with clean code and creative design.</p>
        </div>

        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>

        <div class="footer-social">
          <h4>Follow Me</h4>
          <div class="social-icons">
            <a href="#" aria-label="GitHub"><i class="bi bi-github"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
            <a href="#" aria-label="Twitter"><i class="bi bi-twitter-x"></i></a>
            <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {{ year }} Oum. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.footer {
  background: #0a0a1a;
  color: #64748b;
  padding: 3rem 2rem 0;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.footer-inner {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-logo {
  font-size: 1.25rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  display: inline-block;
  margin-bottom: 0.6rem;
}

.accent {
  color: #6366f1;
}

.footer-brand p {
  font-size: 0.85rem;
  line-height: 1.6;
  max-width: 280px;
}

.footer-links h4,
.footer-social h4 {
  color: #fff;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 0.4rem;
}

.footer-links a {
  color: #64748b;
  text-decoration: none;
  font-size: 0.85rem;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: #818cf8;
}

.social-icons {
  display: flex;
  gap: 0.5rem;
}

.social-icons a {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  color: #64748b;
  font-size: 0.9rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.social-icons a:hover {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

.footer-bottom {
  padding: 1.25rem 0;
  text-align: center;
}

.footer-bottom p {
  font-size: 0.78rem;
  color: #475569;
  margin: 0;
}

@media (max-width: 768px) {
  .footer-inner {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }
  .footer-brand p { max-width: 100%; }
  .footer-logo { display: block; }
  .social-icons { justify-content: center; }
}
</style>
'''

# ============================================================
# App.vue
# ============================================================
app_vue = r'''<script setup>
import Header from "@/components/layouts/Header.vue";
</script>

<template>
  <div id="app">
    <Header />
    <router-view></router-view>
  </div>
</template>

<style>
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1e293b;
  background: #fff;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

a {
  text-decoration: none;
}

img {
  max-width: 100%;
  display: block;
}
</style>
'''

# Write all files
files = {
    os.path.join(base, 'components', 'Bases', 'ProjectsSection.vue'): projects_vue,
    os.path.join(base, 'components', 'Bases', 'ServicesSection.vue'): services_vue,
    os.path.join(base, 'components', 'Bases', 'ContactSection.vue'): contact_vue,
    os.path.join(base, 'components', 'Bases', 'AboutSection.vue'): about_vue,
    os.path.join(base, 'components', 'layouts', 'footer.vue'): footer_vue,
    os.path.join(base, 'App.vue'): app_vue,
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.lstrip('\n'))
    print(f'Wrote: {os.path.basename(path)}')

print('\nAll files written successfully!')
