import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", books: 40 },
  { month: "Feb", books: 65 },
  { month: "Mar", books: 50 },
  { month: "Apr", books: 85 },
  { month: "May", books: 70 },
  { month: "Jun", books: 95 },
];

function Charts() {
  return (
    <div className="panel">
      <div className="panel-header">
        <h2>Books Issued Per Month</h2>
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="month" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="books" fill="#2563eb" radius={[8, 8, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Charts;