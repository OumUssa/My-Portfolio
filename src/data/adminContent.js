function normalizeCategoryName(value) {
  return String(value || "General Stack").trim() || "General Stack";
}

function todayIso() {
  return new Date().toISOString().slice(0, 10);
}

function normalizeCategoryEntry(category = {}) {
  const name = normalizeCategoryName(category.name);

  return {
    id: category.id || name,
    name,
    createdAt: category.createdAt || category.created_at || todayIso(),
    items: Number.isFinite(category.items) ? category.items : 0,
  };
}

export function toAdminProject(project = {}) {
  const category = normalizeCategoryName(project.category || project.tags?.[0]);
  const tech =
    project.tech ||
    (Array.isArray(project.tags) ? project.tags.join(", ") : "");

  return {
    id: project.id || Date.now(),
    title: project.title || "Untitled project",
    category,
    tech,
    link: project.link || project.liveLink || project.link_your_project || "",
    status: project.status || "Draft",
    description: project.description || project.desc || "",
    image: project.image || project.thumbnail || "",
    liveLink:
      project.liveLink || project.link || project.link_your_project || "",
    githubLink: project.githubLink || project.link_github || "",
    openProject: project.openProject || project.open_project || "",
    createdAt: project.createdAt || project.created_at || todayIso(),
    categories: project.categories || [],
  };
}

export function buildCategoryList(
  projects,
  apiCategories = [],
  storedCategories = [],
) {
  const mergedCategories = [...storedCategories, ...apiCategories]
    .map((category) => {
      const normalized = normalizeCategoryEntry(category);
      return normalized;
    })
    .filter((category, index, categories) => {
      return (
        categories.findIndex((item) => item.name === category.name) === index
      );
    });

  return mergedCategories;
}
