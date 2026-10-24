import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { logoutUser } from '@/services/api';

export default function Header({ onOpenModal }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) setUser(JSON.parse(storedUser));
  }, []);

  const handleLogout = () => {
    setUser(null);
    logoutUser();
  };

  return (
    <>
      <header className="header header-desktop">
        <nav className="navbar navbar-expand-lg p-0">
          <div className="container">
            <Link className="navbar-brand p-0" to="/">
              <h2 style={{ fontFamily: "'Playfair Display', serif", fontSize: '28px', color: 'var(--theme-color)', margin: '15px 0' }}>Caroline's</h2>
            </Link>
            <div className="collapse navbar-collapse" id="navbarContent">
              <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                <li className="nav-item"><Link className="nav-link" to="#"><i className="bi bi-headset"></i> Help</Link></li>
                <li className="nav-item"><Link className="nav-link" to="/track-order"><i className="bi bi-truck"></i> Track Order</Link></li>
                <li className="nav-item">
                  <Link className="nav-link position-relative" to="/cart">
                    <i className="bi bi-bag"></i> Cart
                    <span className="cart-count">0</span>
                  </Link>
                </li>
                <li className="nav-item">
                  {user ? (
                    <div className="dropdown">
                      <button className="nav-link border-0 bg-transparent dropdown-toggle" type="button" data-bs-toggle="dropdown">
                        <i className="bi bi-person-circle"></i> {user.name}
                      </button>
                      <ul className="dropdown-menu dropdown-menu-end">
                        <li><Link className="dropdown-item" to="/profile">My Profile</Link></li>
                        <li><Link className="dropdown-item" to="/orders">My Orders</Link></li>
                        <li><hr className="dropdown-divider" /></li>
                        <li><button className="dropdown-item text-danger" onClick={handleLogout}>Logout</button></li>
                      </ul>
                    </div>
                  ) : (
                    <button className="nav-link border-0 bg-transparent" type="button" onClick={onOpenModal}>
                      <i className="bi bi-person"></i> Login
                    </button>
                  )}
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </header>

      <div className="header-mobile d-lg-none">
        <div className="container">
          <div className="d-flex align-items-center justify-content-between py-3">
            <Link className="navbar-brand p-0" to="/">
              <h2 style={{ fontFamily: "'Playfair Display', serif", fontSize: '24px', color: 'var(--theme-color)', margin: 0, letterSpacing: '-0.5px' }}>Caroline's</h2>
            </Link>
            <button className="menu-toggle-btn border-0" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNav" aria-label="Menu">
              <i className="bi bi-list" style={{ fontSize: '1.5rem' }}></i>
            </button>
          </div>
          <div className="pb-3">
            <form className="d-flex w-100" role="search" action="/search">
              <input className="form-control mobile-search-input" type="search" placeholder="Search perfumes, skincare..." />
              <button className="btn btn-search-mobile" type="submit"><i className="bi bi-search"></i></button>
            </form>
          </div>
        </div>
      </div>

      <div className="sub-header-sticky d-none d-lg-block">
        <div className="container">
          <div className="sub-header-inner">
            <button className="all-category-btn" type="button" onClick={() => window.location.href='/category'}>
              <i className="bi bi-grid-fill"></i> <span>All Categories</span>
            </button>
            <div className="search-wrapper">
              <form className="search-form" role="search" action="/search">
                <input id="searchInputDesktop" type="search" className="search-input" placeholder="Search for perfumes, skincare, makeup..." />
                <button type="submit" className="search-btn"><i className="bi bi-search"></i></button>
              </form>
            </div>
            <div className="header-actions">
              <Link to="/best-sellers" className="action-link"><i className="bi bi-fire"></i> <span>Best Sellers</span></Link>
              <a href="tel:+9779709065971" className="action-link hotline-link">
                <i className="bi bi-telephone-fill"></i>
                <div className="hotline-text">
                  <span className="label">Hotline</span>
                  <span className="number">+977 9709065971</span>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}