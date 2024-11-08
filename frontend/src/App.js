import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./screens/Login";
import History from "./screens/History";
import Dashboard from "./screens/Dashboard";
import Profile from "./screens/Profile";
import Register from "./screens/Register";
import { AuthProvider } from "./Components/Context/AuthContext";
import ProtectedRoute from "./Components/Context/ProtectedRoute"; 

function App() {
  return (
    <div>
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            {/* Rotas públicas */}
            <Route path="/" element={<Login />} />
            <Route path="/register" element={<Register />} />
            {/* <Route path="/dashboard" element={<Dashboard/>} /> */}

            {/* Rotas protegidas */}
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute element={<Dashboard />} /> // Protege a rota
              }
            />
            <Route
              path="/history"
              element={
                <ProtectedRoute element={<History />} /> 
              }
            />
            <Route
              path="/profile"
              element={
                <ProtectedRoute element={<Profile />} /> 
              }
            />
            <Route path="*" element={<h1>Page not found</h1>} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </div>
  );
}

export default App;
