import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchCategories } from '@/services/api';

export default function CategorySection() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetchCategories().then(setCategories).catch(console.error);
  }, []);

  const himCategories = categories.filter(c => c.name.toLowerCase().includes('men') || c.name.toLowerCase().includes('him')).slice(0, 1);
  const herCategories = categories.filter(c => c.name.toLowerCase().includes('women') || c.name.toLowerCase().includes('her')).slice(0, 1);

  return (
    <section className="category_section section">
      <div className="container">
        <div className="category_bg">
          <div className="row g-4">
            <div className="col-lg-6">
              <div className="category-block">
                <h2 className="category-title">For Him</h2>
                <div className="category-image-wrapper">
                  <img src={himCategories[0]?.image_url || "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=800&q=80"} alt="Men's" className="category-img" />
                </div>
                <div className="category-tags">
                  {himCategories[0]?.children?.slice(0, 3).map(child => (
                    <Link key={child.id} to={`/category/${child.slug}`} className="tag-btn">{child.name}</Link>
                  )) || <Link to="/category/men" className="tag-btn">Explore Men's</Link>}
                </div>
                <Link to="/category/men" className="view-all-btn">View All For Him <i className="bi bi-arrow-right"></i></Link>
              </div>
            </div>
            <div className="col-lg-6">
              <div className="category-block">
                <h2 className="category-title">For Her</h2>
                <div className="category-image-wrapper">
                  <img src={herCategories[0]?.image_url || "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=800&q=80"} alt="Women's" className="category-img" />
                </div>
                <div className="category-tags">
                  {herCategories[0]?.children?.slice(0, 3).map(child => (
                    <Link key={child.id} to={`/category/${child.slug}`} className="tag-btn">{child.name}</Link>
                  )) || <Link to="/category/women" className="tag-btn">Explore Women's</Link>}
                </div>
                <Link to="/category/women" className="view-all-btn">View All For Her <i className="bi bi-arrow-right"></i></Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}