const API_BASE_URL = "https://api-portfolio-back-end.onrender.com";

function normalizeAssetUrl(value) {
  if (!value || typeof value !== "string") {
    return "";
  }

  if (/^https?:\/\//i.test(value)) {
    return value;
  }

  let path = value.startsWith("/") ? value : `/${value}`;

  // Ensure the path includes /uploads/ if it's a thumbnail file
  if (!path.startsWith("/uploads/") && path.match(/thumbnail-[^/]+\.(png|jpe?g|gif|webp)$/i)) {
    path = `/uploads${path}`;
  }

  return `${API_BASE_URL}${path}`;
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
  const cats = Array.isArray(project?.techStack)
    ? project.techStack
    : Array.isArray(project?.categories)
      ? project.categories
      : [];

  return cats.map((category) => category?.name || category).filter(Boolean);
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
    openProject: normalizeLink(project.open_project),
    createdAt: project.created_at || "",
    categories,
    category: categories[0] || "General Stack",
    tags: categories.length ? categories : ["Project"],
  };
}

export async function fetchProjects() {
  const response = await fetch(`${API_BASE_URL}/api/auth/projects`);

  if (!response.ok) {
    throw new Error(`Failed to load projects (${response.status})`);
  }

  const payload = await response.json();

  if (!payload?.result || !Array.isArray(payload?.data)) {
    return [];
  }

  return payload.data.map(normalizeProject);
}

export async function createProject(project, token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/create-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      title: project.title,
      description: project.desc || project.description || "",
      categoryIds: project.categoryIds || project.categories || [], // Array of IDs
      thumbnail: project.image || project.thumbnail || "",
      link_your_project: project.liveLink || project.link || project.link_your_project || "",
      link_github: project.githubLink || project.link_github || "",
      open_project: project.openProject || project.open_project || ""
    }),
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.message || `Failed to create project (${response.status})`);
  }

  const payload = await response.json();
  return normalizeProject(payload.data || payload.project || payload);
}

export async function updateProject(id, project, token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/projects/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      title: project.title,
      description: project.desc || project.description || "",
      categoryIds: project.categoryIds || project.categories || [],
      thumbnail: project.image || project.thumbnail || "",
      link_your_project: project.liveLink || project.link || project.link_your_project || "",
      link_github: project.githubLink || project.link_github || "",
      open_project: project.openProject || project.open_project || ""
    }),
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.message || `Failed to update project (${response.status})`);
  }

  const payload = await response.json();
  return normalizeProject(payload.data || payload.project || payload);
}

export async function deleteProject(id, token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/projects/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.message || `Failed to delete project (${response.status})`);
  }

  return await response.json();
}

export async function uploadThumbnail(file, token) {
  const formData = new FormData();
  formData.append("thumbnail", file);

  const response = await fetch(`${API_BASE_URL}/api/auth/upload/thumbnail`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
    body: formData,
  });

  if (!response.ok) {
    const err = await response.json().catch(() => ({}));
    throw new Error(err.message || `Failed to upload thumbnail (${response.status})`);
  }

  return await response.json();
}
