import React from "react";
import RegisterForm from "../../Components/RegisterForm/RegisterForm";
import "./style.css";
import Navbar from "../../Components/Navbar";

function Register() {
  return (
    <>
      <Navbar />
      <div className="login-page">
        <div className="login-container">
          <RegisterForm />
        </div>
      </div>
    </>
  );
}

export default Register;
