// Keep all HTTP requests in one file so components stay easy to read.

const API_BASE_URL = "http://127.0.0.1:8000";

async function request(endpoint, options = {}) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: { "Content-Type": "application/json" },
    ...options
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Something went wrong");
  }

  return data;
}

export const getProducts = () => request("/api/products");
export const getCategories = () => request("/api/categories");
export const getAnalytics = () => request("/api/analytics");

export const placeOrder = (productId, quantity = 1) =>
  request("/api/orders", {
    method: "POST",
    body: JSON.stringify({ product_id: productId, quantity })
  });

export const askAssistant = (question) =>
  request("/api/assistant", {
    method: "POST",
    body: JSON.stringify({ question })
  });
