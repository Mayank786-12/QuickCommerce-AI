import React from "react";
import { AlertTriangle, Package, ShoppingCart, TrendingUp } from "lucide-react";
import StatCard from "../components/StatCard";

function formatCurrency(value) {
  return `₹${Number(value || 0).toLocaleString("en-IN")}`;
}

export default function Dashboard({ analytics }) {
  if (!analytics) {
    return <section className="content-panel">Loading dashboard data...</section>;
  }

  const cards = [
    { label: "Total revenue", value: formatCurrency(analytics.revenue), note: "Demo store revenue", icon: TrendingUp },
    { label: "Orders", value: analytics.orders, note: "Total recorded orders", icon: ShoppingCart },
    { label: "Units sold", value: analytics.units_sold, note: "Total items ordered", icon: Package },
    { label: "Low-stock items", value: analytics.low_stock, note: "Needs attention", icon: AlertTriangle }
  ];

  return (
    <>
      <div className="stats-grid">
        {cards.map((card) => <StatCard key={card.label} {...card} />)}
      </div>

      <div className="dashboard-grid">
        <section className="content-panel">
          <h2>Category sales</h2>
          <p className="muted">Revenue grouped by product category</p>

          {analytics.category_sales.map((item) => {
            const maximum = Math.max(
              ...analytics.category_sales.map((category) => category.sales),
              1
            );
            const barWidth = (item.sales / maximum) * 100;

            return (
              <div className="sales-row" key={item.category}>
                <span>{item.category}</span>
                <div className="bar-track">
                  <div className="bar-fill" style={{ width: `${barWidth}%` }} />
                </div>
                <strong>{formatCurrency(item.sales)}</strong>
              </div>
            );
          })}
        </section>

        <section className="content-panel">
          <h2>Inventory alerts</h2>
          <p className="muted">Products with five or fewer units</p>

          {analytics.low_stock_items.map((product) => (
            <div className="inventory-row" key={product.id}>
              <span>{product.emoji}</span>
              <div>
                <strong>{product.name}</strong>
                <small>{product.stock === 0 ? "Out of stock" : `${product.stock} units left`}</small>
              </div>
              <b>{product.stock === 0 ? "OUT" : "LOW"}</b>
            </div>
          ))}
        </section>
      </div>

      <section className="content-panel">
        <h2>Top products</h2>
        <p className="muted">Ranked by units ordered in the demo data</p>

        {analytics.top_products.map((product, index) => (
          <div className="top-product-row" key={product.name}>
            <span>0{index + 1}</span>
            <strong>{product.name}</strong>
            <small>{product.units} units</small>
          </div>
        ))}
      </section>
    </>
  );
}
