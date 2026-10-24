export default function InstagramSection() {
  return (
    <section className="instagram_section section">
      <div className="container">
        <div className="text-center mb-4">
          <h3 style={{ fontSize: '1.75rem', marginBottom: '8px' }}>Follow Us on Instagram</h3>
          <p style={{ color: 'var(--text-muted)' }}>@carolineshouse</p>
        </div>
        <div className="instagram-grid">
          {[1, 2, 3, 4, 5, 6].map(i => (
            <div className="insta-item" key={i}>
              <img src={`https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=400&q=80&random=${i}`} alt="Instagram" />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}