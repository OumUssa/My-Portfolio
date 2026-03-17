<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="navbar-inner w-100">
      <a href="/" class="logo " @click.prevent="onNavClick('home')">
        Oum<span class="logo-accent">.</span>
      </a>

      <ul class="nav-links" :class="{ open: menuOpen }">
        <li v-for="link in navLinks" :key="link.id">
          <a
            href="#"
            class="nav-link"
            :class="{ active: activeSection === link.id }"
            @click.prevent="onNavClick(link.id)">
            {{ link.label }}
          </a>
        </li>
      </ul>
      <button
        class="menu-toggle"
        :class="{ open: menuOpen }"
        @click="menuOpen = !menuOpen"
        aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const navLinks = [
  { id: "home", label: "Home" },
  { id: "about", label: "About" },
  { id: "projects", label: "Projects" },
  { id: "services", label: "Services" },
  { id: "contact", label: "Contact" },
];

const menuOpen = ref(false);
const isScrolled = ref(false);
const activeSection = ref("home");
let pendingSection = null;

const sectionIds = ["home", "projects", "services", "contact"];

const updateActiveFromScroll = () => {
  if (pendingSection) return;
  if (route.path !== "/Home" && route.path !== "/") return;

  const offset = 150;
  let current = "home";
  for (const id of sectionIds) {
    const el = document.getElementById(id);
    if (el && el.getBoundingClientRect().top <= offset) {
      current = id;
    }
  }
  activeSection.value = current;
};

const scrollToSection = (id) => {
  nextTick(() => {
    setTimeout(() => {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: "smooth" });
        setTimeout(() => {
          pendingSection = null;
        }, 800);
      }
    }, 100);
  });
};

const onNavClick = (id) => {
  menuOpen.value = false;
  activeSection.value = id;

  if (id === "about") {
    router.push("/About-Me");
  } else if (route.path === "/Home" || route.path === "/") {
    scrollToSection(id);
  } else {
    pendingSection = id;
    router.push("/Home").then(() => scrollToSection(id));
  }
};

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
  updateActiveFromScroll();
};

watch(
  () => route.path,
  (path) => {
    if (pendingSection) {
      activeSection.value = pendingSection;
      return;
    }
    if (path === "/About-Me") {
      activeSection.value = "about";
    } else if (path === "/Home" || path === "/") {
      if (!pendingSection) activeSection.value = "home";
    }
  },
  { immediate: true },
);

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
  handleScroll();
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 0.85rem 0;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease;
}

.navbar.scrolled {
  background: rgba(255, 255, 255, 0.95);
  padding: 0.65rem 0;
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.06);
  border-bottom-color: rgba(0, 0, 0, 0.06);
}

.navbar-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  font-size: 1.35rem;
  font-weight: 700;
  color: #1e293b;
  text-decoration: none;
  letter-spacing: -0.5px;
}

.logo-accent {
  color: #6366f1;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
  margin: 0;
  padding: 0;
  align-items: center;
}

.nav-link {
  color: #64748b;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.45rem 0.9rem;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.nav-link:hover {
  color: #1e293b;
  background: rgba(99, 102, 241, 0.04);
}

.nav-link.active {
  color: #6366f1;
  background: rgba(99, 102, 241, 0.08);
  font-weight: 600;
}

.cta-btn {
  padding: 0.5rem 1.2rem;
  background: #6366f1;
  color: #fff;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.cta-btn:hover {
  background: #4f46e5;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.cta-desktop {
  display: inline-block;
}

.nav-cta-mobile {
  display: none;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
}

.menu-toggle span {
  width: 20px;
  height: 2px;
  background: #1e293b;
  border-radius: 2px;
  transition: all 0.3s ease;
  transform-origin: center;
}

.menu-toggle.open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}
.menu-toggle.open span:nth-child(2) {
  opacity: 0;
}
.menu-toggle.open span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
  }

  .cta-desktop {
    display: none;
  }

  .nav-cta-mobile {
    display: block;
    margin-top: 0.5rem;
    padding-top: 0.75rem;
    border-top: 1px solid #f1f5f9;
  }

  .nav-cta-mobile .cta-btn {
    display: block;
    text-align: center;
    padding: 0.75rem;
  }

  .nav-links {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100dvh;
    flex-direction: column;
    align-items: stretch;
    background: #fff;
    padding: 5rem 1.5rem 2rem;
    gap: 0.15rem;
    transition: right 0.3s ease;
    box-shadow: -10px 0 30px rgba(0, 0, 0, 0.1);
  }

  .nav-links.open {
    right: 0;
  }

  .nav-link {
    font-size: 0.95rem;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    color: #64748b;
  }

  .nav-link:hover,
  .nav-link.active {
    color: #6366f1;
    background: rgba(99, 102, 241, 0.06);
  }
}
</style>
