import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchSiteSettings } from '@/services/api';

export default function PromoBanner() {
  const [settings, setSettings] = useState(null);

  useEffect(() => {
    fetchSiteSettings().then(setSettings).catch(console.error);
  }, []);

  const bgImage = settings?.bg_image_url || "https://images.unsplash.com/photo-1615634260167-c8cdede054de?auto=format&fit=crop&w=1920&q=80";
  const promoText = settings?.info3 || "Discover our exclusive collection of artisanal scents, crafted with the world's finest ingredients. Enjoy free shipping on all orders over Rs. 5000.";

  return (
    <section className="promo-banner-section" style={{ backgroundImage: `url('${bgImage}')` }}>
      <div className="container">
        <div className="promo-content">
          <h2>The Art of Fragrance</h2>
          <p>{promoText}</p>
          <Link to="/category" className="btn-elegant" style={{ background: 'var(--accent-color)', color: 'var(--bg-white)', borderColor: 'var(--accent-color)' }}>
            Explore Collection <i className="bi bi-arrow-right"></i>
          </Link>
        </div>
      </div>
    </section>
  );
}