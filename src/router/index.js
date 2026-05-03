import App from "@/App.vue";
import AboutMe from "@/components/pages/AboutMe.vue";
import Home from "@/components/pages/Home.vue";
import { createRouter, createWebHistory } from "vue-router";
import detail from "@/components/pages/detail.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
          path:"/detail/:id",
          component: detail,
          name:"detail",
          props:true
        }
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

export default router;
