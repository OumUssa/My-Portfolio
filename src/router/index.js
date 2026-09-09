import AboutMe from "@/components/pages/AboutMe.vue";
import Home from "@/components/pages/Home.vue";
import { createRouter, createWebHistory } from "vue-router";
import detail from "@/components/pages/detail.vue";
import Login from "@/components/pages/Login.vue";
import Admin from "@/components/pages/Admin.vue";

// Note: App.vue is the root app shell (mounted once in main.js) and must never
// also be used as a route `component` — doing so instantiates it a second
// time per page (duplicate Header, duplicate global listeners/animations).
// Routes here are intentionally flat; only "/Home" relies on the "/" redirect.
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/admin",
      name: "Admin",
      component: Admin,
      meta: { requiresAdmin: true },
    },
    {
      path: "/",
      redirect: "/Home",
    },
    {
      path: "/Home",
      name: "Home",
      component: Home,
    },
    {
      path: "/About-Me",
      component: AboutMe,
      name: "About-Me",
    },
    {
      path: "/detail/:id",
      component: detail,
      name: "detail",
      props: true,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

// Simple auth/admin guard:
router.beforeEach(async (to, from, next) => {
  const requiresAdmin = to.matched.some((r) => r.meta && r.meta.requiresAdmin);
  const requiresAuth = to.matched.some((r) => r.meta && r.meta.requiresAuth);
  const token = localStorage.getItem("token");
  let isAuthenticated = !!token;

  if (isAuthenticated && (requiresAdmin || requiresAuth)) {
    try {
      // Decode JWT payload (middle part of the token)
      const payloadBase64 = token.split('.')[1];
      const decodedJson = atob(payloadBase64);
      const decoded = JSON.parse(decodedJson);
      
      const exp = decoded.exp;
      const currentTime = Math.floor(Date.now() / 1000);
      
      // If token is expired, remove it
      if (exp && exp < currentTime) {
        isAuthenticated = false;
        localStorage.removeItem("token");
      }
    } catch (e) {
      isAuthenticated = false;
      localStorage.removeItem("token");
    }
  }

  if (requiresAdmin) {
    if (!isAuthenticated)
      return next("/");
    return next();
  }

  if (requiresAuth && !isAuthenticated) {
    return next("/");
  }

  next();
});

export default router;
