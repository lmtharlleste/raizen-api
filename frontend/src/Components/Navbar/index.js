import React from "react";
import { Link } from "react-router-dom";
import "./style.css";

const Navbar = () => {
  return (
    <header className="header">
      <nav className="nav">
        <ul>
          <li><Link to="/dashboard">Dashboard</Link></li>
          <li><Link to="/history">History</Link></li>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/exit">Exit</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
