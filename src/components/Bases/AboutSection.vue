<template>
  <section class="about-hero">
    <div class="about-hero-bg">
      <div class="blob blob-1"></div>
      <div class="blob blob-2"></div>
    </div>
    <div class="about-hero-inner">
      <span class="about-tag">About Me</span>
      <h1 class="about-heading">Know Me <span class="accent">Better</span></h1>
      <p class="about-sub">A quick overview of who I am and what I do.</p>
    </div>
  </section>

  <section class="profile">
    <div class="container">
      <div class="profile-card">
        <div class="profile-img-wrap">
          <div class="img-frame">
            <img
              src="../../assets/my_image.png"
              alt="Profile Photo"
              class="profile-img" />
          </div>
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
            I bring ideas to life through clean code and thoughtful design
            decisions.
          </p>
          <div class="info-grid">
            <div
              class="info-item"
              v-for="info in personalInfo"
              :key="info.label">
              <div class="info-icon">
                <i :class="info.icon"></i>
              </div>
              <div>
                <span class="info-label">{{ info.label }}</span>
                <span class="info-val">{{ info.value }}</span>
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
          <div
            class="skill-icon"
            :style="{
              borderColor: skill.color + '30',
              background: skill.color + '0a',
            }">
            <i :class="skill.icon" :style="{ color: skill.color }"></i>
          </div>
          <div class="skill-info">
            <div class="skill-top">
              <span class="skill-name">{{ skill.name }}</span>
              <span class="skill-pct">{{ skill.level }}</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" :style="{ width: skill.level }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const personalInfo = [
  { icon: "bi bi-person", label: "Name", value: "Oum Ussa" },
  { icon: "bi bi-envelope", label: "Email", value: "oumussa719@gmail.com" },
  { icon: "bi bi-geo-alt", label: "Location", value: "Your City, Country" },
  { icon: "bi bi-calendar3", label: "Experience", value: "1+ Years" },
];

const skills = [
  {
    name: "HTML5",
    icon: "bi bi-filetype-html",
    level: "95%",
    color: "#e34f26",
  },
  { name: "CSS3", icon: "bi bi-filetype-css", level: "90%", color: "#1572b6" },
  {
    name: "JavaScript",
    icon: "bi bi-filetype-js",
    level: "85%",
    color: "#f7df1e",
  },
  { name: "Vue.js", icon: "bi bi-braces", level: "80%", color: "#42b883" },
  {
    name: "React.js",
    icon: "bi bi-filetype-jsx",
    level: "60%",
    color: "#61dafb",
  },
  { name: "Node.js", icon: "bi bi-hdd-stack", level: "75%", color: "#5fa04e" },
  { name: "Express.js", icon: "bi bi-server", level: "70%", color: "#333333" },
  { name: "PHP", icon: "bi bi-filetype-php", level: "55%", color: "#777bb4" },
  { name: "Laravel", icon: "bi bi-box", level: "50%", color: "#ff2d20" },
  { name: "MySQL", icon: "bi bi-database", level: "65%", color: "#4479a1" },
  {
    name: "API / Fetch",
    icon: "bi bi-cloud-arrow-down",
    level: "75%",
    color: "#10b981",
  },
  {
    name: "Bootstrap",
    icon: "bi bi-bootstrap",
    level: "85%",
    color: "#7952b3",
  },
  {
    name: "Tailwind CSS",
    icon: "bi bi-palette",
    level: "70%",
    color: "#06b6d4",
  },
  { name: "Git", icon: "bi bi-git", level: "85%", color: "#f05032" },
];
</script>

<style scoped>
/* ── About Hero ── */
.about-hero {
  position: relative;
  padding: 9rem 2rem 8rem;
  text-align: center;
  overflow: hidden;
  background: linear-gradient(
    160deg,
    #f8fafc 0%,
    #eef2ff 40%,
    #f0f9ff 70%,
    #faf5ff 100%
  );
}

.about-hero-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.5;
}

.blob-1 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.2), transparent 70%);
  top: -15%;
  right: -5%;
}

.blob-2 {
  width: 350px;
  height: 350px;
  background: radial-gradient(
    circle,
    rgba(139, 92, 246, 0.15),
    transparent 70%
  );
  bottom: -10%;
  left: -8%;
}

.about-hero-inner {
  position: relative;
  z-index: 1;
}

.about-tag {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: #6366f1;
  margin-bottom: 0.75rem;
}

.about-heading {
  font-size: 3rem;
  font-weight: 800;
  color: #1e293b;
  letter-spacing: -0.5px;
  margin-bottom: 0.75rem;
}

.accent {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.about-sub {
  font-size: 0.95rem;
  color: #64748b;
  max-width: 440px;
  margin: 0 auto;
  line-height: 1.7;
}

/* ── Profile Card ── */
.profile {
  padding: 0 2rem 5rem;
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
  border: 1px solid #e2e8f0;
  padding: 2.5rem;
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 2.5rem;
  align-items: center;
  box-shadow: 0 4px 24px rgba(99, 102, 241, 0.06);
  transition: box-shadow 0.3s ease;
}

.profile-card:hover {
  box-shadow: 0 8px 40px rgba(99, 102, 241, 0.1);
}

.profile-img-wrap {
  display: flex;
  justify-content: center;
}

.img-frame {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.12);
}

.img-frame::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 16px;
  border: 2px solid rgba(99, 102, 241, 0.15);
  pointer-events: none;
}

.profile-img {
  width: 220px;
  height: 220px;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}

.img-frame:hover .profile-img {
  transform: scale(1.03);
}

.profile-info h2 {
  font-size: 1.6rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.role {
  display: inline-block;
  font-size: 0.8rem;
  color: #6366f1;
  font-weight: 600;
  background: rgba(99, 102, 241, 0.06);
  padding: 0.25rem 0.75rem;
  border-radius: 100px;
  margin-bottom: 1rem;
}

.bio {
  color: #64748b;
  line-height: 1.75;
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
  padding: 0.5rem;
  border-radius: 10px;
  transition: background 0.2s ease;
}

.info-item:hover {
  background: #f8fafc;
}

.info-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.06);
  border-radius: 8px;
  flex-shrink: 0;
}

.info-icon i {
  font-size: 1rem;
  color: #6366f1;
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

/* ── Skills Section ── */
.skills {
  padding: 4rem 2rem 5rem;
  background: #fff;
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
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.skill-item {
  background: #f8fafc;
  padding: 1.1rem 1.3rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 1rem;
  border: 1px solid #f1f5f9;
  transition: all 0.25s ease;
}

.skill-item:hover {
  border-color: #e0e7ff;
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.06);
  transform: translateY(-2px);
}

.skill-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border: 1px solid #e0e7ff;
  border-radius: 10px;
  flex-shrink: 0;
}

.skill-icon i {
  font-size: 1.1rem;
}

.skill-info {
  flex: 1;
  min-width: 0;
}

.skill-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}

.skill-name {
  font-weight: 600;
  font-size: 0.85rem;
  color: #334155;
}

.skill-pct {
  font-size: 0.72rem;
  font-weight: 700;
  color: #6366f1;
}

.skill-bar {
  width: 100%;
  height: 5px;
  background: #e2e8f0;
  border-radius: 3px;
  overflow: hidden;
}

.skill-fill {
  height: 100%;
  background: linear-gradient(90deg, #6366f1, #8b5cf6);
  border-radius: 3px;
  transition: width 0.6s ease;
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .about-hero {
    padding: 7rem 1.5rem 6rem;
  }
  .about-heading {
    font-size: 2.4rem;
  }
  .profile-card {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .info-grid {
    grid-template-columns: 1fr;
  }
  .info-item {
    justify-content: center;
  }
}

@media (max-width: 576px) {
  .about-hero {
    padding: 6rem 1.5rem 5rem;
  }
  .about-heading {
    font-size: 2rem;
  }
  .profile-card {
    padding: 2rem 1.5rem;
  }
  .profile-img {
    width: 180px;
    height: 180px;
  }
  .profile-info h2 {
    font-size: 1.35rem;
  }
  .skills-grid {
    grid-template-columns: 1fr;
  }
  .skills {
    padding: 3rem 1.5rem 4rem;
  }
  .section-title {
    font-size: 1.6rem;
  }
}
</style>
