import React, { useMemo, useState } from "react";
import { Search } from "lucide-react";
import ProductCard from "../components/ProductCard";

export default function Products({ products, categories, onBuy }) {
  const [searchText, setSearchText] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");

  const visibleProducts = useMemo(() => {
    return products.filter((product) => {
      const matchesCategory =
        selectedCategory === "All" || product.category === selectedCategory;

      const searchableText = `${product.name} ${product.category}`.toLowerCase();
      const matchesSearch = searchableText.includes(searchText.toLowerCase());

      return matchesCategory && matchesSearch;
    });
  }, [products, searchText, selectedCategory]);

  return (
    <section className="content-panel">
      <div className="product-toolbar">
        <div className="search-box">
          <Search size={17} />
          <input
            value={searchText}
            onChange={(event) => setSearchText(event.target.value)}
            placeholder="Search products..."
          />
        </div>

        <select
          value={selectedCategory}
          onChange={(event) => setSelectedCategory(event.target.value)}
        >
          {categories.map((category) => (
            <option key={category} value={category}>{category}</option>
          ))}
        </select>
      </div>

      <div className="products-grid">
        {visibleProducts.map((product) => (
          <ProductCard key={product.id} product={product} onBuy={onBuy} />
        ))}
      </div>

      {visibleProducts.length === 0 && <p>No products match your search.</p>}
    </section>
  );
}
