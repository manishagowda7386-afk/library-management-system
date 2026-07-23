import {
  Plus,
  UserPlus,
  BookUp,
  Undo2,
} from "lucide-react";

function QuickActions() {
  return (
    <div className="quick-actions">
      <h2>Quick Actions</h2>

      <div className="action-grid">
        <button className="action-btn blue-btn">
          <Plus size={28} />
          <span>Add Book</span>
        </button>

        <button className="action-btn green-btn">
          <UserPlus size={28} />
          <span>Add Member</span>
        </button>

        <button className="action-btn purple-btn">
          <BookUp size={28} />
          <span>Issue Book</span>
        </button>

        <button className="action-btn orange-btn">
          <Undo2 size={28} />
          <span>Return Book</span>
        </button>
      </div>
    </div>
  );
}

export default QuickActions;