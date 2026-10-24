import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-newsletter">
        <div className="container">
          <h3>Join Our Fragrance Community</h3>
          <p>Subscribe to get special offers, free giveaways, and exclusive deals.</p>
          <form className="newsletter-form" onSubmit={(e) => { e.preventDefault(); alert('Thank you for subscribing!'); }}>
            <input type="email" placeholder="Enter your email address" required />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>
      <div className="footer-main">
        <div className="container">
          <div className="row g-4">
            <div className="col-lg-3 col-md-6 footer-widget">
              <h4>About Us</h4>
              <p style={{ opacity: 0.8, lineHeight: 1.8 }}>Every product is made in small batches by hand, using only premium organic oils and botanicals. Pure, fresh luxury crafted just for you.</p>
              <div className="footer-social">
                <a href="#" aria-label="Facebook"><i className="bi bi-facebook"></i></a>
                <a href="#" aria-label="Instagram"><i className="bi bi-instagram"></i></a>
                <a href="#" aria-label="YouTube"><i className="bi bi-youtube"></i></a>
                <a href="#" aria-label="TikTok"><i className="bi bi-tiktok"></i></a>
              </div>
            </div>
            <div className="col-lg-3 col-6 footer-widget">
              <h4>Quick Links</h4>
              <ul className="footer-links">
                <li><Link to="#">About Us</Link></li>
                <li><Link to="#">Contact</Link></li>
                <li><Link to="#">Shipping Info</Link></li>
                <li><Link to="#">Return Policy</Link></li>
              </ul>
            </div>
            <div className="col-lg-3 col-6 footer-widget">
              <h4>Categories</h4>
              <ul className="footer-links">
                <li><Link to="#">Perfumes</Link></li>
                <li><Link to="#">Skincare</Link></li>
                <li><Link to="#">Haircare</Link></li>
                <li><Link to="#">Makeup</Link></li>
              </ul>
            </div>
            <div className="col-lg-3 col-12 footer-widget">
              <h4>Contact Us</h4>
              <ul className="contact-info-list">
                <li><i className="bi bi-telephone-fill"></i> <a href="tel:+9779709065971">+977 9709065971</a></li>
                <li><i className="bi bi-envelope-fill"></i> <a href="mailto:support@carolineshouse.com">support@carolineshouse.com</a></li>
                <li><i className="bi bi-geo-alt-fill"></i> <span>5 Plant Ave, Hauppauge, NY</span></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <div className="container">
          <div className="footer-bottom-inner">
            <p className="copyright">&copy; 2026 Caroline's House of Fragrances. All rights reserved.</p>
            <div className="payment-icons">
              <i className="bi bi-credit-card-2-front-fill" title="Credit Card"></i>
              <i className="bi bi-paypal" title="PayPal"></i>
              <i className="bi bi-cash-coin" title="Cash on Delivery"></i>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}