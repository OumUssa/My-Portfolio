<template>
  <section id="contact" class="contact">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Get In Touch</span>
        <h2 class="section-title">Let's Work Together</h2>
        <p class="section-desc">
          Have a project in mind or just want to say hello? I'd love to hear from you.
        </p>
      </div>

      <div class="contact-grid">
        <div class="info-panel">
          <h3>Contact Information</h3>
          <p class="info-desc">Fill up the form and I'll get back to you within 24 hours.</p>

          <div class="info-list">
            <a href="mailto:oumussa719@gmail.com" class="info-item">
              <i class="bi bi-envelope"></i>
              <div>
                <span class="info-label">Email</span>
                <span class="info-value">oumussa719@gmail.com</span>
              </div>
            </a>
            <a href="tel:+1234567890" class="info-item">
              <i class="bi bi-telephone"></i>
              <div>
                <span class="info-label">Phone</span>
                <span class="info-value">+1 234 567 890</span>
              </div>
            </a>
            <div class="info-item">
              <i class="bi bi-geo-alt"></i>
              <div>
                <span class="info-label">Location</span>
                <span class="info-value">Your City, Country</span>
              </div>
            </div>
          </div>

          <div class="social-row">
            <a href="#" aria-label="GitHub"><i class="bi bi-github"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
            <a href="#" aria-label="Twitter"><i class="bi bi-twitter-x"></i></a>
            <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
          </div>
        </div>

        <form class="form-panel" @submit.prevent="sendEmail">
          <Transition name="slide">
            <div v-if="statusMsg" class="status" :class="statusType">
              <i :class="statusType === 'success' ? 'bi bi-check-circle-fill' : 'bi bi-exclamation-circle-fill'"></i>
              {{ statusMsg }}
            </div>
          </Transition>

          <div class="form-row">
            <div class="field">
              <label for="c-name">Your Name</label>
              <input id="c-name" v-model="form.name" type="text" placeholder="John Doe" required />
            </div>
            <div class="field">
              <label for="c-email">Your Email</label>
              <input id="c-email" v-model="form.email" type="email" placeholder="john@email.com" required />
            </div>
          </div>
          <div class="field">
            <label for="c-subject">Subject</label>
            <input id="c-subject" v-model="form.subject" type="text" placeholder="Project Inquiry" required />
          </div>
          <div class="field">
            <label for="c-message">Message</label>
            <textarea id="c-message" v-model="form.message" rows="5" placeholder="Tell me about your project..." required></textarea>
          </div>

          <button type="submit" class="submit-btn" :disabled="loading">
            {{ loading ? "Sending..." : "Send Message" }}
            <i :class="loading ? 'bi bi-arrow-repeat spin' : 'bi bi-arrow-right'"></i>
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
    const mailtoLink = `mailto:oumussa719@gmail.com?subject=${encodeURIComponent(form.subject)}&body=${encodeURIComponent(`Name: ${form.name}\nEmail: ${form.email}\n\n${form.message}`)}`;
    window.open(mailtoLink, "_blank");
    statusMsg.value = "Opening your email client as fallback...";
    statusType.value = "success";
  } finally {
    loading.value = false;
    setTimeout(() => { statusMsg.value = ""; }, 6000);
  }
};
</script>

<style scoped>
.contact {
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
  margin-bottom: 0.5rem;
}

.section-desc {
  font-size: 0.95rem;
  color: #64748b;
  max-width: 460px;
  margin: 0 auto;
  line-height: 1.6;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
  background: #fff;
}

/* Info Panel */
.info-panel {
  background: #0a0a1a;
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
}

.info-panel h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
}

.info-desc {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.45);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: auto;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 0.75rem;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  text-decoration: none;
  transition: background 0.2s ease;
}

.info-item:hover {
  background: rgba(255, 255, 255, 0.08);
}

.info-item i {
  font-size: 1rem;
  color: #818cf8;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(99, 102, 241, 0.15);
  border-radius: 8px;
  flex-shrink: 0;
}

.info-label {
  display: block;
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.35);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

.info-value {
  display: block;
  font-size: 0.85rem;
  color: #fff;
  font-weight: 500;
}

.social-row {
  display: flex;
  gap: 0.5rem;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.social-row a {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  color: #94a3b8;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.social-row a:hover {
  background: #6366f1;
  color: #fff;
  border-color: transparent;
}

/* Form Panel */
.form-panel {
  padding: 2.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.field {
  margin-bottom: 1.25rem;
}

.field label {
  display: block;
  font-size: 0.75rem;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 0.4rem;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.field input,
.field textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.88rem;
  color: #1e293b;
  background: #f8fafc;
  transition: all 0.2s ease;
  font-family: inherit;
  outline: none;
}

.field input::placeholder,
.field textarea::placeholder {
  color: #cbd5e1;
}

.field input:focus,
.field textarea:focus {
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.06);
}

.field textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6366f1;
  color: #fff;
  font-size: 0.88rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.submit-btn:hover:not(:disabled) {
  background: #4f46e5;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1.25rem;
}

.status.success {
  background: #ecfdf5;
  color: #059669;
  border: 1px solid #a7f3d0;
}

.status.error {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

.slide-enter-active { transition: all 0.3s ease; }
.slide-leave-active { transition: all 0.2s ease; }
.slide-enter-from { opacity: 0; transform: translateY(-8px); }
.slide-leave-to { opacity: 0; }

@media (max-width: 900px) {
  .contact-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  .contact { padding: 4rem 1.5rem; }
  .section-title { font-size: 1.8rem; }
  .form-row { grid-template-columns: 1fr; }
  .form-panel { padding: 2rem 1.5rem; }
  .info-panel { padding: 2rem 1.5rem; }
}
</style>
