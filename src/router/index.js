import App from "@/App.vue";
import AboutMe from "@/components/pages/AboutMe.vue";
import Home from "@/components/pages/Home.vue";
import { createRouter, createWebHistory } from "vue-router";
import detail from "@/components/pages/detail.vue";
import Login from "@/components/pages/Login.vue";
import Admin from "@/components/pages/Admin.vue";

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
      component: App,
      redirect: "/Home",
      children: [
        {
          path: "Home",
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
router.beforeEach((to, from, next) => {
  const requiresAdmin = to.matched.some((r) => r.meta && r.meta.requiresAdmin);
  const requiresAuth = to.matched.some((r) => r.meta && r.meta.requiresAuth);
  const token = localStorage.getItem("token");
  const isAuthenticated = !!token;

  if (requiresAdmin) {
    if (!isAuthenticated)
      return next({ path: "/login", query: { redirect: to.fullPath } });
    return next();
  }

  if (requiresAuth && !isAuthenticated) {
    return next({ path: "/login", query: { redirect: to.fullPath } });
  }

  next();
});

export default router;
