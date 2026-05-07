import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const API = "http://localhost:8000";

  // AUTO LOGIN
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      navigate("/dashboard");
    }
  }, []);

  // REGISTER
  const register = async () => {
    try {
      await axios.post(`${API}/register`, {
        name,
        password,
      });

      alert("Registration successful");
    } catch (err) {
      alert("Registration failed");
    }
  };

  // LOGIN
  const login = async () => {
    try {
      const res = await axios.post(
        `${API}/login?name=${name}&password=${password}`
      );

      localStorage.setItem("token", res.data.access_token);

      alert("Login successful");

      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        fontFamily: "Arial",
      }}
    >
      <div
        style={{
          width: "300px",
          padding: "30px",
          border: "1px solid #ccc",
          borderRadius: "10px",
        }}
      >
        <h1>Auth App</h1>

        <input
          type="text"
          placeholder="Username"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "15px",
          }}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "15px",
          }}
        />

        <button
          onClick={register}
          style={{
            width: "100%",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          Register
        </button>

        <button
          onClick={login}
          style={{
            width: "100%",
            padding: "10px",
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;
