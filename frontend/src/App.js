import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./screens/Login";
import History from "./screens/History";
import Dashboard from "./screens/Dashboard";
import Profile from "./screens/Profile";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login/>} />
          <Route path="/dashboard" element={<Dashboard/>} />
          <Route path="/history" element={<History/>} />
          <Route path="/profile" element={<Profile/>} />
          <Route path="*" element={<h1>No folder</h1>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
