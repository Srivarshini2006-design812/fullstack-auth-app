import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login({ setToken }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const API = "https://fullstack-auth-app-1kmt.onrender.com";

  const login = async () => {
    try {
      const res = await axios.post(
        `${API}/login?name=${name}&password=${password}`
      );

      const token = res.data.access_token;

      // save token
      localStorage.setItem("token", token);
      setToken(token);

      alert("Login success");
      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  const register = async () => {
    try {
      await axios.post(`${API}/register`, {
        name,
        password,
      });

      alert("Registered successfully");
    } catch (err) {
      alert("Register failed");
    }
  };

  return (
    <div>
      <h1>Login</h1>

      <input
        placeholder="name"
        onChange={(e) => setName(e.target.value)}
      />

      <input
        placeholder="password"
        type="password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={login}>Login</button>
      <button onClick={register}>Register</button>
    </div>
  );
}

export default Login;
