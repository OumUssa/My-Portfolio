<template>
  <section id="home" class="hero">
    <div class="hero-bg"></div>
    <div class="hero-inner">
      <div class="hero-text">
        <p class="hero-greeting">Hi, I'm</p>
        <h1 class="hero-name">Oum Ussa</h1>
        <h2 class="hero-role">
          I build
          <span class="typewriter">{{ currentWord }}<span class="caret">|</span></span>
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
            View Projects
          </a>
        </div>
        <div class="hero-stack">
          <span class="stack-label">Tech Stack</span>
          <div class="stack-items">
            <span v-for="tech in techStack" :key="tech" class="stack-tag">{{ tech }}</span>
          </div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="code-card">
          <div class="code-header">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
            <span class="code-title">developer.js</span>
          </div>
          <div class="code-body">
            <div class="code-line" v-for="(line, i) in codeLines" :key="i">
              <span class="ln">{{ i + 1 }}</span>
              <span v-html="line"></span>
            </div>
          </div>
        </div>
        <div class="stat stat-1">
          <span class="stat-num">3+</span>
          <span class="stat-lbl">Years Exp.</span>
        </div>
        <div class="stat stat-2">
          <span class="stat-num">50+</span>
          <span class="stat-lbl">Projects</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const words = ["web experiences", "modern UIs", "scalable apps", "digital products"];
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

onMounted(() => { typeTimer = setTimeout(typeEffect, 600); });
onUnmounted(() => clearTimeout(typeTimer));

const techStack = ["Vue.js", "JavaScript", "CSS3", "Node.js", "Git"];

const codeLines = [
  '<span class="kw">const</span> <span class="vr">developer</span> <span class="op">=</span> <span class="br">{</span>',
  '  <span class="pr">name</span><span class="op">:</span> <span class="st">"Oum Ussa"</span><span class="op">,</span>',
  '  <span class="pr">role</span><span class="op">:</span> <span class="st">"Full Stack Developer"</span><span class="op">,</span>',
  '  <span class="pr">skills</span><span class="op">:</span> <span class="br">[</span><span class="st">"Vue"</span><span class="op">,</span> <span class="st">"JS"</span><span class="op">,</span> <span class="st">"Node"</span><span class="br">]</span><span class="op">,</span>',
  '  <span class="pr">available</span><span class="op">:</span> <span class="bl">true</span>',
  '<span class="br">}</span><span class="op">;</span>',
];
</script>

<style scoped>
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 7rem 2rem 5rem;
  background: #0a0a1a;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 25% 50%, rgba(99, 102, 241, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse at 75% 25%, rgba(139, 92, 246, 0.08) 0%, transparent 50%);
}

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

.hero-greeting {
  font-size: 1rem;
  color: #6366f1;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.hero-name {
  font-size: 3.2rem;
  font-weight: 800;
  color: #f1f5f9;
  letter-spacing: -1px;
  line-height: 1.1;
  margin-bottom: 0.75rem;
}

.hero-role {
  font-size: 1.4rem;
  font-weight: 500;
  color: #64748b;
  margin-bottom: 1.25rem;
}

.typewriter {
  color: #818cf8;
}

.caret {
  color: #818cf8;
  animation: blink 0.8s step-end infinite;
  font-weight: 300;
}

@keyframes blink { 50% { opacity: 0; } }

.hero-desc {
  font-size: 0.95rem;
  color: #64748b;
  line-height: 1.7;
  max-width: 480px;
  margin-bottom: 2rem;
}

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
  padding: 0.75rem 1.5rem;
  background: #6366f1;
  color: #fff;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 8px;
  text-decoration: none;
  transition: background 0.2s ease;
}

.btn-primary:hover {
  background: #4f46e5;
}

.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: #94a3b8;
  font-size: 0.875rem;
  font-weight: 500;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-outline:hover {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.2);
}

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
  color: #475569;
}

.stack-items {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.stack-tag {
  padding: 0.3rem 0.7rem;
  font-size: 0.75rem;
  color: #94a3b8;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 6px;
  font-weight: 500;
}

/* Code Card */
.hero-visual {
  position: relative;
}

.code-card {
  background: rgba(15, 15, 35, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  overflow: hidden;
}

.code-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.red { background: #ef4444; }
.yellow { background: #eab308; }
.green { background: #22c55e; }

.code-title {
  margin-left: auto;
  font-size: 0.7rem;
  color: #475569;
  font-family: "Fira Code", monospace;
}

.code-body {
  padding: 1.25rem 1rem;
  font-family: "Fira Code", "Cascadia Code", monospace;
  font-size: 0.8rem;
  line-height: 1.9;
}

.code-line {
  display: flex;
  white-space: nowrap;
}

.ln {
  color: rgba(255, 255, 255, 0.12);
  width: 22px;
  text-align: right;
  margin-right: 1rem;
  font-size: 0.7rem;
  user-select: none;
}

:deep(.kw) { color: #c084fc; }
:deep(.vr) { color: #60a5fa; }
:deep(.op) { color: rgba(255, 255, 255, 0.3); }
:deep(.pr) { color: #34d399; }
:deep(.st) { color: #fbbf24; }
:deep(.br) { color: #f472b6; }
:deep(.bl) { color: #f97316; }

/* Stat Cards */
.stat {
  position: absolute;
  display: flex;
  flex-direction: column;
  padding: 0.75rem 1.1rem;
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
}

.stat-1 { top: -12px; right: -8px; }
.stat-2 { bottom: -12px; left: -16px; }

.stat-num {
  font-size: 1.1rem;
  font-weight: 700;
  color: #fff;
  line-height: 1;
}

.stat-lbl {
  font-size: 0.6rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 2px;
}

/* Responsive */
@media (max-width: 992px) {
  .hero-inner {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
  }

  .hero-desc { max-width: 100%; margin-left: auto; margin-right: auto; }
  .hero-actions { justify-content: center; }
  .hero-stack { align-items: center; }
  .stack-items { justify-content: center; }
  .hero-name { font-size: 2.6rem; }
}

@media (max-width: 768px) {
  .hero { padding: 6rem 1.5rem 3rem; min-height: auto; }
  .hero-name { font-size: 2.2rem; }
  .hero-role { font-size: 1.15rem; }
  .stat { display: none; }
}

@media (max-width: 480px) {
  .hero-name { font-size: 1.9rem; }
  .hero-actions { flex-direction: column; align-items: center; }
  .btn-primary, .btn-outline { width: 100%; justify-content: center; }
}
</style>
