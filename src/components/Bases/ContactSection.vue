<template>
  <section id="contact" class="contact">
    <!-- Decorative background elements -->
    <div class="bg-glow bg-glow--left"></div>
    <div class="bg-glow bg-glow--right"></div>

    <div class="container">
      <div class="section-header" data-aos="fade-up">
        <span class="label">Get In Touch</span>
        <h2 class="section-title">
          Let's Work <span class="gradient-text">Together</span>
        </h2>
        <p class="section-subtitle">
          Have a project in mind or just want to say hello? I'd love to hear
          from you.
        </p>
        <div class="title-line"></div>
      </div>

      <div class="contact-wrapper">
        <!-- Left info panel (dark) -->
        <div class="contact-info-panel">
          <div class="info-panel-bg"></div>
          <div class="info-content">
            <h3 class="info-heading">Contact Information</h3>
            <p class="info-desc">
              Fill up the form and I'll get back to you within 24 hours.
            </p>

            <div class="contact-cards">
              <a href="mailto:oumussa719@gmail.com" class="contact-card">
                <div class="contact-icon">
                  <i class="bi bi-envelope"></i>
                </div>
                <div class="card-text">
                  <span class="card-label">Email</span>
                  <span class="card-value">oumussa719@gmail.com</span>
                </div>
                <i class="bi bi-arrow-right card-arrow"></i>
              </a>

              <a href="tel:+1234567890" class="contact-card">
                <div class="contact-icon">
                  <i class="bi bi-telephone"></i>
                </div>
                <div class="card-text">
                  <span class="card-label">Phone</span>
                  <span class="card-value">+1 234 567 890</span>
                </div>
                <i class="bi bi-arrow-right card-arrow"></i>
              </a>

              <div class="contact-card">
                <div class="contact-icon">
                  <i class="bi bi-geo-alt"></i>
                </div>
                <div class="card-text">
                  <span class="card-label">Location</span>
                  <span class="card-value">Your City, Country</span>
                </div>
              </div>
            </div>

            <div class="divider"></div>

            <div class="socials">
              <span class="social-label">Find me on</span>
              <div class="social-links">
                <a
                  href="#"
                  class="social-link social-github"
                  aria-label="GitHub"
                  ><i class="bi bi-github"></i
                ></a>
                <a
                  href="#"
                  class="social-link social-linkedin"
                  aria-label="LinkedIn"
                  ><i class="bi bi-linkedin"></i
                ></a>
                <a
                  href="#"
                  class="social-link social-twitter"
                  aria-label="Twitter"
                  ><i class="bi bi-twitter-x"></i
                ></a>
                <a
                  href="#"
                  class="social-link social-facebook"
                  aria-label="Facebook"
                  ><i class="bi bi-facebook"></i
                ></a>
              </div>
            </div>
          </div>

          <!-- Decorative circles -->
          <div class="deco-circle deco-circle--lg"></div>
          <div class="deco-circle deco-circle--sm"></div>
        </div>

        <!-- Right form panel -->
        <form class="contact-form" @submit.prevent="sendEmail">
          <!-- Status message -->
          <Transition name="slide-fade">
            <div v-if="statusMsg" class="status-msg" :class="statusType">
              <i
                :class="
                  statusType === 'success'
                    ? 'bi bi-check-circle-fill'
                    : 'bi bi-exclamation-circle-fill'
                "></i>
              {{ statusMsg }}
            </div>
          </Transition>

          <!-- Hidden fields for Web3Forms -->
          <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY" />
          <input
            type="hidden"
            name="subject"
            :value="form.subject || 'New Contact from Portfolio'" />
          <input
            type="hidden"
            name="from_name"
            value="Portfolio Contact Form" />

          <div class="form-row">
            <div
              class="form-group"
              :class="{ focused: focusState.name || form.name }">
              <label for="c-name">Your Name</label>
              <input
                id="c-name"
                v-model="form.name"
                type="text"
                placeholder="John Doe"
                required
                @focus="focusState.name = true"
                @blur="focusState.name = false" />
            </div>
            <div
              class="form-group"
              :class="{ focused: focusState.email || form.email }">
              <label for="c-email">Your Email</label>
              <input
                id="c-email"
                v-model="form.email"
                type="email"
                placeholder="john@email.com"
                required
                @focus="focusState.email = true"
                @blur="focusState.email = false" />
            </div>
          </div>
          <div
            class="form-group"
            :class="{ focused: focusState.subject || form.subject }">
            <label for="c-subject">Subject</label>
            <input
              id="c-subject"
              v-model="form.subject"
              type="text"
              placeholder="Project Inquiry"
              required
              @focus="focusState.subject = true"
              @blur="focusState.subject = false" />
          </div>
          <div
            class="form-group"
            :class="{ focused: focusState.message || form.message }">
            <label for="c-message">Message</label>
            <textarea
              id="c-message"
              v-model="form.message"
              rows="5"
              placeholder="Tell me about your project..."
              required
              @focus="focusState.message = true"
              @blur="focusState.message = false"></textarea>
          </div>

          <button type="submit" class="submit-btn" :disabled="loading">
            <span class="btn-text">{{
              loading ? "Sending..." : "Send Message"
            }}</span>
            <span class="btn-icon">
              <i
                :class="
                  loading ? 'bi bi-arrow-repeat spin' : 'bi bi-arrow-right'
                "></i>
            </span>
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from "vue";

const loading = ref(false);
const statusMsg = ref("");
const statusType = ref("");

const form = reactive({
  name: "",
  email: "",
  subject: "",
  message: "",
});

const focusState = reactive({
  name: false,
  email: false,
  subject: false,
  message: false,
});

const sendEmail = async () => {
  if (!form.name || !form.email || !form.subject || !form.message) {
    statusMsg.value = "Please fill in all fields.";
    statusType.value = "error";
    return;
  }

  loading.value = true;
  statusMsg.value = "";

  try {
    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        access_key: "YOUR_ACCESS_KEY",
        name: form.name,
        email: form.email,
        subject: form.subject,
        message: form.message,
        to: "oumussa719@gmail.com",
      }),
    });

    const data = await response.json();

    if (data.success) {
      statusMsg.value = "Message sent successfully! I'll get back to you soon.";
      statusType.value = "success";
      form.name = "";
      form.email = "";
      form.subject = "";
      form.message = "";
    } else {
      throw new Error("Failed");
    }
  } catch {
    // Fallback: open mailto
    const mailtoLink = `mailto:oumussa719@gmail.com?subject=${encodeURIComponent(form.subject)}&body=${encodeURIComponent(
      `Name: ${form.name}\nEmail: ${form.email}\n\n${form.message}`,
    )}`;
    window.open(mailtoLink, "_blank");
    statusMsg.value = "Opening your email client as fallback...";
    statusType.value = "success";
  } finally {
    loading.value = false;
    setTimeout(() => {
      statusMsg.value = "";
    }, 6000);
  }
};
</script>

<style scoped>
/* ── Section ── */
.contact {
  position: relative;
  padding: 7rem 2rem;
  background: #f1f5f9;
  overflow: hidden;
}

/* ── Decorative background glows ── */
.bg-glow {
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  filter: blur(150px);
  opacity: 0.18;
  pointer-events: none;
}
.bg-glow--left {
  top: -100px;
  left: -150px;
  background: #6366f1;
}
.bg-glow--right {
  bottom: -100px;
  right: -150px;
  background: #a855f7;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

/* ── Header ── */
.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.label {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: #6366f1;
  display: inline-block;
  margin-bottom: 0.75rem;
  background: rgba(99, 102, 241, 0.08);
  padding: 0.4rem 1rem;
  border-radius: 20px;
  border: 1px solid rgba(99, 102, 241, 0.15);
}

.section-title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 0.75rem;
  letter-spacing: -0.5px;
}

.gradient-text {
  background: linear-gradient(135deg, #818cf8, #a78bfa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-subtitle {
  font-size: 1.05rem;
  color: #64748b;
  max-width: 500px;
  margin: 0 auto 1.25rem;
  line-height: 1.7;
}

.title-line {
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #6366f1, #a855f7);
  border-radius: 2px;
  margin: 0 auto;
}

/* ── Wrapper: two panels ── */
.contact-wrapper {
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  border-radius: 24px;
  overflow: hidden;
  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.08),
    0 0 0 1px rgba(0, 0, 0, 0.04);
}

/* ── Left panel (dark gradient) ── */
.contact-info-panel {
  position: relative;
  background: linear-gradient(160deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
  padding: 3rem 2.5rem;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.info-panel-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(
      circle at 20% 80%,
      rgba(99, 102, 241, 0.15) 0%,
      transparent 50%
    ),
    radial-gradient(
      circle at 80% 20%,
      rgba(168, 85, 247, 0.15) 0%,
      transparent 50%
    );
  pointer-events: none;
}

.info-content {
  position: relative;
  z-index: 1;
}

.info-heading {
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.75rem;
}

.info-desc {
  font-size: 0.92rem;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.7;
  margin-bottom: 2.5rem;
}

/* ── Contact cards ── */
.contact-cards {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin-bottom: 2rem;
}

.contact-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.15rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  cursor: pointer;
  backdrop-filter: blur(10px);
}

.contact-card:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: rgba(255, 255, 255, 0.15);
  transform: translateX(6px);
}

.contact-icon {
  width: 46px;
  height: 46px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
}

.contact-icon i {
  font-size: 1.15rem;
  color: #fff;
}

.card-text {
  flex: 1;
  min-width: 0;
}

.card-label {
  display: block;
  font-size: 0.68rem;
  color: rgba(255, 255, 255, 0.45);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin-bottom: 2px;
}

.card-value {
  display: block;
  font-size: 0.88rem;
  color: #fff;
  font-weight: 600;
}

.card-arrow {
  color: rgba(255, 255, 255, 0.3);
  font-size: 0.85rem;
  transition: all 0.3s ease;
}
.contact-card:hover .card-arrow {
  color: #fff;
  transform: translateX(3px);
}

/* ── Divider ── */
.divider {
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.12),
    transparent
  );
  margin-bottom: 1.5rem;
}

/* ── Socials ── */
.socials {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.social-label {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
}

.social-links {
  display: flex;
  gap: 0.7rem;
}

.social-link {
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  font-size: 1.1rem;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
}

/* Real brand colors */
.social-github {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.15);
}
.social-github:hover {
  background: #333;
  color: #fff;
  border-color: transparent;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(51, 51, 51, 0.35);
}

.social-linkedin {
  color: #0a66c2;
  border-color: rgba(10, 102, 194, 0.2);
}
.social-linkedin:hover {
  background: #0a66c2;
  color: #fff;
  border-color: transparent;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(10, 102, 194, 0.35);
}

.social-twitter {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.15);
}
.social-twitter:hover {
  background: #000;
  color: #fff;
  border-color: transparent;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.social-facebook {
  color: #1877f2;
  border-color: rgba(24, 119, 242, 0.2);
}
.social-facebook:hover {
  background: #1877f2;
  color: #fff;
  border-color: transparent;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(24, 119, 242, 0.35);
}

/* ── Decorative circles ── */
.deco-circle {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.05);
  pointer-events: none;
}
.deco-circle--lg {
  width: 250px;
  height: 250px;
  bottom: -80px;
  right: -80px;
  background: radial-gradient(
    circle,
    rgba(99, 102, 241, 0.08),
    transparent 70%
  );
}
.deco-circle--sm {
  width: 120px;
  height: 120px;
  top: -40px;
  right: -30px;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.1), transparent 70%);
}

/* ── Right form panel ── */
.contact-form {
  background: #fff;
  padding: 3rem 2.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}

.form-group {
  margin-bottom: 1.4rem;
  position: relative;
}

.form-group label {
  display: block;
  font-size: 0.78rem;
  font-weight: 700;
  color: #94a3b8;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: color 0.3s ease;
}

.form-group.focused label {
  color: #6366f1;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.85rem 1.15rem;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 0.92rem;
  color: #1e293b;
  background: #f8fafc;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  outline: none;
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: #cbd5e1;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.08);
}

.form-group textarea {
  resize: vertical;
  min-height: 130px;
}

/* ── Submit button ── */
.submit-btn {
  display: inline-flex;
  align-items: center;
  gap: 0;
  padding: 0;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  border: none;
  border-radius: 14px;
  font-size: 0.92rem;
  font-weight: 650;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  position: relative;
}

.btn-text {
  padding: 0.9rem 1.6rem;
}

.btn-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 100%;
  background: rgba(255, 255, 255, 0.15);
  padding: 0.9rem 0;
  transition: all 0.35s ease;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(99, 102, 241, 0.35);
}

.submit-btn:hover:not(:disabled) .btn-icon {
  background: rgba(255, 255, 255, 0.25);
}

.submit-btn:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

.spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* ── Status message ── */
.status-msg {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.9rem 1.15rem;
  border-radius: 12px;
  font-size: 0.88rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.status-msg.success {
  background: #ecfdf5;
  color: #059669;
  border: 1px solid #a7f3d0;
}

.status-msg.error {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

/* Vue transition */
.slide-fade-enter-active {
  transition: all 0.35s ease-out;
}
.slide-fade-leave-active {
  transition: all 0.25s ease-in;
}
.slide-fade-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .contact-wrapper {
    grid-template-columns: 1fr;
  }

  .contact-info-panel {
    padding: 2.5rem 2rem;
  }

  .contact-form {
    padding: 2.5rem 2rem;
  }

  .deco-circle--lg,
  .deco-circle--sm {
    display: none;
  }
}

@media (max-width: 768px) {
  .contact {
    padding: 4.5rem 1.25rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .contact-form {
    padding: 2rem 1.5rem;
  }

  .contact-info-panel {
    padding: 2rem 1.5rem;
  }
}
</style>
