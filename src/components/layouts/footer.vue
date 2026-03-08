<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="footer-logo">
            <i class="bi bi-code-slash"></i>
            <span>Portfolio</span>
          </a>
          <p>
            Building modern web experiences with clean code and creative design.
          </p>
        </div>

        <div class="footer-links">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>

        <div class="footer-social">
          <h4>Follow Me</h4>
          <div class="social-icons">
            <a href="#"><i class="bi bi-github"></i></a>
            <a href="#"><i class="bi bi-linkedin"></i></a>
            <a href="#"><i class="bi bi-twitter-x"></i></a>
            <a href="#"><i class="bi bi-facebook"></i></a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {{ year }} Portfolio. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.footer {
  background: #0f172a;
  color: #94a3b8;
  padding: 3rem 2rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem;
  padding-bottom: 2.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.4rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  margin-bottom: 0.8rem;
}

.footer-brand p {
  font-size: 0.88rem;
  line-height: 1.6;
  max-width: 300px;
}

.footer-links h4,
.footer-social h4 {
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.88rem;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #a78bfa;
}

.social-icons {
  display: flex;
  gap: 0.6rem;
}

.social-icons a {
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  color: #94a3b8;
  font-size: 1rem;
  transition: all 0.3s ease;
  text-decoration: none;
}

.social-icons a:hover {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
  transform: translateY(-2px);
}

.footer-bottom {
  padding: 1.5rem 0;
  text-align: center;
}

.footer-bottom p {
  font-size: 0.8rem;
  color: #475569;
  margin: 0;
}

@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }

  .footer-brand p {
    max-width: 100%;
  }

  .footer-logo {
    justify-content: center;
  }

  .social-icons {
    justify-content: center;
  }
}
</style>
