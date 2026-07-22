function QuickActions() {
  return (
    <div className="quick-actions">
      <h2>Quick Actions</h2>

      <div className="action-grid">
        <button className="action-btn blue-btn">
          📚
          <span>Add Book</span>
        </button>

        <button className="action-btn green-btn">
          👤
          <span>Add Member</span>
        </button>

        <button className="action-btn purple-btn">
          🔄
          <span>Issue Book</span>
        </button>

        <button className="action-btn orange-btn">
          ↩
          <span>Return Book</span>
        </button>
      </div>
    </div>
  );
}

export default QuickActions;