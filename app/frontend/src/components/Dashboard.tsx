function DashboardCards() {
  const cards = [
    {
      title: "Total Books",
      value: "1,250",
      subtitle: "+15 this week",
      icon: "📚",
      color: "blue",
    },
    {
      title: "Members",
      value: "420",
      subtitle: "+8 this week",
      icon: "👥",
      color: "green",
    },
    {
      title: "Active Loans",
      value: "96",
      subtitle: "Currently Issued",
      icon: "🔄",
      color: "purple",
    },
    {
      title: "Overdue Books",
      value: "12",
      subtitle: "Needs Attention",
      icon: "⚠️",
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