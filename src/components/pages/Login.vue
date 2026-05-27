<template>
  <div class="login-wrapper">
    <div class="glass-card">
      <h2 class="title">Admin Login</h2>
      <p class="subtitle">Sign in to manage projects and categories</p>
      <p v-if="error" class="error">{{ error }}</p>
      <form @submit.prevent="submit" class="form">
        <div class="field">
          <label>Username</label>
          <input
            v-model="username"
            type="text"
            required
            autocomplete="username" />
        </div>
        <div class="field">
          <label>Password</label>
          <input
            v-model="password"
            type="password"
            required
            autocomplete="current-password" />
        </div>
        <button type="submit" class="submit" :disabled="loading">
          {{ loading ? "Signing in..." : "Sign in" }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const route = useRoute();
const auth = useAuthStore();
const username = ref("");
const password = ref("");
const error = ref("");
const loading = ref(false);

async function submit() {
  error.value = "";
  loading.value = true;
  try {
    const res = await auth.login({
      username: username.value,
      password: password.value
    });
    

    const redirect = route.query.redirect || "/admin";

    router.push(redirect);

  } catch (e) {
    console.error(e);
    error.value = e.message || "Login failed";
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.login-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0f172a 0%, #071029 100%);
}
.glass-card {
  width: 380px;
  padding: 28px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 8px 30px rgba(2, 6, 23, 0.6);
  backdrop-filter: blur(10px) saturate(120%);
  color: #e6eef8;
}
.title {
  margin: 0 0 6px 0;
  font-size: 20px;
  text-align: center;
}
.subtitle {
  margin: 0 0 14px 0;
  font-size: 13px;
  color: #a9c0d9;
  text-align: center;
}
.form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.field label {
  display: block;
  font-size: 13px;
  margin-bottom: 6px;
  color: #cfe2ff;
}
.field input {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.02);
  color: #e6eef8;
}
.submit {
  margin-top: 6px;
  padding: 10px;
  border-radius: 10px;
  border: none;
  background: linear-gradient(90deg, #3b82f6, #06b6d4);
  color: white;
  font-weight: 600;
  cursor: pointer;
}
.error {
  color: #ffb4b4;
  background: rgba(255, 80, 80, 0.06);
  padding: 8px;
  border-radius: 8px;
  text-align: center;
  margin-bottom: 4px;
}
</style>
