<template>
  <section id="testimonials" class="testimonials">
    <div class="container">
      <div class="section-header">
        <span class="label">Testimonials</span>
        <h2 class="section-title">What People Say</h2>
        <div class="title-line"></div>
      </div>

      <div class="slider-wrapper">
        <div
          class="slider-track"
          :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
          <div v-for="(t, i) in testimonials" :key="i" class="slide">
            <div class="testimonial-card">
              <div class="quote-icon">
                <i class="bi bi-quote"></i>
              </div>
              <p class="testimonial-text">{{ t.text }}</p>
              <div class="testimonial-author">
                <div class="author-avatar" :style="{ background: t.color }">
                  {{ t.initials }}
                </div>
                <div>
                  <span class="author-name">{{ t.name }}</span>
                  <span class="author-role">{{ t.role }}</span>
                </div>
              </div>
              <div class="stars">
                <i v-for="s in 5" :key="s" class="bi bi-star-fill"></i>
              </div>
            </div>
          </div>
        </div>

        <!-- Controls -->
        <div class="slider-controls">
          <button
            class="slider-btn"
            @click="prevSlide"
            :disabled="currentSlide === 0">
            <i class="bi bi-chevron-left"></i>
          </button>
          <div class="slider-dots">
            <span
              v-for="(_, i) in totalSlides"
              :key="i"
              class="dot"
              :class="{ active: currentSlide === i }"
              @click="currentSlide = i">
            </span>
          </div>
          <button
            class="slider-btn"
            @click="nextSlide"
            :disabled="currentSlide === totalSlides - 1">
            <i class="bi bi-chevron-right"></i>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";

const testimonials = [
  {
    name: "Sarah Johnson",
    role: "CEO, TechStartup",
    initials: "SJ",
    color: "#6366f1",
    text: "Working with this developer was an absolute pleasure. The attention to detail and clean code quality exceeded our expectations. Highly recommend!",
  },
  {
    name: "Michael Chen",
    role: "Product Manager",
    initials: "MC",
    color: "#ec4899",
    text: "Delivered our project on time with exceptional quality. Great communication throughout the entire process and very responsive to feedback.",
  },
  {
    name: "Emily Davis",
    role: "Founder, DesignCo",
    initials: "ED",
    color: "#0ea5e9",
    text: "The website they built for us is not only beautiful but also incredibly fast and user-friendly. Our conversion rates have significantly improved.",
  },
  {
    name: "David Kim",
    role: "CTO, AppWorks",
    initials: "DK",
    color: "#10b981",
    text: "Outstanding technical skills combined with a great eye for design. They transformed our ideas into a polished, professional web application.",
  },
];

const currentSlide = ref(0);
const totalSlides = computed(() => testimonials.length);
let interval;

const nextSlide = () => {
  if (currentSlide.value < totalSlides.value - 1) currentSlide.value++;
  else currentSlide.value = 0;
};

const prevSlide = () => {
  if (currentSlide.value > 0) currentSlide.value--;
  else currentSlide.value = totalSlides.value - 1;
};

onMounted(() => {
  interval = setInterval(nextSlide, 5000);
});

onUnmounted(() => {
  clearInterval(interval);
});
</script>

<style scoped>
.testimonials {
  padding: 6rem 2rem;
  background: #f8fafc;
}

.container {
  max-width: 900px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 3.5rem;
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

/* ── Slider ── */
.slider-wrapper {
  overflow: hidden;
  position: relative;
}

.slider-track {
  display: flex;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide {
  min-width: 100%;
  padding: 0 1rem;
  box-sizing: border-box;
}

.testimonial-card {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 2.5rem;
  text-align: center;
  position: relative;
}

.quote-icon {
  font-size: 2.5rem;
  color: #c7d2fe;
  margin-bottom: 1rem;
  line-height: 1;
}

.testimonial-text {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.75;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  margin-bottom: 1rem;
}

.author-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 700;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.author-name {
  display: block;
  font-weight: 700;
  color: #1e293b;
  font-size: 0.95rem;
  text-align: left;
}

.author-role {
  display: block;
  font-size: 0.8rem;
  color: #94a3b8;
  text-align: left;
}

.stars {
  display: flex;
  justify-content: center;
  gap: 0.2rem;
}

.stars i {
  color: #fbbf24;
  font-size: 0.85rem;
}

/* ── Controls ── */
.slider-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 2rem;
}

.slider-btn {
  width: 40px;
  height: 40px;
  border: 1.5px solid #e2e8f0;
  border-radius: 50%;
  background: #fff;
  color: #475569;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.slider-btn:hover:not(:disabled) {
  background: #6366f1;
  color: #fff;
  border-color: #6366f1;
}

.slider-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.slider-dots {
  display: flex;
  gap: 0.5rem;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #cbd5e1;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: #6366f1;
  width: 28px;
  border-radius: 5px;
}

@media (max-width: 768px) {
  .testimonials {
    padding: 4rem 1.5rem;
  }

  .testimonial-card {
    padding: 2rem 1.5rem;
  }

  .testimonial-text {
    font-size: 0.95rem;
  }

  .section-title {
    font-size: 2rem;
  }
}
</style>
