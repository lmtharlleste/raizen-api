import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../Context/AuthContext';  
import AlertModal from '../AlertModal';
import './style.css';

const Navbar = () => {
  const { isLoggedIn, logout } = useAuth(); // Pegando o estado de autenticação
  const navigate = useNavigate();
  const [showModal, setShowModal] = useState(false); 

  const handleLogoutClick = () => {
    setShowModal(true); 
  };

  const handleConfirmLogout = () => {
    logout(); 
    setShowModal(false); 
    navigate("/"); 
  };

  const handleCancelLogout = () => {
    setShowModal(false);
  };

  return (
    <header className="header">
      <nav className="nav">
        <ul>
          {isLoggedIn && (
            <>
              <li><Link to="/dashboard">Dashboard</Link></li>
              <li><Link to="/history">History</Link></li>
              <li><Link to="/profile">Profile</Link></li>
            </>
          )}
          {!isLoggedIn && (
            <li><Link to="/search">Quer pesquisar sem criar uma conta?</Link></li>  
          )}
          {isLoggedIn && (
            <li><Link to="#" onClick={handleLogoutClick} className="exit-link">Exit</Link></li>
          )}
        </ul>
      </nav>

      {showModal && (
        <AlertModal
          title="Tem certeza?"
          message="Você deseja realmente sair?"
          onConfirm={handleConfirmLogout}
          onCancel={handleCancelLogout}
        />
      )}
    </header>
  );
};

export default Navbar;
