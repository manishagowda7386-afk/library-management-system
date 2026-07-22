import DashboardCards from "../components/DashboardCards";

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
          <input
            type="text"
            placeholder="Search books, members..."
          />
        </div>
      </header>

      <DashboardCards />
    </>
  );
}

export default Dashboard;