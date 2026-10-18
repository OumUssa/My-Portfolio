import { defineStore } from "pinia";
import { ref } from "vue";

let nextId = 1;

export const useToastStore = defineStore("Toast", () => {
  const toasts = ref([]);

  const remove = (id) => {
    toasts.value = toasts.value.filter((t) => t.id !== id);
  };

  const push = (type, message, duration = 4000) => {
    const id = nextId++;
    toasts.value.push({ id, type, message });
    if (duration > 0) setTimeout(() => remove(id), duration);
    return id;
  };

  const success = (message, duration) => push("success", message, duration);
  const error = (message, duration = 5500) => push("error", message, duration);
  const info = (message, duration) => push("info", message, duration);

  return { toasts, remove, push, success, error, info };
});
