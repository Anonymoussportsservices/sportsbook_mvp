import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    fetch('https://sportsbook-mvp2-0.onrender.com/')
      .then(response => response.json())
      .then(data => {
        console.log('API Response:', data);
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  }, []);

  return (
    <div>
      <h1>Sportsbook MVP Frontend</h1>
      <p>Check your browser console for the API response.</p>
    </div>
  );
}

export default App;
