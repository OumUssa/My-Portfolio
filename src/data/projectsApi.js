const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "https://portfolio.cms-jubpet.linkpc.net";

function normalizeAssetUrl(value) {
  if (!value || typeof value !== "string") {
    return "";
  }

  try {
    const urlObj = new URL(value);
    // If backend returns a localhost URL or the backend URL, extract just the path
    // so we can use relative paths and leverage the Vite proxy / same-origin policy.
    if (
      urlObj.hostname === "localhost" ||
      urlObj.hostname === "127.0.0.1" ||
      urlObj.hostname.includes("portfolio.cms-jubpet")
    ) {
      value = urlObj.pathname;
    }
  } catch (e) {
    // Ignore error if value is a relative path and not a valid absolute URL
  }

  if (/^https?:\/\//i.test(value)) {
    return value;
  }

  let cleanValue = value.startsWith("/") ? value : `/${value}`;
  
  // Ensure the path includes /uploads/ if it's a thumbnail file
  if (!cleanValue.startsWith("/uploads/") && cleanValue.match(/thumbnail-[^/]+\.(png|jpe?g|gif|webp)$/i)) {
    cleanValue = `/uploads${cleanValue}`;
  }

  // Return relative path to utilize Vite's /uploads proxy
  return cleanValue;
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

function splitTags(value) {
  if (Array.isArray(value)) {
    return value.map((item) => String(item || "").trim()).filter(Boolean);
  }

  if (typeof value !== "string") {
    return [];
  }

  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function normalizeStoredProject(project) {
  const category =
    project.category || project.categories?.[0] || "General Stack";
  const categories =
    Array.isArray(project.categories) && project.categories.length
      ? project.categories.map((item) => item || category).filter(Boolean)
      : [category];
  const tags = splitTags(project.tags?.length ? project.tags : project.tech);

  return {
    id: project.id,
    adminId: project.adminId || project.admin_id || null,
    adminName: project.adminName || project.admin_name || "",
    title: project.title || "Untitled project",
    desc: project.desc || project.description || "",
    image: normalizeAssetUrl(project.image || project.thumbnail || ""),
    liveLink: normalizeLink(
      project.liveLink || project.link || project.link_your_project || "",
    ),
    githubLink: normalizeLink(project.githubLink || project.link_github || ""),
    openProject: normalizeLink(project.openProject || project.open_project || ""),
    createdAt: project.createdAt || project.created_at || "",
    categories,
    category: categories[0] || "General Stack",
    tags: tags.length ? tags : [category],
    status: project.status || "Draft",
    tech: project.tech || tags.join(", "),
  };
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
