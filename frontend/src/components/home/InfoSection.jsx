import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchSiteSettings } from '@/services/api';

export default function InfoSection() {
  const [settings, setSettings] = useState(null);

  useEffect(() => {
    fetchSiteSettings().then(setSettings).catch(console.error);
  }, []);

  const img1 = settings?.image1_url || "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=600&q=80";
  const img2 = settings?.image2_url || "https://images.unsplash.com/photo-1616949755610-8c9bbc08f138?auto=format&fit=crop&w=600&q=80";
  const info1 = settings?.info1 || "Each signature scent starts with a color and a feeling.";
  const info2 = settings?.info2 || "Caroline's House of Fragrances is a modern artisanal perfumery committed to producing high-quality products using ethically sourced, all-natural ingredients.";

  return (
    <section className="info_section section">
      <div className="container">
        <div className="row align-items-center g-4">
          <div className="col-lg-4 d-none d-lg-block">
            <div className="image_section">
              <img src={img1} alt="About Caroline's" />
            </div>
          </div>
          <div className="col-lg-4 col-12">
            <div className="content_section">
              <h5>Our Story</h5>
              <h3>{info1}</h3>
              <p>{info2}</p>
              <Link to="/page/about-us" className="btn-elegant">Schedule a Studio Visit <i className="bi bi-arrow-right"></i></Link>
            </div>
          </div>
          <div className="col-lg-4 d-none d-lg-block">
            <div className="image_section">
              <img src={img2} alt="Artisanal Process" />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}