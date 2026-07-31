<template>
  <section id="achievements" class="achievements">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Milestones</span>
        <h2 class="section-title">My Achievements</h2>
      </div>

      <div class="achievement-content">
        <div class="text-content">
          <h3>ANT TECHNOLOGY TRAINING CENTER <span class="badge">(Scholarship Trainee)</span></h3>
          
          <div class="scholarship-meta">
            <div class="meta-item"><i class="bi bi-calendar3"></i> <span>16 June 2025 - 17 July 2026</span></div>
            <div class="meta-item"><i class="bi bi-clock"></i> <span>Mon-Fri (700 hours)</span></div>
            <div class="meta-item"><i class="bi bi-building"></i> <span>Sponsored by Ministry of Post and Telecommunications & CBRD Fund</span></div>
          </div>

          <div class="course-grid">
            <div class="course-card">
              <h4><i class="bi bi-laptop"></i> Frontend</h4>
              <p>HTML, CSS, Bootstrap, JavaScript, Vue.js, API Consumption</p>
            </div>
            <div class="course-card">
              <h4><i class="bi bi-server"></i> Backend</h4>
              <p>Node.js, Express.js, API Design, JWT Authentication, MVC Architecture</p>
            </div>
            <div class="course-card">
              <h4><i class="bi bi-journal-code"></i> Extra Courses</h4>
              <p>C++, UX/UI Advanced Concepts, Cyber Security Fundamentals</p>
            </div>
            <div class="course-card">
              <h4><i class="bi bi-diagram-3"></i> Core Skills</h4>
              <p>Git, GitHub, Team Collaboration, SDLC</p>
            </div>
          </div>
        </div>
        <div class="images-grid">
          <img src="@/assets/Achievements_1.jpg" alt="Achievement 1" class="achievement-img" />
          <img src="@/assets/Achievements_2.jpg" alt="Achievement 2" class="achievement-img" />
          <img src="@/assets/Achievements_3.jpg" alt="Achievement 3" class="achievement-img" />
          <img src="@/assets/Achievements_4.jpg" alt="Achievement 4" class="achievement-img" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.achievements {
  padding: 6rem 2rem;
  background: #fff;
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

.achievement-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.text-content {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.text-content h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.badge {
  font-size: 0.9rem;
  font-weight: 500;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.1);
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  vertical-align: middle;
  margin-left: 0.5rem;
  display: inline-block;
  margin-top: 0.5rem;
}

.scholarship-meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 2rem;
  padding: 1.25rem;
  background: #f8fafc;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: #475569;
}

.meta-item i {
  color: #6366f1;
  font-size: 1.1rem;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  text-align: left;
}

.course-card {
  padding: 1.25rem;
  background: #fff;
  border: 1px solid #f1f5f9;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
  transition: all 0.2s ease;
}

.course-card:hover {
  border-color: #c7d2fe;
  transform: translateY(-2px);
}

.course-card h4 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.course-card h4 i {
  color: #6366f1;
}

.course-card p {
  font-size: 0.85rem;
  color: #64748b;
  line-height: 1.5;
  margin: 0;
}

.images-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
}

.achievement-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease;
}

.achievement-img:hover {
  transform: scale(1.02);
}

@media (max-width: 768px) {
  .images-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 576px) {
  .achievements {
    padding: 4rem 1.5rem;
  }
  .section-title {
    font-size: 1.8rem;
  }
}
</style>
