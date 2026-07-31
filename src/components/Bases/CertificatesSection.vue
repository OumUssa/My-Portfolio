<template>
  <section id="certificates" class="certificates">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Qualifications</span>
        <h2 class="section-title">My Certificates</h2>
      </div>

      <div class="grid">
        <!-- Placeholder for a Certificate -->
        <div class="card">
          <div class="card-icon">
            <i class="bi bi-award"></i>
          </div>
          <h3>Coming Soon</h3>
          <p>More certificates and qualifications will be added here in the future.</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.certificates {
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
  justify-content: center;
}

.card {
  background: #fff;
  border: 1px solid #f1f5f9;
  border-radius: 12px;
  padding: 1.75rem;
  transition: all 0.25s ease;
  text-align: center;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  border-color: #e2e8f0;
}

.card-icon {
  width: 50px;
  height: 50px;
  background: rgba(99, 102, 241, 0.08);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.card-icon i {
  font-size: 1.5rem;
  color: #6366f1;
}

.card h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 0.9rem;
  color: #64748b;
  line-height: 1.6;
  margin: 0;
}

@media (max-width: 992px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 576px) {
  .certificates { padding: 4rem 1.5rem; }
  .grid { grid-template-columns: 1fr; }
  .section-title { font-size: 1.8rem; }
}
</style>
