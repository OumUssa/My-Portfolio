<template>
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
