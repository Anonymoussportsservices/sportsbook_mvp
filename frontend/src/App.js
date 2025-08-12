import React, { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL.replace(/\/$/, '');
    console.log('Fetching from:', apiUrl + "/api/users");
    fetch(apiUrl + "/api/users")
      .then(res => res.json())
      .then(data => setUsers(data))
      .catch(err => console.error('Fetch error:', err));
  }, []);

  return (
    <div>
      <h1>Sportsbook MVP Frontend</h1>
      <h2>Users List:</h2>
      {users.length === 0 ? (
        <p>Loading users...</p>
      ) : (
        <ul>
          {users.map(user => (
            <li key={user.id}>{user.name} (ID: {user.id})</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
