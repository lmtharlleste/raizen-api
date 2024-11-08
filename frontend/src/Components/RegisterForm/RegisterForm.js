import { FaUser, FaLock } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
import { IoDocumentAttachSharp } from "react-icons/io5";
import { Link } from "react-router-dom";
import React from "react";
import "./RegisterForm.css";


const RegisterForm = () => {
  return (
    <div className="wrapper">
      <form action="">
        <h1>Registro</h1>
        <div className="input-box">
          <input type="text" placeholder="Full Name" required />
          <FaUser className="icon"/>
        </div>
        <div className="input-box">
          <input type="text" placeholder="email" required />
          <MdEmail className="icon"/>
        </div>
        <div className="input-box">
          <input type="text" placeholder="Cpf" required />
          <IoDocumentAttachSharp className="icon"/>
        </div>
        <div className="input-box">
          <input type="password" placeholder="Senha" required />
            <FaLock className="icon"/>
        </div>
        <button type="submit">Registrar</button>
        <div className="register-link">
            <p>Já tem uma conta? <Link to={"/"}>Faça Login</Link></p>
        </div>
      </form>
    </div>
  );
};

export default RegisterForm;
