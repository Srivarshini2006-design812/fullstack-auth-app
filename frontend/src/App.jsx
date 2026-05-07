import { useEffect, useState } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./ProtectedRoute";

function App() {
  const [token, setToken] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const savedToken = localStorage.getItem("token");

    if (savedToken) {
      setToken(savedToken);
    }
  }, []);

  const logout = () => {
    localStorage.removeItem("token");
    setToken("");
    navigate("/");
  };

  return (
    <Routes>
      <Route path="/" element={<Login setToken={setToken} />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard logout={logout} />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

export default App;
