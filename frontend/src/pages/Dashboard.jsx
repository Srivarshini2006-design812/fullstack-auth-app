import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [users, setUsers] = useState([]);
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");

  const API = "http://localhost:8000";

  useEffect(() => {
    fetchUsers();
    fetchTodos();
  }, []);

  const token = localStorage.getItem("token");

  // USERS
  const fetchUsers = async () => {
    try {
      const res = await axios.get(`${API}/users`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setUsers(res.data.users);
    } catch (err) {
      alert("Failed to fetch users");
    }
  };

  // TODOS
  const fetchTodos = async () => {
    try {
      const res = await axios.get(`${API}/todos`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setTodos(res.data.todos);
    } catch (err) {
      alert("Failed to fetch todos");
    }
  };

  // CREATE TODO
  const createTodo = async () => {
    try {
      await axios.post(
        `${API}/todos?title=${title}`,
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setTitle("");

      fetchTodos();
    } catch (err) {
      alert("Failed to create todo");
    }
  };

  // LOGOUT
  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/";
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      
      {/* NAVBAR */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: "30px",
          background: "#eee",
          padding: "15px",
          borderRadius: "10px",
        }}
      >
        <h2>Dashboard</h2>

        <button onClick={logout}>Logout</button>
      </div>

      {/* USERS */}
      <h3>Registered Users</h3>

      <div
        style={{
          marginBottom: "40px",
          padding: "20px",
          border: "1px solid #ccc",
          borderRadius: "10px",
        }}
      >
        {users.map((u) => (
          <div key={u.id}>
            {u.id} - {u.name}
          </div>
        ))}
      </div>

      {/* TODOS */}
      <h3>Todos</h3>

      <input
        placeholder="New todo"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{
          padding: "10px",
          marginRight: "10px",
        }}
      />

      <button onClick={createTodo}>
        Add Todo
      </button>

      <div
        style={{
          marginTop: "20px",
          padding: "20px",
          border: "1px solid #ccc",
          borderRadius: "10px",
        }}
      >
        {todos.length === 0 ? (
          <p>No todos yet</p>
        ) : (
          todos.map((t) => (
            <div
              key={t.id}
              style={{
                padding: "10px",
                borderBottom: "1px solid #ddd",
              }}
            >
              {t.title}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Dashboard;
