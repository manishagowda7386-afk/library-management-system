function Dashboard() {
  return (
    <>
      <header className="topbar">
        <div>
          <h1>Dashboard</h1>
          <p className="subtitle">
            Welcome back! Here's your library overview.
          </p>
        </div>

        <div className="search-box">
          <input type="text" placeholder="Search books, members..." />
        </div>
      </header>

      <div className="cards">
        <div className="card blue">
          <span>📚</span>
          <h3>Total Books</h3>
          <h2>1250</h2>
          <small>+15 this week</small>
        </div>

        <div className="card green">
          <span>👥</span>
          <h3>Total Members</h3>
          <h2>420</h2>
          <small>+8 this week</small>
        </div>

        <div className="card purple">
          <span>🔄</span>
          <h3>Active Loans</h3>
          <h2>96</h2>
          <small>Currently Issued</small>
        </div>

        <div className="card red">
          <span>⚠</span>
          <h3>Overdue Books</h3>
          <h2>12</h2>
          <small>Needs Attention</small>
        </div>
      </div>
    </>
  );
}

export default Dashboard;