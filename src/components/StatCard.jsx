import React from "react";

export default function StatCard({ label, value, note, icon: Icon }) {
  return (
    <article className="stat-card">
      <div className="stat-card-heading">
        <span>{label}</span>
        <Icon size={18} />
      </div>
      <strong>{value}</strong>
      <small>{note}</small>
    </article>
  );
}
