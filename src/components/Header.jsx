import React from "react";
import { RefreshCw } from "lucide-react";

export default function Header({ title, description, onRefresh }) {
  return (
    <header className="page-header">
      <div>
        <p className="eyebrow">QUICK COMMERCE / WORKSPACE</p>
        <h1>{title}</h1>
        <p className="page-description">{description}</p>
      </div>

      <button className="refresh-button" onClick={onRefresh}>
        <RefreshCw size={16} />
        Refresh
      </button>
    </header>
  );
}
