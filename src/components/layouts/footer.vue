<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="/" class="footer-logo">Oum<span class="accent">.</span></a>
          <p>Building modern web experiences with clean code and creative design.</p>
        </div>

        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
            <li><router-link to="/admin">Admin</router-link></li>
          </ul>
        </div>

        <div class="footer-social">
          <h4>Follow Me</h4>
          <div class="social-icons">
            <a href="#" aria-label="GitHub"><i class="bi bi-github"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
            <a href="#" aria-label="Twitter"><i class="bi bi-twitter-x"></i></a>
            <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {{ year }} Oum. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.footer {
  background: #0a0a1a;
  color: #64748b;
  padding: 3rem 2rem 0;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
}

.footer-inner {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-logo {
  font-size: 1.25rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  display: inline-block;
  margin-bottom: 0.6rem;
}

.accent {
  color: #6366f1;
}

.footer-brand p {
  font-size: 0.85rem;
  line-height: 1.6;
  max-width: 280px;
}

.footer-links h4,
.footer-social h4 {
  color: #fff;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 0.4rem;
}

.footer-links a {
  color: #64748b;
  text-decoration: none;
  font-size: 0.85rem;
  transition: color 0.2s ease;
}

.footer-links a:hover {
  color: #818cf8;
}

.social-icons {
  display: flex;
  gap: 0.5rem;
}

.social-icons a {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  color: #64748b;
  font-size: 0.9rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.social-icons a:hover {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

.footer-bottom {
  padding: 1.25rem 0;
  text-align: center;
}

.footer-bottom p {
  font-size: 0.78rem;
  color: #475569;
  margin: 0;
}

@media (max-width: 768px) {
  .footer-inner {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }
  .footer-brand p { max-width: 100%; }
  .footer-logo { display: block; }
  .social-icons { justify-content: center; }
}
</style>
