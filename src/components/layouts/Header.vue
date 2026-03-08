<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="navbar-container">
      <div class="logo">
        <a href="/">
          <i class="bi bi-code-slash"></i>
          <span>Portfolio</span>
        </a>
      </div>
      <ul class="nav-menu" :class="{ active: mobileMenuOpen }">
        <!-- Animated pill indicator -->
        <li class="nav-pill" ref="pillRef"></li>
        <li
          v-for="link in navLinks"
          :key="link.id"
          class="nav-item"
          ref="navItemRefs">
          <a
            href="#"
            class="nav-link"
            :class="{ 'active-link': activeSection === link.id }"
            @click.prevent="onNavClick(link.id)">
            {{ link.label }}
          </a>
        </li>
      </ul>
      <div
        class="hamburger"
        :class="{ active: mobileMenuOpen }"
        @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();

const navLinks = [
  { id: "home", label: "Home" },
  { id: "about", label: "About Me" },
  { id: "projects", label: "Projects" },
  { id: "services", label: "Services" },
  { id: "contact", label: "Contact" },
];

const mobileMenuOpen = ref(false);
const isScrolled = ref(false);
const activeSection = ref("home");
const pillRef = ref(null);
const navItemRefs = ref([]);

const toggleMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const scrollToSection = (id) => {
  // Add a small delay to ensure DOM is fully rendered after route change
  setTimeout(() => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  }, 300);
};

const onNavClick = (id) => {
  mobileMenuOpen.value = false;
  activeSection.value = id;

  if (id === "about") {
    router.push("/About-Me");
  } else if (id === "home") {
    router.push("/Home").then(() => {
      scrollToSection("home");
    });
  } else {
    // For projects, services, contact - go to home first then scroll
    router.push("/Home").then(() => {
      scrollToSection(id);
    });
  }
};

// Move pill indicator to the active nav item
const movePill = () => {
  if (!pillRef.value || !navItemRefs.value.length) return;
  const idx = navLinks.findIndex((l) => l.id === activeSection.value);
  const activeEl = navItemRefs.value[idx];
  if (!activeEl) return;
  const linkEl = activeEl.querySelector ? activeEl : activeEl.$el;
  if (!linkEl) return;
  pillRef.value.style.width = linkEl.offsetWidth + "px";
  pillRef.value.style.left = linkEl.offsetLeft + "px";
};

// Scroll spy — detect which section is visible
const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;

  // Don't run scroll spy on About Me page
  if (route.path === "/About-Me") return;

  const sections = navLinks
    .map((l) => document.getElementById(l.id))
    .filter(Boolean);
  const scrollPos = window.scrollY + 120;

  for (let i = sections.length - 1; i >= 0; i--) {
    if (sections[i].offsetTop <= scrollPos) {
      activeSection.value = sections[i].id;
      break;
    }
  }
};

// Sync activeSection with current route
watch(
  () => route.path,
  (path) => {
    if (path === "/About-Me") {
      activeSection.value = "about";
    } else if (path === "/Home" || path === "/") {
      activeSection.value = "home";
    }
  },
  { immediate: true },
);

watch(activeSection, () => {
  nextTick(movePill);
});

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
  nextTick(movePill);
  // Reposition pill on resize
  window.addEventListener("resize", movePill);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
  window.removeEventListener("resize", movePill);
});
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 1.2rem 0;
  transition: all 0.35s ease;
}

.navbar.scrolled {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  box-shadow: 0 1px 20px rgba(0, 0, 0, 0.08);
  padding: 0.8rem 0;
}

.navbar.scrolled .logo a,
.navbar.scrolled .nav-link {
  color: #1e293b;
}

.navbar.scrolled .nav-pill {
  background: #6366f1;
}

.navbar.scrolled .nav-link.active-link {
  color: #fff;
}

.navbar.scrolled .hamburger span {
  background: #1e293b;
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  width: 100%;
}

.logo a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.5rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  letter-spacing: -0.5px;
  transition: color 0.3s ease;
}

.logo a i {
  font-size: 1.6rem;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: 0.3rem;
  margin: 0;
  padding: 0;
  position: relative;
}

/* ── Animated pill indicator ── */
.nav-pill {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  height: 36px;
  background: rgba(255, 255, 255, 0.18);
  border-radius: 50px;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
  z-index: 0;
}

.nav-item {
  position: relative;
  z-index: 1;
}

.nav-link {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 500;
  padding: 0.45rem 1.1rem;
  border-radius: 50px;
  transition: color 0.3s ease;
  display: block;
  white-space: nowrap;
}

.nav-link:hover {
  color: #fff;
}

.nav-link.active-link {
  color: #fff;
}

.hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
  gap: 5px;
  padding: 4px;
}

.hamburger span {
  width: 24px;
  height: 2.5px;
  background: #fff;
  border-radius: 4px;
  transition: all 0.3s ease;
  transform-origin: center;
}

.hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav-pill {
    display: none;
  }

  .nav-menu {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    flex-direction: column;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    padding: 5rem 2rem 2rem;
    gap: 0.5rem;
    transition: right 0.35s ease;
    box-shadow: -5px 0 30px rgba(0, 0, 0, 0.1);
  }

  .nav-menu.active {
    right: 0;
  }

  .nav-link {
    color: #334155;
    font-size: 1rem;
    padding: 0.8rem 1.2rem;
    border-radius: 12px;
  }

  .nav-link:hover,
  .nav-link.active-link {
    background: #6366f1;
    color: #fff;
  }

  .navbar-container {
    padding: 0 1.2rem;
  }
}
</style>
