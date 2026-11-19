import React, { useEffect, useState } from "react";

import { getAnalytics, getCategories, getProducts, placeOrder } from "./api";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import AssistantPanel from "./components/AssistantPanel";
import Dashboard from "./pages/Dashboard";
import Products from "./pages/Products";

export default function App() {
  const [activePage, setActivePage] = useState("Overview");
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState(["All"]);
  const [analytics, setAnalytics] = useState(null);
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(true);

  // Load all data needed by the dashboard and product page.
  async function loadApplicationData() {
    setIsLoading(true);

    try {
      const [productData, categoryData, analyticsData] = await Promise.all([
        getProducts(),
        getCategories(),
        getAnalytics()
      ]);

      setProducts(productData);
      setCategories(categoryData);
      setAnalytics(analyticsData);
      setMessage("");
    } catch (error) {
      setMessage("Cannot connect to backend. Start the FastAPI server first.");
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    loadApplicationData();
  }, []);

  // Place an order, then refresh stock and sales figures.
  async function handleBuy(product) {
    try {
      const result = await placeOrder(product.id, 1);
      setMessage(result.message);
      await loadApplicationData();
    } catch (error) {
      setMessage(error.message);
    }
  }

  const pageDetails = {
    Overview: {
      title: "Store overview",
      description: "Monitor sales, products and inventory health."
    },
    Products: {
      title: "Product catalogue",
      description: "Explore the catalogue and place a demo order."
    },
    "AI Assistant": {
      title: "Your AI shopping assistant",
      description: "Ask questions about products, shopping and inventory."
    }
  };

  return (
    <div className="app-layout">
      <Sidebar activePage={activePage} onNavigate={setActivePage} />

      <main className="main-content">
        <Header
          title={pageDetails[activePage].title}
          description={pageDetails[activePage].description}
          onRefresh={loadApplicationData}
        />

        {message && (
          <button className="message-banner" onClick={() => setMessage("")}>
            {message}　×
          </button>
        )}

        {isLoading && !analytics ? (
          <section className="content-panel">Loading project data...</section>
        ) : (
          <>
            {activePage === "Overview" && <Dashboard analytics={analytics} />}

            {activePage === "Products" && (
              <Products
                products={products}
                categories={categories}
                onBuy={handleBuy}
              />
            )}

            {activePage === "AI Assistant" && <AssistantPanel />}
          </>
        )}

        <footer>
          SwiftCart AI <span>Portfolio demo · React + FastAPI + SQLite</span>
        </footer>
      </main>
    </div>
  );
}
