export default function ServiceSection() {
  const services = [
    { icon: "bi-truck", title: "Same Day Free Shipping", desc: "Orders ship on the day that you place them." },
    { icon: "bi-shield-check", title: "Trusted Since 2001", desc: "100% authentic fragrances. No knockoffs." },
    { icon: "bi-lock-fill", title: "Safe & Secure Checkout", desc: "Your information is 100% protected." },
    { icon: "bi-star-fill", title: "5 Star Customer Ratings", desc: "Over 20 million satisfied customers." }
  ];

  return (
    <section className="service_section section">
      <div className="container">
        <div className="service-row">
          {services.map((s, i) => (
            <div className="service_wrap" key={i}>
              <div className="service_icon"><i className={`bi ${s.icon}`}></i></div>
              <div className="service-description">
                <h4>{s.title}</h4>
                <p>{s.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}