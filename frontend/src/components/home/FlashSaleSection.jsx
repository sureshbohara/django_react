import { useState, useEffect } from 'react';
import { fetchFlashSaleProducts } from '@/services/api';
import ProductCard from '@/components/shared/ProductCard';

export default function FlashSaleSection() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchFlashSaleProducts().then(setProducts).catch(console.error);
  }, []);

  if (products.length === 0) return null;

  return (
    <section className="flash-sale-section section">
      <div className="container">
        <div className="flash-header">
          <h2><i className="bi bi-lightning-charge-fill me-2"></i>Flash Sale</h2>
          <p>Grab your favorite luxury fragrances before time runs out!</p>
        </div>
        <div className="row row-cols-2 row-cols-md-4 g-4">
          {products.map(p => (
            <div className="col" key={p.id}>
              <ProductCard product={p} isFlashSale={true} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}