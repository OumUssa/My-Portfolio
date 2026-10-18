<template>
  <div ref="root" class="as" :class="{ open, up, disabled }" @keydown="onKey">
    <button
      type="button"
      class="as-trigger"
      :disabled="disabled"
      aria-haspopup="listbox"
      :aria-expanded="open"
      @click="toggle">
      <span class="as-value" :class="{ 'as-placeholder': !displayText }">
        {{ displayText || placeholder }}
      </span>
      <span v-if="multiple && selectedList.length" class="as-count">{{ selectedList.length }}</span>
      <i class="bi bi-chevron-down as-chevron"></i>
    </button>

    <transition name="as-pop">
      <div v-if="open" class="as-menu" role="listbox">
        <div v-if="!options.length" class="as-empty">{{ emptyText }}</div>
        <button
          v-for="(opt, i) in options"
          :key="opt.value"
          type="button"
          role="option"
          class="as-option"
          :class="{ active: i === highlighted, selected: isSelected(opt) }"
          :aria-selected="isSelected(opt)"
          @mouseenter="highlighted = i"
          @click="choose(opt)">
          <span class="as-label">{{ opt.label }}</span>
          <i v-if="isSelected(opt)" class="bi bi-check2 as-check"></i>
        </button>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from "vue";

const props = defineProps({
  modelValue: { type: [String, Number, Array], default: "" },
  multiple: { type: Boolean, default: false },
  options: { type: Array, default: () => [] }, // [{ value, label }]
  placeholder: { type: String, default: "Select..." },
  emptyText: { type: String, default: "No options" },
  disabled: { type: Boolean, default: false },
});

const emit = defineEmits(["update:modelValue"]);

const root = ref(null);
const open = ref(false);
const up = ref(false);
const highlighted = ref(-1);

const selected = computed(() => props.options.find((o) => o.value === props.modelValue) || null);

const selectedList = computed(() =>
  props.multiple && Array.isArray(props.modelValue)
    ? props.options.filter((o) => props.modelValue.includes(o.value))
    : [],
);

const displayText = computed(() => {
  if (!props.multiple) return selected.value ? selected.value.label : "";
  const list = selectedList.value;
  if (!list.length) return "";
  return list.length <= 2 ? list.map((o) => o.label).join(", ") : `${list[0].label}, ${list[1].label} +${list.length - 2}`;
});

function isSelected(opt) {
  return props.multiple
    ? Array.isArray(props.modelValue) && props.modelValue.includes(opt.value)
    : opt.value === props.modelValue;
}

function openMenu() {
  if (props.disabled) return;
  const rect = root.value.getBoundingClientRect();
  const needed = Math.min(props.options.length, 6) * 40 + 16;
  up.value = window.innerHeight - rect.bottom < needed && rect.top > needed;
  highlighted.value = Math.max(0, props.options.findIndex((o) => isSelected(o)));
  open.value = true;
  nextTick(() => root.value?.querySelector(".as-option.active")?.scrollIntoView({ block: "nearest" }));
}

function close() {
  open.value = false;
}

function toggle() {
  open.value ? close() : openMenu();
}

function choose(opt) {
  if (props.multiple) {
    const current = Array.isArray(props.modelValue) ? props.modelValue : [];
    emit(
      "update:modelValue",
      current.includes(opt.value) ? current.filter((v) => v !== opt.value) : [...current, opt.value],
    );
    close();
    return;
  }
  emit("update:modelValue", opt.value);
  close();
}

function onKey(e) {
  if (e.key === "Escape" && open.value) {
    e.stopPropagation();
    close();
    return;
  }
  if (!["ArrowDown", "ArrowUp", "Enter"].includes(e.key)) return;
  if (!open.value) {
    if (e.key !== "Enter") {
      e.preventDefault();
      openMenu();
    }
    return;
  }
  e.preventDefault();
  const n = props.options.length;
  if (!n) return;
  if (e.key === "ArrowDown") highlighted.value = (highlighted.value + 1) % n;
  else if (e.key === "ArrowUp") highlighted.value = (highlighted.value - 1 + n) % n;
  else if (props.options[highlighted.value]) choose(props.options[highlighted.value]);
  nextTick(() => root.value?.querySelector(".as-option.active")?.scrollIntoView({ block: "nearest" }));
}

function onOutside(e) {
  if (open.value && root.value && !root.value.contains(e.target)) close();
}

onMounted(() => document.addEventListener("pointerdown", onOutside));
onBeforeUnmount(() => document.removeEventListener("pointerdown", onOutside));
</script>

<style>
.as {
  --as-bg: #f8fafc;
  --as-bg-open: #ffffff;
  --as-border: rgba(148, 163, 184, 0.35);
  --as-text: #0f172a;
  --as-muted: #94a3b8;
  --as-menu: rgba(255, 255, 255, 0.82);
  --as-menu-border: rgba(226, 232, 240, 0.9);
  --as-hover: rgba(99, 102, 241, 0.1);
  position: relative;
  width: 100%;
}

[data-bs-theme="dark"] .as {
  --as-bg: #0f172a;
  --as-bg-open: #0f172a;
  --as-border: #334155;
  --as-text: #e2e8f0;
  --as-muted: #64748b;
  --as-menu: rgba(30, 41, 59, 0.85);
  --as-menu-border: #334155;
  --as-hover: rgba(129, 140, 248, 0.18);
}

.as-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid var(--as-border);
  background: var(--as-bg);
  color: var(--as-text);
  font: inherit;
  font-size: 14px;
  text-align: left;
  cursor: pointer;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease, transform 0.12s ease;
}

.as-trigger:hover { border-color: #818cf8; }
.as-trigger:active { transform: scale(0.99); }

.as.open .as-trigger {
  border-color: #6366f1;
  background: var(--as-bg-open);
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
}

.as.disabled .as-trigger { opacity: 0.55; cursor: not-allowed; }

.as-value { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.as-value.as-placeholder { color: var(--as-muted); }

.as-count {
  margin-left: auto;
  min-width: 20px;
  padding: 1px 7px;
  border-radius: 999px;
  background: #6366f1;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  text-align: center;
}

.as-chevron {
  font-size: 12px;
  color: var(--as-muted);
  transition: transform 0.28s cubic-bezier(0.3, 1.4, 0.5, 1), color 0.2s;
}
.as.open .as-chevron { transform: rotate(180deg); color: #6366f1; }

.as-menu {
  position: absolute;
  left: 0;
  right: 0;
  top: calc(100% + 8px);
  z-index: 80;
  max-height: 260px;
  overflow-y: auto;
  padding: 6px;
  border-radius: 14px;
  background: var(--as-menu);
  border: 1px solid var(--as-menu-border);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  box-shadow: 0 18px 50px rgba(15, 23, 42, 0.22), 0 2px 6px rgba(15, 23, 42, 0.08);
  transform-origin: top center;
}

.as.up .as-menu { top: auto; bottom: calc(100% + 8px); transform-origin: bottom center; }

.as-option {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 9px 12px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  color: var(--as-text);
  font: inherit;
  font-size: 14px;
  text-align: left;
  cursor: pointer;
  transition: background 0.12s ease;
}

.as-option.active { background: var(--as-hover); }
.as-option.selected { font-weight: 600; color: #6366f1; }
[data-bs-theme="dark"] .as-option.selected { color: #a5b4fc; }
.as-check { font-size: 16px; }

.as-empty { padding: 12px; font-size: 13px; color: var(--as-muted); text-align: center; }

.as-pop-enter-active { transition: opacity 0.2s ease, transform 0.28s cubic-bezier(0.2, 1.1, 0.3, 1); }
.as-pop-leave-active { transition: opacity 0.12s ease, transform 0.12s ease; }
.as-pop-enter-from,
.as-pop-leave-to { opacity: 0; transform: scale(0.94) translateY(-6px); }
.as.up .as-pop-enter-from,
.as.up .as-pop-leave-to { transform: scale(0.94) translateY(6px); }

@media (prefers-reduced-motion: reduce) {
  .as-trigger, .as-chevron, .as-pop-enter-active, .as-pop-leave-active { transition: none; }
}
</style>
