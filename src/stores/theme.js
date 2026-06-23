import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  const isDark = ref(localStorage.getItem('theme') === 'dark');

  const toggleTheme = () => {
    isDark.value = !isDark.value;
    const theme = isDark.value ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-bs-theme', theme);
  };

  const initTheme = () => {
    const theme = isDark.value ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', theme);
  };

  return { isDark, toggleTheme, initTheme };
});
