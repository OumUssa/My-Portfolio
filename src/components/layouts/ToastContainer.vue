<template>
  <div class="toast-stack" aria-live="polite">
    <transition-group name="toast">
      <div
        v-for="t in toast.toasts"
        :key="t.id"
        class="toast"
        :class="t.type"
        role="status"
        @click="toast.remove(t.id)">
        <span class="toast-icon">
          <i :class="icons[t.type]"></i>
        </span>
        <div class="toast-body">
          <strong>{{ titles[t.type] }}</strong>
          <p>{{ t.message }}</p>
        </div>
        <button class="toast-close" aria-label="Dismiss" @click.stop="toast.remove(t.id)">
          <i class="bi bi-x-lg"></i>
        </button>
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { useToastStore } from "@/stores/toast";

const toast = useToastStore();

const icons = {
  success: "bi bi-check-circle-fill",
  error: "bi bi-x-circle-fill",
  info: "bi bi-info-circle-fill",
};

const titles = {
  success: "Success",
  error: "Failed",
  info: "Notice",
};
</script>

<style scoped>
.toast-stack {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: min(380px, calc(100vw - 32px));
  pointer-events: none;
}

.toast {
  --accent: #6366f1;
  pointer-events: auto;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 14px 14px 16px;
  border-radius: 14px;
  background: #ffffff;
  color: #0f172a;
  border: 1px solid #e2e8f0;
  border-left: 4px solid var(--accent);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.18);
  cursor: pointer;
}

.toast.success { --accent: #10b981; }
.toast.error { --accent: #ef4444; }

.toast-icon {
  font-size: 20px;
  line-height: 1;
  color: var(--accent);
  margin-top: 2px;
}

.toast-body { flex: 1; min-width: 0; }

.toast-body strong {
  display: block;
  font-size: 14px;
  font-weight: 700;
}

.toast-body p {
  margin: 2px 0 0;
  font-size: 13px;
  line-height: 1.45;
  color: #475569;
  word-break: break-word;
}

.toast-close {
  border: 0;
  background: transparent;
  color: #94a3b8;
  cursor: pointer;
  font-size: 12px;
  padding: 2px;
}

.toast-close:hover { color: #0f172a; }

.toast-enter-active,
.toast-leave-active { transition: all 0.3s ease; }
.toast-enter-from { opacity: 0; transform: translateX(40px); }
.toast-leave-to { opacity: 0; transform: translateX(40px) scale(0.95); }
.toast-move { transition: transform 0.3s ease; }
</style>
