import { Link } from 'react-router-dom';

export default function OffcanvasMenu() {
  return (
    <div className="offcanvas offcanvas-start" tabIndex="-1" id="offcanvasNav" aria-labelledby="offcanvasNavLabel">
      <div className="offcanvas-header">
        <h5 className="offcanvas-title" id="offcanvasNavLabel">Menu</h5>
        <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div className="offcanvas-body p-0">
        <nav className="nav flex-column">
          <Link className="nav-link" to="/"><i className="bi bi-house me-2"></i> Home</Link>
          <Link className="nav-link" to="/best-sellers"><i className="bi bi-fire me-2"></i> Best Sellers</Link>
          <Link className="nav-link" to="/track-order"><i className="bi bi-truck me-2"></i> Track Order</Link>
        </nav>
        <div className="accordion" id="ecomAccordion">
          <div className="accordion-item">
            <h2 className="accordion-header">
              <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#cat1">
                <i className="bi bi-droplet-fill me-2"></i> Fragrances
              </button>
            </h2>
            <div id="cat1" className="accordion-collapse collapse" data-bs-parent="#ecomAccordion">
              <div className="accordion-body p-0">
                <ul className="list-unstyled m-0">
                  <li><Link to="#">Men's Perfume</Link></li>
                  <li><Link to="#">Women's Perfume</Link></li>
                  <li><Link to="#">Body Mists</Link></li>
                </ul>
              </div>
            </div>
          </div>
          <div className="accordion-item">
            <h2 className="accordion-header">
              <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#cat2">
                <i className="bi bi-stars me-2"></i> Skincare
              </button>
            </h2>
            <div id="cat2" className="accordion-collapse collapse" data-bs-parent="#ecomAccordion">
              <div className="accordion-body p-0">
                <ul className="list-unstyled m-0">
                  <li><Link to="#">Serums</Link></li>
                  <li><Link to="#">Moisturizers</Link></li>
                  <li><Link to="#">Cleansers</Link></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="offcanvas-footer">
        <p className="mb-2"><i className="bi bi-telephone-fill me-2"></i> <a href="tel:+9779709065971">+977 9709065971</a></p>
        <p className="mb-0"><i className="bi bi-geo-alt-fill me-2"></i> 5 Plant Ave, Hauppauge, NY</p>
      </div>
    </div>
  );
}