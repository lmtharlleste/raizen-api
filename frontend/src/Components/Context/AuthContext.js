import React, { createContext, useState, useContext, useEffect } from 'react';

// Criação do contexto
const AuthContext = createContext();

// Provedor do contexto
export const AuthProvider = ({ children }) => {
  // Definindo o estado para armazenar se o usuário está logado e o token
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [token, setToken] = useState(localStorage.getItem('token') || null); // Carrega o token do localStorage se existir

  // Função para fazer login
  const login = (token) => {
    setToken(token);
    setIsLoggedIn(true);
    localStorage.setItem('token', token); // Armazenando o token no localStorage
  };

  // Função para fazer logout
  const logout = () => {
    setToken(null);
    setIsLoggedIn(false);
    localStorage.removeItem('token'); // Removendo o token do localStorage
  };

  // Efeito para verificar se o token existe no localStorage na inicialização
  useEffect(() => {
    if (token) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, [token]);

  return (
    <AuthContext.Provider value={{ isLoggedIn, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Hook customizado para acessar o AuthContext
export const useAuth = () => {
  return useContext(AuthContext);
};
