import "./App.css";

function App() {
  return (
    <div className="app">
      <aside className="sidebar">
        <div className="logo">
          <div className="logo-icon">📚</div>
          <div>
            <h2>Library</h2>
            <p>Management System</p>
          </div>
        </div>

        <nav className="menu">
          <div className="menu-item active">🏠 Dashboard</div>
          <div className="menu-item">📖 Books</div>
          <div className="menu-item">👥 Members</div>
          <div className="menu-item">🔄 Loans</div>
          <div className="menu-item">📊 Reports</div>
          <div className="menu-item">⚙ Settings</div>
          <div className="menu-item">💾 Backup</div>
          <div className="menu-item">ℹ About</div>
        </nav>

        <button className="logout">Logout</button>
      </aside>

      <main className="content">
        <h1>Dashboard</h1>
        <p>Welcome back, Admin!</p>
      </main>
    </div>
  );
}

export default App;