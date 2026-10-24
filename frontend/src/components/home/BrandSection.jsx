import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchBrands } from '@/services/api';

export default function BrandSection() {
  const [brands, setBrands] = useState([]);

  useEffect(() => {
    fetchBrands().then(setBrands).catch(console.error);
  }, []);

  return (
    <section className="brand_section section">
      <div className="container">
        <div className="offer-banner"><span>Curated Luxury Brands</span></div>
        <div className="brand-grid">
          {brands.length > 0 ? brands.map(brand => (
            <Link key={brand.id} to={`/category?brand=${brand.slug}`} className="brand-card">
              <div className="brand-logo-box">
                <img src={brand.logo_url} loading="lazy" alt={brand.name} onError={(e) => { e.target.src = `https://via.placeholder.com/150x50?text=${brand.name}`; }} />
              </div>
            </Link>
          )) : (
            ['Chanel', 'Dior', 'Gucci', 'YSL', 'Versace', 'Tom Ford'].map((name, i) => (
              <Link key={i} to="#" className="brand-card">
                <div className="brand-logo-box">
                  <img src={`https://via.placeholder.com/150x50?text=${name}`} loading="lazy" alt={name} />
                </div>
              </Link>
            ))
          )}
        </div>
      </div>
    </section>
  );
}