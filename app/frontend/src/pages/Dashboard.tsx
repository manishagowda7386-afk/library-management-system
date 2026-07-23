import Topbar from "../components/Topbar";
import DashboardCards from "../components/DashboardCards";
import QuickActions from "../components/QuickActions";
import RecentLoans from "../components/RecentLoans";
import BooksTable from "../components/BooksTable";
import Charts from "../components/Charts";

function Dashboard() {
  return (
    <>
      <Topbar />

      <DashboardCards />

      <div className="dashboard-row">
        <QuickActions />
        <RecentLoans />
      </div>

      <div className="dashboard-row">
        <BooksTable />
        <Charts />
      </div>
    </>
  );
}

export default Dashboard;