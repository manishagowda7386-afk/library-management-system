function Topbar() {
  return (
    <header className="topbar">
      <div>
        <h1>Dashboard</h1>
        <p className="subtitle">
          Welcome back! Here's your library overview.
        </p>
      </div>

      <div className="topbar-right">
        <div className="notification">
          🔔
          <span className="notification-badge">3</span>
        </div>

        <div className="profile-card">
          <div className="avatar">M</div>

          <div>
            <h4>Manisha</h4>
            <small>Administrator</small>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Topbar;