export default function TrustBar() {
  return (
    <div className="trust-bar section">
      <div className="container">
        <div className="trust-container">
          <div className="trust-item">
            <div className="icon-box"><i className="bi bi-shield-lock-fill"></i></div>
            <div className="text-content"><h4>Safe & Secure</h4><p>100% Protected Checkout</p></div>
          </div>
          <div className="trust-item">
            <div className="icon-box"><i className="bi bi-patch-check-fill"></i></div>
            <div className="text-content"><h4>100% Authentic</h4><p>Genuine Fragrances Only</p></div>
          </div>
          <div className="trust-item">
            <div className="icon-box"><i className="bi bi-truck"></i></div>
            <div className="text-content"><h4>Same Day Shipping</h4><p>Orders dispatched daily</p></div>
          </div>
          <div className="trust-item">
            <div className="icon-box"><i className="bi bi-headset"></i></div>
            <div className="text-content"><h4>Expert Support</h4><p>Dedicated fragrance consultants</p></div>
          </div>
        </div>
      </div>
    </div>
  );
}