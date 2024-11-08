import React from "react";
import LoginForm from "../../Components/LoginForm/LoginForm";
import "./style.css";
import Navbar from "../../Components/Navbar";

function Login() {
  return (
    <>
      <Navbar />
      <div className="login-page">
        <div className="login-container">
          <LoginForm />
        </div>
      </div>
    </>
  );
}

export default Login;
