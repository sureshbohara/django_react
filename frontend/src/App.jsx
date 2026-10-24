import { useState } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import MobileMenu from './components/layout/MobileMenu';
import AuthModal from './components/layout/AuthModal';
import OffcanvasMenu from './components/layout/OffcanvasMenu';
import AppRoutes from './routes/AppRoutes';
import './index.css';

function App() {
  const [showModal, setShowModal] = useState(false);

  return (
    <Router>
      <Header onOpenModal={() => setShowModal(true)} />

      <main className="main-content">
        <AppRoutes />
      </main>
      
      <Footer />
      <MobileMenu onOpenModal={() => setShowModal(true)} />
      <AuthModal isOpen={showModal} onClose={() => setShowModal(false)} />
      <OffcanvasMenu />
    </Router>
  );
}

export default App;