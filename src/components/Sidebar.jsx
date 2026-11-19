import React from "react";
import { ShoppingBasket, LayoutDashboard, Package, MessageCircle } from "lucide-react";

const navigationItems = [
  { label: "Overview", icon: LayoutDashboard },
  { label: "Products", icon: Package },
  { label: "AI Assistant", icon: MessageCircle }
];

export default function Sidebar({ activePage, onNavigate }) {
  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="brand-icon"><ShoppingBasket /></span>
        <div>
          <strong>swiftcart</strong>
          <small>QUICKCOMMERCE AI</small>
        </div>
      </div>

      <p className="nav-label">WORKSPACE</p>

      {navigationItems.map((item) => {
        const Icon = item.icon;

        return (
          <button
            key={item.label}
            className={`nav-button ${activePage === item.label ? "active" : ""}`}
            onClick={() => onNavigate(item.label)}
          >
            <Icon size={18} />
            {item.label}
          </button>
        );
      })}

      <div className="sidebar-bottom">
        <strong>Smarter commerce</strong>
        <p>Turn product and inventory data into better decisions.</p>
        <small>DEMO STORE · INDIA</small>
      </div>
    </aside>
  );
}
