import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchBanners, fetchCategories } from '@/services/api';

export default function BannerSection() {
  const [banners, setBanners] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      const [bannersData, categoriesData] = await Promise.all([fetchBanners(), fetchCategories()]);
      setBanners(bannersData);
      setCategories(categoriesData);
    };
    loadData();
  }, []);

  return (
    <section className="banner-section">
      <div className="container">
        <div className="row g-0">
          <aside className="col-lg-2 sidebar d-none d-lg-block">
            <nav aria-label="Product Categories">
              <ul className="list-unstyled parent_menu">
                {categories.slice(0, 8).map(cat => (
                  <li key={cat.id}>
                    <Link to={`/category/${cat.slug}`}>
                      {cat.name} <i className="bi bi-chevron-right"></i>
                    </Link>
                    {cat.children && cat.children.length > 0 && (
                      <ul className="child_menu list-unstyled">
                        {cat.children.map(child => (
                          <li key={child.id}><Link to={`/category/${child.slug}`}>{child.name}</Link></li>
                        ))}
                      </ul>
                    )}
                  </li>
                ))}
              </ul>
            </nav>
          </aside>
          <div className="col-12 col-lg-10 p-0">
            <div className="react-carousel carousel-single">
              {banners.length > 0 ? banners.map(banner => (
                <div key={banner.id} className="banner-item">
                  <img src={banner.image_url} alt={banner.title} loading="lazy" />  
                </div>
              )) : (
                <div className="banner-item">
                  <img src="https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=1200&q=80" alt="Default Banner" loading="lazy" />
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}