import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL.replace(/\/$/, '');
    fetch(apiUrl + "/api/users")
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.error('Fetch error:', err));
  }, []);

  return (
    <div>
      <h1>Sportsbook MVP Frontend</h1>
      <p>Check your browser console for the API response.</p>
    </div>
  );
}

export default App;
