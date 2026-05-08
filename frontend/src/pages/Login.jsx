import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login({ setToken }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const API = "https://fullstack-auth-app-1kmt.onrender.com";

  // -------------------------
  // LOGIN
  // -------------------------
  const login = async () => {
    try {
      const res = await axios.post(`${API}/login`, {
        name,
        password,
      });

      alert(res.data.message);

      navigate("/dashboard");
    } catch (err) {
      console.log(err);
      alert("Login failed");
    }
  };

  // -------------------------
  // REGISTER
  // -------------------------
  const register = async () => {
    try {
      await axios.post(`${API}/register`, {
        name,
        password,
      });

      alert("Registered successfully");
    } catch (err) {
      console.log(err);
      alert("Register failed");
    }
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Login</h1>

      <input
        placeholder="name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{
          display: "block",
          marginBottom: "10px",
          padding: "10px",
        }}
      />

      <input
        placeholder="password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{
          display: "block",
          marginBottom: "10px",
          padding: "10px",
        }}
      />

      <button
        onClick={login}
        style={{
          marginRight: "10px",
          padding: "10px 20px",
        }}
      >
        Login
      </button>

      <button
        onClick={register}
        style={{
          padding: "10px 20px",
        }}
      >
        Register
      </button>
    </div>
  );
}

export default Login;
