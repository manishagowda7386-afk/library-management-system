import {
  BookOpen,
  Users,
  BookMarked,
  AlertTriangle,
} from "lucide-react";

function DashboardCards() {
  const cards = [
    {
      title: "Total Books",
      value: "1,250",
      subtitle: "+15 this week",
      icon: <BookOpen size={34} />,
      color: "blue",
    },
    {
      title: "Members",
      value: "420",
      subtitle: "+8 this week",
      icon: <Users size={34} />,
      color: "green",
    },
    {
      title: "Active Loans",
      value: "96",
      subtitle: "Currently Issued",
      icon: <BookMarked size={34} />,
      color: "purple",
    },
    {
      title: "Overdue Books",
      value: "12",
      subtitle: "Needs Attention",
      icon: <AlertTriangle size={34} />,
      color: "red",
    },
  ];

  return (
    <section className="cards">
      {cards.map((card, index) => (
        <div className={`card ${card.color}`} key={index}>
          <div className="card-icon">{card.icon}</div>

          <h3>{card.title}</h3>

          <h2>{card.value}</h2>

          <p>{card.subtitle}</p>
        </div>
      ))}
    </section>
  );
}

export default DashboardCards;