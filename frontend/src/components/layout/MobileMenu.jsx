import { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { logoutUser } from '@/services/api';

export default function MobileMenu() {
  const location = useLocation();
  const isActive = (path) => location.pathname === path ? 'active' : '';
  const [user, setUser] = useState(null);

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) setUser(JSON.parse(storedUser));
  }, []);

  return (
    <div className="mobile-menu">
      <Link to="/" className={isActive('/')}>
        <i className="bi bi-house-door-fill"></i><span>Home</span>
      </Link>
      <Link to="/category" className={isActive('/category')}>
        <i className="bi bi-grid-fill"></i><span>Shop</span>
      </Link>
      <Link to="/cart" className={isActive('/cart')}>
        <i className="bi bi-bag-fill"></i><span>Cart</span>
      </Link>
      {user ? (
        <button className="border-0 bg-transparent text-decoration-none" onClick={logoutUser} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', color: 'var(--danger)', fontSize: '11px', fontWeight: 500, gap: '4px' }}>
          <i className="bi bi-box-arrow-right" style={{ fontSize: '24px' }}></i><span>Logout</span>
        </button>
      ) : (
        <button className="border-0 bg-transparent text-decoration-none" data-bs-toggle="modal" data-bs-target="#accountModal" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', color: 'var(--text-muted)', fontSize: '11px', fontWeight: 500, gap: '4px' }}>
          <i className="bi bi-person-fill" style={{ fontSize: '24px' }}></i><span>Login</span>
        </button>
      )}
    </div>
  );
}