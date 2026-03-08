<template>
  <section id="home" class="banner">
    <!-- Animated mesh gradient background -->
    <div class="mesh-gradient"></div>
    <div class="noise-overlay"></div>

    <!-- Floating orbs -->
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <div class="banner-content">
      <!-- Left: Text -->
      <div class="banner-text">
        <div class="status-badge">
          <span class="pulse-dot"></span>
          Available for work
        </div>

        <h1 class="banner-title">
          Hi, I'm <span class="name-highlight">Oum Ussa</span>
        </h1>
        <h2 class="banner-role">
          I build
          <span class="typewriter-wrapper">
            <span class="typewriter-text">{{ currentWord }}</span>
            <span class="cursor">|</span>
          </span>
        </h2>
        <p class="banner-subtitle">
          A passionate developer crafting clean, modern, and user-friendly web
          applications with attention to detail and performance.
        </p>

        <div class="banner-buttons">
          <a href="#contact" class="btn btn-primary">
            <span>Get In Touch</span>
            <i class="bi bi-arrow-right"></i>
          </a>
          <a href="#projects" class="btn btn-glass">
            <i class="bi bi-play-circle"></i>
            <span>View Projects</span>
          </a>
        </div>

        <!-- Tech stack pills -->
        <div class="tech-stack">
          <span class="tech-label">Tech Stack</span>
          <div class="tech-pills">
            <span class="tech-pill" v-for="tech in techStack" :key="tech.name">
              <i :class="tech.icon"></i>
              {{ tech.name }}
            </span>
          </div>
        </div>
      </div>

      <!-- Right: Code terminal + stats -->
      <div class="banner-visual">
        <div class="terminal">
          <div class="terminal-bar">
            <div class="terminal-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span class="terminal-title">
              <i class="bi bi-terminal"></i> developer.js
            </span>
            <div class="terminal-actions">
              <i class="bi bi-dash-lg"></i>
              <i class="bi bi-square"></i>
              <i class="bi bi-x-lg"></i>
            </div>
          </div>
          <div class="terminal-body">
            <div
              class="code-line"
              v-for="(line, i) in codeLines"
              :key="i"
              :style="{ animationDelay: `${0.6 + i * 0.15}s` }">
              <span class="line-num">{{ i + 1 }}</span>
              <span v-html="line"></span>
            </div>
            <div
              class="code-line cursor-line"
              :style="{ animationDelay: '2s' }">
              <span class="line-num">{{ codeLines.length + 1 }}</span>
              <span class="typing-cursor">_</span>
            </div>
          </div>
        </div>

        <!-- Stats cards floating -->
        <div class="stat-card stat-card-1">
          <div class="stat-icon"><i class="bi bi-calendar-check"></i></div>
          <div>
            <span class="stat-number">3+</span>
            <span class="stat-label">Years Exp.</span>
          </div>
        </div>
        <div class="stat-card stat-card-2">
          <div class="stat-icon"><i class="bi bi-folder-check"></i></div>
          <div>
            <span class="stat-number">50+</span>
            <span class="stat-label">Projects</span>
          </div>
        </div>
        <div class="stat-card stat-card-3">
          <div class="stat-icon"><i class="bi bi-people"></i></div>
          <div>
            <span class="stat-number">30+</span>
            <span class="stat-label">Clients</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="scroll-indicator">
      <div class="mouse">
        <div class="wheel"></div>
      </div>
      <span>Scroll Down</span>
    </div>

    <!-- Bottom transition -->
    <div class="wave-bottom">
      <svg viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path
          d="M0,60 C360,120 720,0 1080,60 C1260,90 1380,70 1440,80 L1440,120 L0,120 Z"
          fill="#f8fafc" />
      </svg>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

// Typewriter effect
const words = [
  "web experiences",
  "modern UIs",
  "scalable apps",
  "digital products",
];
const currentWord = ref("");
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeTimer = null;

function typeEffect() {
  const current = words[wordIndex];

  if (!isDeleting) {
    currentWord.value = current.substring(0, charIndex + 1);
    charIndex++;
    if (charIndex === current.length) {
      isDeleting = true;
      typeTimer = setTimeout(typeEffect, 1800);
      return;
    }
    typeTimer = setTimeout(typeEffect, 90);
  } else {
    currentWord.value = current.substring(0, charIndex - 1);
    charIndex--;
    if (charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
    }
    typeTimer = setTimeout(typeEffect, 50);
  }
}

onMounted(() => {
  typeTimer = setTimeout(typeEffect, 600);
});

onUnmounted(() => {
  clearTimeout(typeTimer);
});

// Tech stack data
const techStack = [
  { name: "Vue.js", icon: "bi bi-braces" },
  { name: "JavaScript", icon: "bi bi-filetype-js" },
  { name: "CSS3", icon: "bi bi-palette" },
  { name: "Node.js", icon: "bi bi-hdd-stack" },
  { name: "Git", icon: "bi bi-git" },
];

// Code lines (syntax-highlighted HTML)
const codeLines = [
  '<span class="kw">const</span> <span class="var">developer</span> <span class="op">=</span> <span class="br">{</span>',
  '  <span class="prop">name</span><span class="op">:</span> <span class="str">"Your Name"</span><span class="op">,</span>',
  '  <span class="prop">role</span><span class="op">:</span> <span class="str">"Full Stack Developer"</span><span class="op">,</span>',
  '  <span class="prop">skills</span><span class="op">:</span> <span class="br">[</span><span class="str">"Vue"</span><span class="op">,</span> <span class="str">"JS"</span><span class="op">,</span> <span class="str">"Node"</span><span class="br">]</span><span class="op">,</span>',
  '  <span class="prop">passion</span><span class="op">:</span> <span class="str">"Building amazing things"</span><span class="op">,</span>',
  '  <span class="prop">available</span><span class="op">:</span> <span class="bool">true</span>',
  '<span class="br">}</span><span class="op">;</span>',
];
</script>

<style scoped>
/* ── Section ── */
.banner {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding: 7rem 2rem 5rem;
  background: #0f0f23;
}

/* ── Animated mesh gradient ── */
.mesh-gradient {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(
      ellipse at 20% 50%,
      rgba(99, 102, 241, 0.25) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 80% 20%,
      rgba(139, 92, 246, 0.2) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 60% 80%,
      rgba(59, 130, 246, 0.15) 0%,
      transparent 50%
    );
  animation: meshShift 12s ease-in-out infinite alternate;
}

@keyframes meshShift {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  100% {
    opacity: 0.8;
    transform: scale(1.1) rotate(2deg);
  }
}

.noise-overlay {
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
  pointer-events: none;
}

/* ── Floating orbs ── */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
  animation: orbFloat 18s ease-in-out infinite;
}
.orb-1 {
  width: 350px;
  height: 350px;
  top: -80px;
  right: 10%;
  background: rgba(99, 102, 241, 0.2);
}
.orb-2 {
  width: 250px;
  height: 250px;
  bottom: 10%;
  left: -5%;
  background: rgba(168, 85, 247, 0.15);
  animation-delay: -6s;
}
.orb-3 {
  width: 180px;
  height: 180px;
  top: 50%;
  left: 40%;
  background: rgba(59, 130, 246, 0.12);
  animation-delay: -12s;
}

@keyframes orbFloat {
  0%,
  100% {
    transform: translate(0, 0);
  }
  33% {
    transform: translate(30px, -25px);
  }
  66% {
    transform: translate(-20px, 15px);
  }
}

/* ── Content grid ── */
.banner-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  max-width: 1200px;
  width: 100%;
  position: relative;
  z-index: 2;
}

/* ── Text side ── */
.banner-text {
  animation: slideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Status badge */
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
  color: #4ade80;
  padding: 0.4rem 1rem;
  border-radius: 50px;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.3px;
  margin-bottom: 1.75rem;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background: #4ade80;
  border-radius: 50%;
  position: relative;
}
.pulse-dot::after {
  content: "";
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  border: 1px solid #4ade80;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.8);
    opacity: 0;
  }
}

/* Title */
.banner-title {
  font-size: 3.5rem;
  font-weight: 800;
  color: #f1f5f9;
  line-height: 1.15;
  margin-bottom: 0.5rem;
  letter-spacing: -1.5px;
}

.name-highlight {
  background: linear-gradient(135deg, #818cf8, #a78bfa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Role with typewriter */
.banner-role {
  font-size: 1.6rem;
  font-weight: 600;
  color: #94a3b8;
  margin-bottom: 1.25rem;
  line-height: 1.4;
}

.typewriter-wrapper {
  color: #818cf8;
  position: relative;
}

.typewriter-text {
  color: #818cf8;
}

.cursor {
  color: #818cf8;
  animation: blink 0.8s step-end infinite;
  font-weight: 300;
  margin-left: 1px;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

.banner-subtitle {
  font-size: 1.05rem;
  color: rgba(148, 163, 184, 0.8);
  line-height: 1.8;
  margin-bottom: 2rem;
  max-width: 500px;
  font-weight: 400;
}

/* ── Buttons ── */
.banner-buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 2.5rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.9rem 1.75rem;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.45);
}

.btn-primary i {
  transition: transform 0.3s ease;
}
.btn-primary:hover i {
  transform: translateX(4px);
}

.btn-glass {
  background: rgba(255, 255, 255, 0.05);
  color: #e2e8f0;
  border: 1.5px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

.btn-glass:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

/* ── Tech stack ── */
.tech-stack {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}

.tech-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: rgba(148, 163, 184, 0.5);
}

.tech-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tech-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem 0.85rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 0.78rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.tech-pill:hover {
  background: rgba(99, 102, 241, 0.1);
  border-color: rgba(99, 102, 241, 0.2);
  color: #a5b4fc;
}

/* ── Visual / Terminal ── */
.banner-visual {
  position: relative;
  animation: slideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both;
}

.terminal {
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.terminal-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 1.25rem;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.terminal-dots {
  display: flex;
  gap: 7px;
}

.dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}
.dot-red {
  background: #ef4444;
}
.dot-yellow {
  background: #eab308;
}
.dot-green {
  background: #22c55e;
}

.terminal-title {
  color: rgba(255, 255, 255, 0.35);
  font-size: 0.75rem;
  font-family: "Fira Code", "Cascadia Code", monospace;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.terminal-actions {
  display: flex;
  gap: 0.75rem;
  color: rgba(255, 255, 255, 0.15);
  font-size: 0.65rem;
}

.terminal-body {
  padding: 1.5rem 1.25rem;
  font-family: "Fira Code", "Cascadia Code", monospace;
  font-size: 0.82rem;
  line-height: 2;
}

.code-line {
  display: flex;
  align-items: center;
  white-space: nowrap;
  opacity: 0;
  animation: fadeInLine 0.4s ease forwards;
}

@keyframes fadeInLine {
  from {
    opacity: 0;
    transform: translateX(-8px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.line-num {
  color: rgba(255, 255, 255, 0.15);
  width: 24px;
  text-align: right;
  margin-right: 1.25rem;
  font-size: 0.72rem;
  user-select: none;
}

/* Syntax colors */
:deep(.kw) {
  color: #c084fc;
}
:deep(.var) {
  color: #60a5fa;
}
:deep(.op) {
  color: rgba(255, 255, 255, 0.4);
}
:deep(.prop) {
  color: #34d399;
}
:deep(.str) {
  color: #fbbf24;
}
:deep(.br) {
  color: #f472b6;
}
:deep(.bool) {
  color: #f97316;
}

.cursor-line {
  opacity: 0;
  animation: fadeInLine 0.4s ease forwards;
}

.typing-cursor {
  color: #818cf8;
  animation: blink 1s step-end infinite;
  font-weight: 700;
}

/* ── Stat cards (floating) ── */
.stat-card {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  background: rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 14px;
  padding: 0.75rem 1.1rem;
  animation: floatCard 4s ease-in-out infinite;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
}

.stat-card-1 {
  top: -15px;
  right: -10px;
  animation-delay: 0s;
}
.stat-card-2 {
  bottom: -15px;
  left: -20px;
  animation-delay: 1.3s;
}
.stat-card-3 {
  top: 45%;
  right: -30px;
  animation-delay: 2.6s;
}

@keyframes floatCard {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

.stat-icon {
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon i {
  color: #fff;
  font-size: 0.95rem;
}

.stat-number {
  display: block;
  font-size: 1.1rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}

.stat-label {
  display: block;
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.45);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* ── Scroll indicator ── */
.scroll-indicator {
  position: absolute;
  bottom: 5rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  z-index: 3;
  animation: fadeIn 1s ease 1.5s both;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.scroll-indicator span {
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.25);
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 600;
}

.mouse {
  width: 22px;
  height: 34px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  display: flex;
  justify-content: center;
  padding-top: 6px;
}

.wheel {
  width: 3px;
  height: 8px;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 2px;
  animation: scroll 2s ease-in-out infinite;
}

@keyframes scroll {
  0% {
    transform: translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateY(10px);
    opacity: 0;
  }
}

/* ── Bottom wave ── */
.wave-bottom {
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 100%;
  z-index: 3;
  line-height: 0;
}

.wave-bottom svg {
  width: 100%;
  height: 80px;
}

/* ── Responsive ── */
@media (max-width: 992px) {
  .banner-content {
    grid-template-columns: 1fr;
    gap: 3rem;
    text-align: center;
  }

  .banner-subtitle {
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }

  .banner-buttons {
    justify-content: center;
  }

  .tech-stack {
    align-items: center;
  }

  .tech-pills {
    justify-content: center;
  }

  .banner-title {
    font-size: 3rem;
  }

  .stat-card-1 {
    right: 10px;
    top: -20px;
  }
  .stat-card-2 {
    left: 10px;
    bottom: -20px;
  }
  .stat-card-3 {
    right: 0;
  }
}

@media (max-width: 768px) {
  .banner {
    padding: 6rem 1.5rem 4rem;
    min-height: auto;
  }

  .banner-title {
    font-size: 2.4rem;
  }

  .banner-role {
    font-size: 1.25rem;
  }

  .banner-subtitle {
    font-size: 0.95rem;
  }

  .stat-card {
    display: none;
  }

  .scroll-indicator {
    display: none;
  }
}

@media (max-width: 480px) {
  .banner-title {
    font-size: 2rem;
  }

  .banner-buttons {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
