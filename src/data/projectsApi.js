const API_BASE_URL = "http://localhost:3000";

function normalizeAssetUrl(value) {
  if (!value || typeof value !== "string") {
    return "";
  }

  if (/^https?:\/\//i.test(value) || value.startsWith("/")) {
    return value;
  }

  return `${API_BASE_URL}/${value}`;
}

function normalizeLink(value) {
  if (!value || typeof value !== "string") {
    return "";
  }

  if (/^https?:\/\//i.test(value) || value.startsWith("/")) {
    return value;
  }

  return "";
}

function getCategories(project) {
  if (!Array.isArray(project?.categories)) {
    return [];
  }

  return project.categories.map((category) => category?.name).filter(Boolean);
}

export function normalizeProject(project) {
  const categories = getCategories(project);

  return {
    id: project.id,
    adminId: project.admin_id,
    adminName: project.admin_name || "",
    title: project.title || "Untitled project",
    desc: project.description || "",
    image: normalizeAssetUrl(project.thumbnail),
    liveLink: normalizeLink(project.link_your_project),
    githubLink: normalizeLink(project.link_github),
    createdAt: project.created_at || "",
    categories,
    category: categories[0] || "Uncategorized",
    tags: categories.length ? categories : ["Project"],
  };
}

export async function fetchProjects() {
  const response = await fetch("/api/auth/projects");

  if (!response.ok) {
    throw new Error(`Failed to load projects (${response.status})`);
  }

  const payload = await response.json();

  if (!payload?.result || !Array.isArray(payload?.data)) {
    return [];
  }

  return payload.data.map(normalizeProject);
}
