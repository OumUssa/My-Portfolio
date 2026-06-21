const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://portfolio.cms-jubpet.linkpc.net";

export async function fetchCategories() {
  const response = await fetch(`${API_BASE_URL}/api/auth/categories`);

  if (!response.ok) {
    throw new Error(`Failed to load categories (${response.status})`);
  }

  const payload = await response.json();

  if (!payload?.result || !Array.isArray(payload?.data)) {
    return [];
  }

  return payload.data.map((category) => ({
    id: category.id,
    name: category.name || "General Stack",
    createdAt: category.createdAt || category.created_at || "",
  }));
}

export async function createCategory({ name, token }) {
  const doRequest = (authorizationValue) =>
    fetch(`${API_BASE_URL}/api/auth/categories`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: authorizationValue,
      },
      body: JSON.stringify({ name }),
    });

  let response = await doRequest(`Bearer ${token}`);
  let payload = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      payload?.message || `Failed to create tech stack (${response.status})`,
    );
  }

  const created = payload?.data || payload?.category || payload || {};

  return {
    id: created.id,
    name: created.name || name,
    createdAt: created.createdAt || created.created_at || "",
  };
}

export async function deleteCategory(categoryId, token) {
  const doRequest = (authorizationValue) =>
    fetch(`${API_BASE_URL}/api/auth/categories/${categoryId}`, {
      method: "DELETE",
      headers: {
        Authorization: authorizationValue,
      },
    });

  let response = await doRequest(`Bearer ${token}`);
  let payload = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      payload?.message || `Failed to delete tech stack (${response.status})`,
    );
  }

  return payload;
}

export async function updateCategory(categoryId, { name, token }) {
  const doRequest = (authorizationValue) =>
    fetch(`${API_BASE_URL}/api/auth/categories/${categoryId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: authorizationValue,
      },
      body: JSON.stringify({ name }),
    });

  let response = await doRequest(`Bearer ${token}`);
  let payload = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      payload?.message || `Failed to update tech stack (${response.status})`,
    );
  }

  const updated = payload?.data || payload?.category || payload || {};

  return {
    id: updated.id || categoryId,
    name: updated.name || name,
    createdAt: updated.createdAt || updated.created_at || "",
  };
}
