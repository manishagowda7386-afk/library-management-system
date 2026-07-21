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
          <div className="menu-item">📚 Books</div>
          <div className="menu-item">👥 Members</div>
          <div className="menu-item">🔄 Loans</div>
          <div className="menu-item">📈 Reports</div>
          <div className="menu-item">⚙ Settings</div>
        </nav>

        <button className="logout">Logout</button>
      </aside>

      <main className="content">
        <header className="topbar">
          <h1>Dashboard</h1>

          <div className="search">
            🔍
            <input type="text" placeholder="Search..." />
          </div>
        </header>

        <div className="cards">
          <div className="card blue">
            <h3>Total Books</h3>
            <h2>1250</h2>
            <p>+12 this week</p>
          </div>

          <div className="card green">
            <h3>Members</h3>
            <h2>420</h2>
            <p>+8 this week</p>
          </div>

          <div className="card purple">
            <h3>Active Loans</h3>
            <h2>96</h2>
            <p>Currently Issued</p>
          </div>

          <div className="card red">
            <h3>Overdue</h3>
            <h2>12</h2>
            <p>Needs Attention</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;