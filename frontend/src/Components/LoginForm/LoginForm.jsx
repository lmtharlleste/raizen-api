import { FaUser, FaLock } from "react-icons/fa";
import React from "react";
import "./LoginForm.css";


const LoginForm = () => {
  return (
    <div className="wrapper">
      <form action="">
        <h1>Login</h1>
        <div className="input-box">
          <input type="text" placeholder="Email" required />
          <FaUser className="icon"/>
        </div>
        <div className="input-box">
          <input type="password" placeholder="Senha" required />
            <FaLock className="icon"/>
        </div>
        <div className="remenber-forgot">
          <label>
            <input type="checkbox" />
            Lembrar-me
          </label>
          <a href="http://127.0.0.1:3000"> Esqueçi minha senha</a>
        </div>
        <button type="submit">Login</button>
        <div className="register-link">
            Ainda não tem registro? Cadastre-se
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
