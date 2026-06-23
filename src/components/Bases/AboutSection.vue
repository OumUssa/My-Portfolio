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
      <div class="lottie-wrapper">
        <div ref="lottieContainer" class="lottie-animation"></div>
      </div>
    </div>
  </section>

  <section class="profile pb-5">
    <div class="container pt-5">
      <div class="profile-card pt-5">
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
          <p class="role">Back-End Developer</p>
          <p class="bio">
            I am a driven IT Engineering student, an MPTC Scholarship recipient at ANT, and a web developer with a strong focus on building secure, scalable backend architectures. I approach software engineering with careful reasoning, believing that the best digital solutions come from deeply understanding the 'why' behind a problem before writing code.
          </p>
          <p class="bio">
            While I specialize in robust server-side logic and database design, I care deeply about the final user experience. I thrive in collaborative team environments, bringing strong situational awareness and clear communication to deliver highly refined, clean digital environments.
          </p>
          
          <div class="cv-action mt-2 mb-4">
            <a :href="cvFile" download="CV_OumUssa.pdf" class="cv-btn-simple">
              <i class="bi bi-file-earmark-arrow-down"></i> Download Resume
            </a>
          </div>

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

  <section class="timeline-section">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">My Journey</span>
        <h2 class="section-title">Experience & Education</h2>
      </div>
      <div class="timeline-grid">
        <div class="timeline-col">
          <h3 class="timeline-title"><i class="bi bi-briefcase"></i> Experience</h3>
          <div class="timeline-wrap">
            <div class="timeline-item" v-for="exp in experience" :key="exp.title">
              <div class="timeline-dot"></div>
              <div class="timeline-content">
                <h4>{{ exp.title }}</h4>
                <p class="timeline-desc">{{ exp.desc }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="timeline-col">
          <h3 class="timeline-title"><i class="bi bi-mortarboard"></i> Education</h3>
          <div class="timeline-wrap">
            <div class="timeline-item" v-for="edu in education" :key="edu.title">
              <div class="timeline-dot"></div>
              <div class="timeline-content">
                <h4>{{ edu.title }}</h4>
                <span class="timeline-date">{{ edu.date }}</span>
                <p class="timeline-desc">{{ edu.desc }}</p>
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
import { ref, onMounted } from "vue";
import lottie from "lottie-web";
import mentalTherapyAnimation from "../../assets/mental-therapy.json";
import cvFile from "../../assets/CV_OumUssa.pdf";

const lottieContainer = ref(null);

onMounted(() => {
  if (lottieContainer.value) {
    lottie.loadAnimation({
      container: lottieContainer.value,
      renderer: "svg",
      loop: true,
      autoplay: true,
      animationData: mentalTherapyAnimation,
    });
  }
});

const personalInfo = [
  { icon: "bi bi-person", label: "Name", value: "Oum Ussa" },
  { icon: "bi bi-envelope", label: "Email", value: "oumussa719@gmail.com" },
  { icon: "bi bi-geo-alt", label: "Location", value: "Por Sen Chey, Phnom Penh " },
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
  { name: "Express.js", icon: "bi bi-server", level: "90%", color: "#333333" },
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
  { name: "Git & GitHub", icon: "bi bi-github", level: "85%", color: "#f05032" },
  { name: "Contabo / VPS", icon: "bi bi-hdd-network", level: "70%", color: "#003b5c" },
  { name: "aaPanel", icon: "bi bi-server", level: "75%", color: "#20a53a" },
  { name: "Postman", icon: "bi bi-send", level: "80%", color: "#ff6c37" }
];

const experience = [
  {
    title: "Clinic & Pet Management System",
    desc: "Developed a full-stack platform featuring an automated appointment booking system with Node.js/Express.js/Laravel and MySQL."
  },
  {
    title: "WorkSync with Dashboard",
    desc: "Engineered a secure web application focused on workflow management and efficient RESTful API integration."
  },
  {
    title: "Personal Portfolio Dashboard",
    desc: "Designed and developed a minimalist, high-end developer portfolio and dashboard using Vue.js / Node.js / Express.js and modern responsive UI architectures."
  },
  {
    title: "e-examCam",
    desc: "Designed clean, responsive, and intuitive web interfaces using HTML/CSS/Bootstrap and JavaScript."
  },
  {
    title: "Deployment & Tools",
    desc: "Hosted and deployed projects on Linux VPS (Contabo) using aaPanel; utilized Git/GitHub for strict version control."
  }
];

const education = [
  {
    title: "Royal University of Phnom Penh (RUPP)",
    date: "2023 - Present",
    desc: "Bachelor of Information Technology Engineering (ITE)"
  },
  {
    title: "ANT Training",
    date: "Scholarship",
    desc: "MPTC Full Stack Development Scholarship recipient."
  }
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

.lottie-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
}

.lottie-animation {
  width: 350px;
  max-width: 100%;
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



/* ── Download CV Button (Simple) ── */
.cv-btn-simple {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(99, 102, 241, 0.08);
  color: #6366f1;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.2s ease;
  border: 1px solid rgba(99, 102, 241, 0.15);
}

.cv-btn-simple:hover {
  background: rgba(99, 102, 241, 0.15);
  transform: translateY(-1px);
}

/* ── Timeline Section ── */
.timeline-section {
  padding: 5rem 2rem;
  background: #f8fafc;
}

.timeline-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
}

.timeline-col {
  background: #fff;
  padding: 2.5rem;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 24px rgba(99, 102, 241, 0.04);
}

.timeline-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.timeline-title i {
  color: #6366f1;
}

.timeline-wrap {
  border-left: 2px solid #e2e8f0;
  padding-left: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.timeline-item {
  position: relative;
}

.timeline-dot {
  position: absolute;
  left: calc(-2rem - 8px);
  top: 2px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #6366f1;
  border: 3px solid #fff;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.timeline-content h4 {
  font-size: 1.1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.3rem;
  line-height: 1.4;
}

.timeline-date {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.1);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  margin-bottom: 0.75rem;
}

.timeline-desc {
  font-size: 0.85rem;
  color: #64748b;
  line-height: 1.6;
  margin: 0;
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .about-hero {
    padding: 7rem 1.5rem 6rem;
  }
  .about-heading {
    font-size: 2.4rem;
  }
  .profile {
    padding: 0 1.5rem 4rem;
  }
  .profile-card {
    grid-template-columns: 1fr;
    text-align: center;
    padding: 2rem;
  }
  .info-grid {
    grid-template-columns: 1fr;
  }
  .info-item {
    justify-content: center;
  }
  .skills-grid {
    grid-template-columns: 1fr;
  }
  .timeline-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 576px) {
  .about-hero {
    padding: 5rem 1rem 4rem;
  }
  .about-heading {
    font-size: 2rem;
  }
  .profile {
    padding: 0 1rem 3rem;
  }
  .profile-card {
    padding: 1.5rem 1rem;
  }
  .profile-img {
    width: 150px;
    height: 150px;
  }
  .profile-info h2 {
    font-size: 1.35rem;
  }
  .skills {
    padding: 3rem 1rem 4rem;
  }
  .section-title {
    font-size: 1.6rem;
  }
  .timeline-section {
    padding: 3rem 1rem;
  }
}
</style>
