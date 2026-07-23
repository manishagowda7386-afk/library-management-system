function BooksTable() {
  return (
    <div className="panel">
      <div className="panel-header">
        <h2>Books Overview</h2>

        <button className="view-btn">View All</button>
      </div>

      <table className="books-table">
        <thead>
          <tr>
            <th>Book</th>
            <th>Author</th>
            <th>Available</th>
            <th>Category</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>Python Basics</td>
            <td>Guido van Rossum</td>
            <td>12</td>
            <td>Programming</td>
          </tr>

          <tr>
            <td>React Guide</td>
            <td>Meta</td>
            <td>7</td>
            <td>Web</td>
          </tr>

          <tr>
            <td>Java Programming</td>
            <td>James Gosling</td>
            <td>5</td>
            <td>Programming</td>
          </tr>

          <tr>
            <td>Machine Learning</td>
            <td>Andrew Ng</td>
            <td>3</td>
            <td>AI</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default BooksTable;