import React from "react";
import { ShoppingCart } from "lucide-react";

export default function ProductCard({ product, onBuy }) {
  const isAvailable = product.stock > 0;

  return (
    <article className="product-card">
      <div className="product-emoji">{product.emoji}</div>

      <div className="product-meta">
        <span>{product.category}</span>
        <span>★ {product.rating}</span>
      </div>

      <h3>{product.name}</h3>
      <p>{product.description}</p>

      <div className="product-footer">
        <div>
          <strong>₹{product.price}</strong>
          <small>{isAvailable ? `${product.stock} in stock` : "Out of stock"}</small>
        </div>

        <button disabled={!isAvailable} onClick={() => onBuy(product)}>
          <ShoppingCart size={15} />
          Add
        </button>
      </div>
    </article>
  );
}
