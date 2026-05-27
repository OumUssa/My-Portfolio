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
    if (newUser) {
      localStorage.setItem("user", JSON.stringify(newUser));
    } else {
      localStorage.removeItem("user");
    }
  };

  const login = async ({ username, password } = {}) => {
    try {
      const body = { username, name: username, password };

      const res = await fetch("/api/auth/login", {
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
          data.message ||
            data.error ||
            `Login failed (${res.status})`,
        );
      }

      if (data.token) {
        setToken(data.token);
      }

      const nextUser = data.data || data.user || null;
      setUser(nextUser);

      localStorage.setItem("auth", data.token ? "true" : "false");

      return data;
    } catch (err) {
      throw err;
    }
  };
  const logout = async () => {
    try {
      setToken(null);
      setUser(null);
      localStorage.removeItem("auth");
      return { result: true };
    } catch (err) {
      throw err.message;
    }
  };

  return { user, token, isAuthenticated, login, logout };
});
