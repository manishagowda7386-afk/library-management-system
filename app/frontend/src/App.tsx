import "./App.css";

function App() {
  return (
    <div className="app">
      {/* Sidebar */}
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
          <div className="menu-item">📊 Reports</div>
          <div className="menu-item">⚙ Settings</div>
          <div className="menu-item">💾 Backup</div>
          <div className="menu-item">ℹ About</div>
        </nav>

        <button className="logout">Logout</button>
      </aside>

      {/* Main */}
      <main className="content">
        <header className="topbar">
          <div>
            <h1>Dashboard</h1>
            <p className="subtitle">
              Welcome back! Here's your library overview.
            </p>
          </div>

          <div className="search-box">
            <input placeholder="Search books, members..." />
          </div>
        </header>

        {/* Cards */}

        <section className="cards">

          <div className="card blue">
            <span>📚</span>
            <h3>Total Books</h3>
            <h2>1,250</h2>
            <small>+15 this week</small>
          </div>

          <div className="card green">
            <span>👥</span>
            <h3>Members</h3>
            <h2>420</h2>
            <small>+6 today</small>
          </div>

          <div className="card purple">
            <span>🔄</span>
            <h3>Active Loans</h3>
            <h2>96</h2>
            <small>Currently issued</small>
          </div>

          <div className="card red">
            <span>⚠</span>
            <h3>Overdue</h3>
            <h2>12</h2>
            <small>Needs attention</small>
          </div>

        </section>

        {/* Second Row */}

        <section className="row">

          <div className="quick-actions">

            <h2>Quick Actions</h2>

            <div className="actions">

              <button>Add Book</button>

              <button>Add Member</button>

              <button>Issue Book</button>

              <button>Return Book</button>

            </div>

          </div>

          <div className="recent-loans">

            <h2>Recent Loans</h2>

            <table>

              <thead>

                <tr>

                  <th>Member</th>

                  <th>Book</th>

                  <th>Status</th>

                </tr>

              </thead>

              <tbody>

                <tr>

                  <td>John</td>

                  <td>Python</td>

                  <td className="issued">Issued</td>

                </tr>

                <tr>

                  <td>Alice</td>

                  <td>React</td>

                  <td className="returned">Returned</td>

                </tr>

                <tr>

                  <td>David</td>

                  <td>Java</td>

                  <td className="issued">Issued</td>

                </tr>

              </tbody>

            </table>

          </div>

        </section>

        {/* Third Row */}

        <section className="row">

          <div className="books">

            <h2>Books Overview</h2>

            <table>

              <thead>

                <tr>

                  <th>Book</th>

                  <th>Author</th>

                  <th>Available</th>

                </tr>

              </thead>

              <tbody>

                <tr>

                  <td>Python</td>

                  <td>Guido</td>

                  <td>12</td>

                </tr>

                <tr>

                  <td>Java</td>

                  <td>James</td>

                  <td>8</td>

                </tr>

                <tr>

                  <td>React</td>

                  <td>Meta</td>

                  <td>4</td>

                </tr>

              </tbody>

            </table>

          </div>

          <div className="charts">

            <h2>Statistics</h2>

            <div className="chart-placeholder">

              Doughnut Chart

            </div>

            <div className="chart-placeholder">

              Bar Chart

            </div>

          </div>

        </section>

      </main>

    </div>
  );
}

export default App;