function RecentLoans() {
  return (
    <div className="panel">
      <div className="panel-header">
        <h2>Recent Loans</h2>

        <button className="view-btn">View All</button>
      </div>

      <table className="loan-table">
        <thead>
          <tr>
            <th>Member</th>
            <th>Book</th>
            <th>Status</th>
            <th>Date</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>John Smith</td>
            <td>Python Basics</td>
            <td>
              <span className="status issued">Issued</span>
            </td>
            <td>21 Jul 2026</td>
          </tr>

          <tr>
            <td>Alice</td>
            <td>React Guide</td>
            <td>
              <span className="status returned">Returned</span>
            </td>
            <td>20 Jul 2026</td>
          </tr>

          <tr>
            <td>David</td>
            <td>Machine Learning</td>
            <td>
              <span className="status overdue">Overdue</span>
            </td>
            <td>17 Jul 2026</td>
          </tr>

          <tr>
            <td>Sophia</td>
            <td>Java Programming</td>
            <td>
              <span className="status issued">Issued</span>
            </td>
            <td>15 Jul 2026</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default RecentLoans;