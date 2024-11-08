import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext"; // Acessa o estado de login

const ProtectedRoute = ({ element, ...rest }) => {
  const { isLoggedIn } = useAuth(); // Verifica o estado de login

  // Se o usuário não estiver logado, redireciona para a página de login
  if (!isLoggedIn) {
    return <Navigate to="/" />;
  }

  // Se o usuário estiver logado, renderiza o componente passado
  return element;
};

export default ProtectedRoute;
