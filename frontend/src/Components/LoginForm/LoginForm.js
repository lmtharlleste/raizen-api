import { Link, useNavigate } from "react-router-dom";
import { FaUser, FaLock } from "react-icons/fa";
import React, { useState } from "react";
import "./LoginForm.css";
import { useAuth } from "../Context/AuthContext";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const { login } = useAuth(); // Pegando a função de login do contexto
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = { email, password };

    const headers = {
      "Content-Type": "application/json",
      "User-Agent": "insomnia/10.1.1",
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/v1/user/login", {
        method: "POST",
        headers,
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (response.ok) {
        // Se o login for bem-sucedido, chama o login do contexto e armazena o token
        login(data.access_token); // Aqui, estamos acessando o access_token corretamente
        navigate("/dashboard"); // Redireciona para a página do dashboard
      } else {
        setErrorMessage(data.message || "Erro no login, tente novamente.");
      }
    } catch (error) {
      console.error("Erro ao conectar com o servidor:", error);
      setErrorMessage("Erro ao se conectar ao servidor.");
    }
  };

  return (
    <div className="wrapper">
      <form onSubmit={handleSubmit}>
        <h1>Login</h1>
        <div className="input-box">
          <input
            type="text"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <FaUser className="icon" />
        </div>
        <div className="input-box">
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <FaLock className="icon" />
        </div>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        <div className="remenber-forgot">
          <label>
            <input type="checkbox" />
            Lembrar-me
          </label>
          <a href="http://127.0.0.1:3000"> Esqueçi minha senha</a>
        </div>
        <button type="submit">Login</button>
        <div className="register-link">
          <p>
            AInda não tem uma conta? <Link to={"/register"}>Cadastre-se</Link>
          </p>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
