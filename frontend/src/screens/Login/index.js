import React from "react";
import LoginForm from "../../Components/LoginForm/LoginForm";
import "./style.css";

function Login() {
  return (
    <div className="login-page">
      <div className="login-container">
        <LoginForm />
      </div>
    </div>
  );
}

export default Login;
