import { useState, useEffect } from 'react';
import { fetchFeaturedProducts } from '@/services/api';
import ProductCard from '@/components/shared/ProductCard';

export default function ProductCarousel() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchFeaturedProducts(8).then(setProducts).catch(console.error);
  }, []);

  if (products.length === 0) return null;

  return (
    <section className="product_section section">
      <div className="container">
        <div className="offer-banner"><span>Featured Products</span></div>
        <div className="react-carousel carousel-multi">
          {products.map(p => <ProductCard key={p.id} product={p} />)}
        </div>
      </div>
    </section>
  );
}