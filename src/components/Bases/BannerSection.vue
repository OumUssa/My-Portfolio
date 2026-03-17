<template>
  <section id="home" class="hero">
    <div class="hero-bg">
      <div ref="animationContainer" class="lottie-bg"></div>
      <div class="blob blob-1"></div>
      <div class="blob blob-2"></div>
      <div class="blob blob-3"></div>
    </div>
    <div class="hero-inner">
      <div class="hero-text" :class="{ visible: mounted }">
        <div class="hero-badge">
          <span class="badge-dot"></span>
          Available for work
        </div>
        <h1 class="hero-name">Hi, I'm <span class="accent">Oum Ussa</span></h1>
        <h2 class="hero-role">
          I build
          <span class="typewriter"
            >{{ currentWord }}<span class="caret">|</span></span
          >
        </h2>
        <p class="hero-desc">
          A passionate developer crafting clean, modern, and user-friendly web
          applications with attention to detail and performance.
        </p>
        <div class="hero-actions">
          <a href="#contact" class="btn-primary">
            Get In Touch <i class="bi bi-arrow-right"></i>
          </a>
          <a href="#projects" class="btn-outline">
            <i class="bi bi-play-circle"></i> View Projects
          </a>
        </div>
        <div class="hero-stack">
          <span class="stack-label text-dark">Tech Stack</span>
          <div class="stack-items">
            <span v-for="tech in techStack" :key="tech" class="stack-tag">{{
              tech
            }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const mounted = ref(false);

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

import lottie from "lottie-web";
import animationData from "@/assets/animation.json";

const animationContainer = ref(null);

onMounted(() => {
  typeTimer = setTimeout(typeEffect, 600);
  requestAnimationFrame(() => {
    mounted.value = true;
  });
  lottie.loadAnimation({
    container: animationContainer.value,
    renderer: "svg",
    loop: true,
    autoplay: true,
    animationData: animationData,
  });
});
onUnmounted(() => clearTimeout(typeTimer));

const techStack = [
  "Vue.js",
  "JavaScript",
  "CSS3",
  "Node.js",
  "Git/Github",
  "Express.js",
];
</script>

<style scoped>
/* ── Hero Section ── */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 7rem 2rem 3rem;
  background: linear-gradient(
    160deg,
    #f8fafc 0%,
    #eef2ff 40%,
    #f0f9ff 0%,
    #faf5ff 0%
  );
  overflow: hidden;
}

/* ── Animated Blobs ── */
.hero-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  opacity: 1;
}

.lottie-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.lottie-bg :deep(svg) {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.5;
  animation: floatBlob 20s ease-in-out infinite;
}

.blob-1 {
  width: 500px;
  height: 500px;
  background: radial-gradient(
    circle,
    rgba(99, 102, 241, 0.25),
    transparent 70%
  );
  top: -10%;
  right: -5%;
  animation-delay: 0s;
}

.blob-2 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(139, 92, 246, 0.2), transparent 70%);
  bottom: -5%;
  left: -10%;
  animation-delay: -7s;
}

.blob-3 {
  width: 300px;
  height: 300px;
  background: radial-gradient(
    circle,
    rgba(59, 130, 246, 0.15),
    transparent 70%
  );
  top: 40%;
  left: 50%;
  animation-delay: -14s;
}

@keyframes floatBlob {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(30px, -40px) scale(1.05);
  }
  66% {
    transform: translate(-20px, 25px) scale(0.95);
  }
}

/* ── Layout ── */
.hero-inner {
  max-width: 1100px;
  margin: 0 auto;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  position: relative;
  z-index: 1;
}

/* ── Entrance Animations ── */
.hero-text {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-text.visible {
  opacity: 1;
  transform: translateY(0);
}

.hero-visual {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.2s;
}

.hero-visual.visible {
  opacity: 1;
  transform: translateY(0);
}

/* ── Badge ── */
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1rem 0.4rem 0.65rem;
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 100px;
  font-size: 0.78rem;
  font-weight: 500;
  color: #475569;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%,
  100% {
    box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.4);
  }
  50% {
    box-shadow: 0 0 0 6px rgba(34, 197, 94, 0);
  }
}

/* ── Typography ── */
.hero-name {
  font-size: 3.2rem;
  font-weight: 800;
  color: #1e293b;
  letter-spacing: -1.5px;
  line-height: 1.15;
  margin-bottom: 0.75rem;
}

.accent {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-role {
  font-size: 1.35rem;
  font-weight: 500;
  color: #64748b;
  margin-bottom: 1.25rem;
}

.typewriter {
  color: #6366f1;
  font-weight: 600;
}

.caret {
  color: #6366f1;
  animation: blink 0.8s step-end infinite;
  font-weight: 300;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

.hero-desc {
  font-size: 0.95rem;
  color: #64748b;
  line-height: 1.75;
  max-width: 480px;
  margin-bottom: 2rem;
}

/* ── Buttons ── */
.hero-actions {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.6rem;
  background: linear-gradient(135deg, #6366f1, #7c3aed);
  color: #fff;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 10px;
  text-decoration: none;
  transition: all 0.25s ease;
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
}

.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.6rem;
  background: #fff;
  color: #475569;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  text-decoration: none;
  transition: all 0.25s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.btn-outline:hover {
  color: #6366f1;
  border-color: #c7d2fe;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.1);
}

/* ── Tech Stack ── */
.hero-stack {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.stack-label {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #94a3b8;
}

.stack-items {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.stack-tag {
  padding: 0.3rem 0.75rem;
  font-size: 0.75rem;
  color: #6366f1;
  background: #fff;
  border: 1px solid #e0e7ff;
  border-radius: 6px;
  font-weight: 500;
  transition: all 0.2s ease;
}

.stack-tag:hover {
  background: #eef2ff;
  border-color: #c7d2fe;
}

/* ── Code Card ── */
.hero-visual {
  position: relative;
}

.code-card {
  background: linear-gradient(145deg, #f8fafc, #fff);
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 8px 32px rgba(99, 102, 241, 0.08),
    0 1px 2px rgba(0, 0, 0, 0.04);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.code-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 16px 48px rgba(99, 102, 241, 0.12),
    0 2px 4px rgba(0, 0, 0, 0.04);
}

.code-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0.85rem 1.1rem;
  border-bottom: 1px solid #f1f5f9;
  background: #fafbfc;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.red {
  background: #f87171;
}
.yellow {
  background: #fbbf24;
}
.green {
  background: #34d399;
}

.code-line {
  display: flex;
  white-space: nowrap;
}

.ln {
  color: #cbd5e1;
  width: 22px;
  text-align: right;
  margin-right: 1rem;
  font-size: 0.7rem;
  user-select: none;
}

:deep(.kw) {
  color: #8b5cf6;
}
:deep(.vr) {
  color: #3b82f6;
}
:deep(.op) {
  color: #94a3b8;
}
:deep(.pr) {
  color: #059669;
}
:deep(.st) {
  color: #d97706;
}
:deep(.br) {
  color: #ec4899;
}
:deep(.bl) {
  color: #f97316;
}

/* ── Floating Stat Cards ── */
.float-card {
  position: absolute;
  display: flex;
  flex-direction: column;
  padding: 0.75rem 1.15rem;
  background: #fff;
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  animation: floatCard 6s ease-in-out infinite;
}

.stat-1 {
  top: -16px;
  right: -12px;
  animation-delay: 0s;
}

.stat-2 {
  bottom: -16px;
  left: -20px;
  animation-delay: -3s;
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

.float-num {
  font-size: 1.15rem;
  font-weight: 700;
  color: #6366f1;
  line-height: 1;
}

.float-lbl {
  font-size: 0.6rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 3px;
  font-weight: 600;
}




.mouse {
  width: 22px;
  height: 34px;
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  display: flex;
  justify-content: center;
  padding-top: 6px;
}

.wheel {
  width: 3px;
  height: 8px;
  background: #6366f1;
  border-radius: 3px;
  animation: scrollWheel 2s ease-in-out infinite;
}

@keyframes scrollWheel {
  0% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(10px);
  }
}

/* ── Responsive ── */
@media (max-width: 992px) {
  .hero-inner {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
  }

  .hero-badge {
    margin-left: auto;
    margin-right: auto;
  }
  .hero-desc {
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
  }
  .hero-actions {
    justify-content: center;
  }
  .hero-stack {
    align-items: center;
  }
  .stack-items {
    justify-content: center;
  }
  .hero-name {
    font-size: 2.6rem;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 6rem 1.5rem 3rem;
    min-height: auto;
  }
  .hero-name {
    font-size: 2.2rem;
  }
  .hero-role {
    font-size: 1.15rem;
  }
  .float-card {
    display: none;
  }
  .scroll-hint {
    display: none;
  }
  .blob {
    opacity: 0.3;
  }
}

@media (max-width: 480px) {
  .hero-name {
    font-size: 1.9rem;
  }
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
  .btn-primary,
  .btn-outline {
    width: 100%;
    justify-content: center;
  }
}
</style>
