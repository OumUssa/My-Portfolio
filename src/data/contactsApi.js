const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "https://portfolio.cms-jubpet.linkpc.net";

export async function submitContact(form) {
  const response = await fetch(`${API_BASE_URL}/api/auth/contacts`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: form.name,
      email: form.email,
      subject: form.subject,
      message: form.message,
    }),
  });

  const data = await response.json();
  
  if (!response.ok || !data.result) {
    throw new Error(data.message || "Failed to submit message");
  }
  
  return data;
}

export async function fetchContacts(token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/contacts`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || "Failed to fetch contacts");
  }
  
  return data.data || data.contacts || data;
}

export async function deleteContact(id, token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/contacts/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || "Failed to delete contact");
  }
  
  return data;
}
