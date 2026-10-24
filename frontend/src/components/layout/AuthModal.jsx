import { useState } from 'react';
import { loginUser, registerUser } from '@/services/api';

export default function AuthModal({ isOpen, onClose }) {
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);
  const [loginData, setLoginData] = useState({ email: '', password: '' });
  const [registerData, setRegisterData] = useState({ name: '', email: '', phone: '', password: '' });
  if (!isOpen) return null;

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await loginUser(loginData);
      onClose();
    } catch (err) {
      // Error toast api.js ma handle bhaisakyo
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await registerUser(registerData);
      onClose(); // Success huda modal band huncha
    } catch (err) {
      // Error toast api.js ma handle bhaisakyo
    } finally {
      setLoading(false);
    }
  };

  return (
    <>

      <div className="modal-backdrop fade show" onClick={onClose} style={{ zIndex: 1050 }}></div>
      

      <div className="modal fade show d-block" tabIndex="-1" style={{ zIndex: 1055, display: 'block' }} onClick={onClose}>
        <div className="modal-dialog modal-dialog-centered" onClick={(e) => e.stopPropagation()}>
          <div className="modal-content auth-modal">
            <div className="modal-header">
              <h5 className="modal-title">{isLogin ? 'Welcome Back' : 'Create Account'}</h5>
              <button type="button" className="btn-close" onClick={onClose} aria-label="Close"></button>
            </div>
            
            <div className="modal-body">
              {/* LOGIN FORM */}
              <form className={isLogin ? '' : 'd-none'} onSubmit={handleLogin}>
                <div className="mb-3">
                  <label className="form-label">Email Address</label>
                  <input type="email" className="form-control" placeholder="name@example.com" value={loginData.email} onChange={(e) => setLoginData({...loginData, email: e.target.value})} required />
                </div>
                <div className="mb-3">
                  <label className="form-label">Password</label>
                  <input type="password" className="form-control" placeholder="Enter your password" value={loginData.password} onChange={(e) => setLoginData({...loginData, password: e.target.value})} required />
                </div>
                <button type="submit" className="btn btn-primary w-100" disabled={loading}>{loading ? 'Logging in...' : 'Login'}</button>
                <p className="text-center mt-3">New here? <button type="button" className="btn btn-link p-0" onClick={() => setIsLogin(false)}>Create an Account</button></p>
              </form>

              {/* REGISTER FORM */}
              <form className={!isLogin ? '' : 'd-none'} onSubmit={handleRegister}>
                <div className="mb-3">
                  <label className="form-label">Full Name</label>
                  <input type="text" className="form-control" placeholder="Your Full Name" value={registerData.name} onChange={(e) => setRegisterData({...registerData, name: e.target.value})} required />
                </div>
                <div className="mb-3">
                  <label className="form-label">Email Address</label>
                  <input type="email" className="form-control" placeholder="name@example.com" value={registerData.email} onChange={(e) => setRegisterData({...registerData, email: e.target.value})} required />
                </div>
                <div className="mb-3">
                  <label className="form-label">Phone</label>
                  <input type="tel" className="form-control" placeholder="98XXXXXXXX" value={registerData.phone} onChange={(e) => setRegisterData({...registerData, phone: e.target.value})} required />
                </div>
                <div className="mb-3">
                  <label className="form-label">Password</label>
                  <input type="password" className="form-control" placeholder="Create a strong password" value={registerData.password} onChange={(e) => setRegisterData({...registerData, password: e.target.value})} required />
                </div>
                <button type="submit" className="btn btn-primary w-100" disabled={loading}>{loading ? 'Registering...' : 'Register'}</button>
                <p className="text-center mt-3">Already have an account? <button type="button" className="btn btn-link p-0" onClick={() => setIsLogin(true)}>Login Here</button></p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}