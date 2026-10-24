import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchBlogs } from '@/services/api';

export default function BlogSection() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    fetchBlogs().then(setBlogs).catch(console.error);
  }, []);

  return (
    <section className="blog_section section">
      <div className="container">
        <div className="text-center mb-5">
          <h3 style={{ fontSize: '1.75rem', marginBottom: '8px' }}>Latest from the Journal</h3>
          <p style={{ color: 'var(--text-muted)' }}>Fragrance tips, skincare routines, and wellness guides.</p>
        </div>
        <div className="row g-4">
          {blogs.length > 0 ? blogs.slice(0, 3).map(blog => (
            <div className="col-md-4" key={blog.id}>
              <div className="blog-card">
                <div className="blog-img"><img src={blog.image_url} alt={blog.title} /></div>
                <div className="blog-content">
                  <div className="blog-meta">{blog.category_name} • {new Date(blog.created_at).toLocaleDateString()}</div>
                  <h4>{blog.title}</h4>
                  <p>{blog.excerpt}</p>
                  <Link to={`/blog/${blog.slug}`} className="read-more">Read Article <i className="bi bi-arrow-right"></i></Link>
                </div>
              </div>
            </div>
          )) : (
            <p className="text-center">No blogs available.</p>
          )}
        </div>
      </div>
    </section>
  );
}