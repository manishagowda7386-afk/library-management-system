import {
    LayoutDashboard,
      BookOpen,
        Users,
          BookCopy,
            BarChart3,
              Settings,
                Database,
                  Info,
                    LogOut,
                    } from "lucide-react";

                    function Sidebar() {
                      return (
                          <aside className="sidebar">
                                <div className="logo">
                                        <div className="logo-icon">
                                                  <BookOpen size={36} />
                                                          </div>

                                                                  <div>
                                                                            <h2>Library</h2>
                                                                                      <p>Management System</p>
                                                                                              </div>
                                                                                                    </div>

                                                                                                          <nav className="menu">
                                                                                                                  <div className="menu-item active">
                                                                                                                            <LayoutDashboard size={20} />
                                                                                                                                      <span>Dashboard</span>
                                                                                                                                              </div>

                                                                                                                                                      <div className="menu-item">
                                                                                                                                                                <BookOpen size={20} />
                                                                                                                                                                          <span>Books</span>
                                                                                                                                                                                  </div>

                                                                                                                                                                                          <div className="menu-item">
                                                                                                                                                                                                    <Users size={20} />
                                                                                                                                                                                                              <span>Members</span>
                                                                                                                                                                                                                      </div>

                                                                                                                                                                                                                              <div className="menu-item">
                                                                                                                                                                                                                                        <BookCopy size={20} />
                                                                                                                                                                                                                                                  <span>Loans</span>
                                                                                                                                                                                                                                                          </div>

                                                                                                                                                                                                                                                                  <div className="menu-item">
                                                                                                                                                                                                                                                                            <BarChart3 size={20} />
                                                                                                                                                                                                                                                                                      <span>Reports</span>
                                                                                                                                                                                                                                                                                              </div>

                                                                                                                                                                                                                                                                                                      <div className="menu-item">
                                                                                                                                                                                                                                                                                                                <Settings size={20} />
                                                                                                                                                                                                                                                                                                                          <span>Settings</span>
                                                                                                                                                                                                                                                                                                                                  </div>

                                                                                                                                                                                                                                                                                                                                          <div className="menu-item">
                                                                                                                                                                                                                                                                                                                                                    <Database size={20} />
                                                                                                                                                                                                                                                                                                                                                              <span>Backup</span>
                                                                                                                                                                                                                                                                                                                                                                      </div>

                                                                                                                                                                                                                                                                                                                                                                              <div className="menu-item">
                                                                                                                                                                                                                                                                                                                                                                                        <Info size={20} />
                                                                                                                                                                                                                                                                                                                                                                                                  <span>About</span>
                                                                                                                                                                                                                                                                                                                                                                                                          </div>
                                                                                                                                                                                                                                                                                                                                                                                                                </nav>

                                                                                                                                                                                                                                                                                                                                                                                                                      <button className="logout">
                                                                                                                                                                                                                                                                                                                                                                                                                              <LogOut size={18} />
                                                                                                                                                                                                                                                                                                                                                                                                                                      Logout
                                                                                                                                                                                                                                                                                                                                                                                                                                            </button>
                                                                                                                                                                                                                                                                                                                                                                                                                                                </aside>
                                                                                                                                                                                                                                                                                                                                                                                                                                                  );
                                                                                                                                                                                                                                                                                                                                                                                                                                                  }

                                                                                                                                                                                                                                                                                                                                                                                                                        export default Sidebar;
}