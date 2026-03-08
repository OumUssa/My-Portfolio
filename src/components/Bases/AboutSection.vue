<template>
  <!-- Hero Banner -->
  <section class="hero-banner">
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <span class="hero-label">About Me</span>
      <h1 class="hero-title">Know Me Better</h1>
      <div class="hero-line"></div>
    </div>
  </section>

  <!-- Profile Card (overlapping banner) -->
  <section class="profile-section">
    <div class="container">
      <div class="profile-card">
        <!-- Profile Image -->
        <div class="profile-image-wrapper">
          <div class="image-frame">
            <!-- Replace the src below with your own photo -->
            <img :src="profileImage" alt="My Photo" class="profile-image" />
            <div class="image-decoration"></div>
          </div>
        </div>

        <!-- Profile Info -->
        <div class="profile-info">
          <h2>Hi, I'm <span class="accent">Your Name</span></h2>
          <p class="role">Full-Stack Developer</p>
          <p class="bio">
            I'm a passionate full-stack developer with a love for creating
            beautiful, functional, and user-friendly websites. I specialize in
            building modern web applications with the latest technologies.
          </p>
          <p class="bio">
            With a strong foundation in both front-end and back-end development,
            I bring ideas to life through clean code and thoughtful design
            decisions.
          </p>

          <div class="info-grid">
            <div class="info-item">
              <i class="bi bi-person"></i>
              <div>
                <span class="info-label">Name</span>
                <span class="info-value">Oum Ussa</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-envelope"></i>
              <div>
                <span class="info-label">Email</span>
                <span class="info-value">oumussa719@gmail.com</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-geo-alt"></i>
              <div>
                <span class="info-label">Location</span>
                <span class="info-value">Your City, Country</span>
              </div>
            </div>
            <div class="info-item">
              <i class="bi bi-calendar3"></i>
              <div>
                <span class="info-label">Experience</span>
                <span class="info-value">1+ Years</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Skills Section -->
  <section class="skills-section">
    <div class="container">
      <div class="section-header">
        <span class="label">My Expertise</span>
        <h2 class="section-title">Skills & Technologies</h2>
        <div class="title-line"></div>
      </div>

      <div class="skills-grid">
        <div v-for="skill in skills" :key="skill.name" class="skill-card">
          <div class="skill-icon">
            <i :class="skill.icon"></i>
          </div>
          <span class="skill-name">{{ skill.name }}</span>
          <div class="skill-bar">
            <div class="skill-fill" :style="{ width: skill.level }"></div>
          </div>
          <span class="skill-percent">{{ skill.level }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

// Replace this with the path to your own image
// e.g. import myPhoto from '@/assets/my-photo.jpg'
// or use a URL: const profileImage = ref('https://your-photo-url.jpg')
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
/* ── Hero Banner ── */
.hero-banner {
  position: relative;
  background: #6366f1;
  padding: 10rem 2rem 8rem;
  text-align: center;
  overflow: hidden;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: rgba(255, 255, 255, 0.8);
  display: block;
  margin-bottom: 0.8rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 1rem;
}

.hero-line {
  width: 60px;
  height: 4px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 2px;
  margin: 0 auto;
}

/* ── Profile Section ── */
.profile-section {
  padding: 0 2rem 4rem;
  background: #f8fafc;
  margin-top: -5rem;
  position: relative;
  z-index: 2;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.profile-card {
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
  padding: 3rem;
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 3rem;
  align-items: center;
}

/* ── Profile Image ── */
.profile-image-wrapper {
  display: flex;
  justify-content: center;
}

.image-frame {
  position: relative;
  width: 240px;
  height: 240px;
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
  position: relative;
  z-index: 1;
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.2);
}

.image-decoration {
  position: absolute;
  top: 12px;
  left: 12px;
  right: -12px;
  bottom: -12px;
  border: 3px solid #6366f1;
  border-radius: 20px;
  z-index: 0;
  opacity: 0.3;
}

/* ── Profile Info ── */
.profile-info h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.3rem;
}

.accent {
  color: #6366f1;
}

.role {
  font-size: 1rem;
  font-weight: 500;
  color: #6366f1;
  margin-bottom: 1.2rem;
}

.bio {
  color: #64748b;
  line-height: 1.8;
  margin-bottom: 0.8rem;
  font-size: 0.95rem;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1.5rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 0;
}

.info-item i {
  font-size: 1.1rem;
  color: #6366f1;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.08);
  border-radius: 10px;
  flex-shrink: 0;
}

.info-label {
  display: block;
  font-size: 0.68rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 500;
}

.info-value {
  display: block;
  font-size: 0.88rem;
  color: #1e293b;
  font-weight: 600;
}

/* ── Skills Section ── */
.skills-section {
  padding: 4rem 2rem 5rem;
  background: #f8fafc;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
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
  font-size: 2.2rem;
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

.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.2rem;
}

.skill-card {
  background: #fff;
  padding: 1.2rem 1.4rem;
  border-radius: 14px;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

.skill-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.1);
  border-color: #c7d2fe;
}

.skill-icon {
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.08);
  border-radius: 10px;
  flex-shrink: 0;
}

.skill-icon i {
  font-size: 1.2rem;
  color: #6366f1;
}

.skill-name {
  font-weight: 600;
  font-size: 0.9rem;
  color: #334155;
  flex: 1;
}

.skill-bar {
  width: 60px;
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  overflow: hidden;
  flex-shrink: 0;
}

.skill-fill {
  height: 100%;
  background: #6366f1;
  border-radius: 3px;
  transition: width 1s ease;
}

.skill-percent {
  font-size: 0.75rem;
  font-weight: 700;
  color: #6366f1;
  width: 32px;
  text-align: right;
  flex-shrink: 0;
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .profile-card {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 2.5rem 2rem;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .info-item {
    justify-content: center;
  }

  .skills-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .hero-banner {
    padding: 8rem 1.5rem 6rem;
  }

  .hero-title {
    font-size: 2.2rem;
  }

  .profile-card {
    padding: 2rem 1.5rem;
    gap: 2rem;
  }

  .image-frame {
    width: 180px;
    height: 180px;
  }

  .profile-info h2 {
    font-size: 1.5rem;
  }

  .skills-grid {
    grid-template-columns: 1fr;
  }

  .section-title {
    font-size: 1.8rem;
  }

  .skills-section {
    padding: 3rem 1.5rem 4rem;
  }
}
</style>
