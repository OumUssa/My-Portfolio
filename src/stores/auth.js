import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useAuthStore = defineStore("Auth", () => {
  const user = ref(null);
  const token = ref(localStorage.getItem("token") || null);

  const isAuthenticated = computed(() => !!token.value);

  const setToken = (newToken) => {
    if (newToken) {
      token.value = newToken;
      localStorage.setItem("token", newToken);
    } else {
      localStorage.removeItem("token");
    }
  };

  const setUser = (newUser) => {
    user.value = newUser;
  };

  const login = async ({ username, password } = {}) => {
    try {
      const body = { username, name: username, password };

      const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://portfolio.cms-jubpet.linkpc.net";
      const res = await fetch(`${API_BASE_URL}/api/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });

      const data = await res.json();
      console.log("login response:", data);

      if (!res.ok) {
        throw new Error(
          data.message || data.error || `Login failed (${res.status})`,
        );
      }

      if (data.token) {
        setToken(data.token);
      }

      const nextUser = data.data || data.user || null;
      setUser(nextUser);

      return data;
    } catch (err) {
      throw err;
    }
  };
  const logout = async () => {
    try {
      setToken(null);
      setUser(null);
      return { result: true };
    } catch (err) {
      throw err.message;
    }
  };

  return { user, token, isAuthenticated, login, logout };
});
