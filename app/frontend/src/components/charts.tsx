import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";

const monthlyData = [
  { month: "Jan", books: 40 },
  { month: "Feb", books: 65 },
  { month: "Mar", books: 50 },
  { month: "Apr", books: 85 },
  { month: "May", books: 70 },
  { month: "Jun", books: 95 },
];

const categoryData = [
  { name: "Programming", value: 40 },
  { name: "AI", value: 20 },
  { name: "Database", value: 15 },
  { name: "Networking", value: 10 },
  { name: "Others", value: 15 },
];

const COLORS = [
  "#2563eb",
  "#10b981",
  "#f59e0b",
  "#ef4444",
  "#8b5cf6",
];

function Charts() {
  return (
    <div className="panel">
      <div className="panel-header">
        <h2>Library Statistics</h2>
      </div>

      <div className="charts-grid">

        <div>
          <h3 className="chart-title">Books Issued</h3>

          <ResponsiveContainer width="100%" height={260}>
            <BarChart data={monthlyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="books" fill="#2563eb" radius={[8,8,0,0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div>
          <h3 className="chart-title">Book Categories</h3>

          <ResponsiveContainer width="100%" height={260}>
            <PieChart>
              <Pie
                data={categoryData}
                cx="50%"
                cy="50%"
                outerRadius={80}
                dataKey="value"
                label
              >
                {categoryData.map((entry, index) => (
                  <Cell
                    key={index}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>

              <Tooltip />

              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

      </div>
    </div>
  );
}

export default Charts;